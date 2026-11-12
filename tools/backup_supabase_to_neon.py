"""Create a full, transactional snapshot of Supabase's public tables in Neon.

This deliberately overwrites the Neon backup contents. It is never run by the
bot at startup; invoke it from a scheduled job only after reviewing the target.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import json
import os
import sys
import re
from pathlib import Path
from urllib.parse import urlsplit


def _is_supabase_url(url: str) -> bool:
    host = (urlsplit(url).hostname or "").lower()
    return host.endswith(".supabase.com") or host.endswith(".supabase.co")


def _is_neon_url(url: str) -> bool:
    host = (urlsplit(url).hostname or "").lower()
    return host.endswith(".neon.tech")


def _quote_identifier(value: str) -> str:
    """Quote a PostgreSQL identifier returned by trusted schema metadata."""
    return '"' + value.replace('"', '""') + '"'


def _write_success_status(path: str | None, started_at: datetime, completed_at: datetime, counts: dict[str, int], source_host: str, target_host: str) -> None:
    if not path:
        return
    status_path = Path(path)
    status_path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = status_path.with_name(f"{status_path.name}.{os.getpid()}.tmp")
    payload = {
        "status": "succeeded",
        "started_at": started_at.isoformat(),
        "completed_at": completed_at.isoformat(),
        "verification": "row_counts_passed",
        "source_host": source_host,
        "target_host": target_host,
        "table_counts": counts,
    }
    try:
        temp_path.write_text(json.dumps(payload, sort_keys=True) + "\n", encoding="utf-8")
        os.replace(temp_path, status_path)
    finally:
        if temp_path.exists():
            temp_path.unlink()


def _invalidate_success_status(path: str | None) -> None:
    """Ensure a failed current attempt cannot leave an older marker looking current."""
    if not path:
        return
    try:
        Path(path).unlink()
    except FileNotFoundError:
        pass


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--confirm-overwrite", action="store_true", help="Required because this replaces Neon backup contents")
    parser.add_argument("--status-file", help="Optional private JSON marker for completion/age monitoring")
    args = parser.parse_args()
    source_url = os.getenv("DATABASE_URL", "").strip()
    target_url = os.getenv("NEON_DATABASE_URL", "").strip()
    if not source_url or not target_url:
        parser.error("Both DATABASE_URL (Supabase primary) and NEON_DATABASE_URL (Neon backup) are required")
    if source_url == target_url:
        parser.error("DATABASE_URL and NEON_DATABASE_URL point to the same string; refusing to back up to itself")
    if not _is_supabase_url(source_url):
        parser.error("DATABASE_URL must point to Supabase; Neon is reserved for backups")
    if not _is_neon_url(target_url):
        parser.error("NEON_DATABASE_URL must point to Neon")
    if not args.confirm_overwrite:
        parser.error("This replaces the Neon snapshot. Re-run with --confirm-overwrite after verifying both connection strings")
    # Remove the previous success marker before attempting I/O. If this run
    # fails or is interrupted, the age checker will report a missing marker.
    _invalidate_success_status(args.status_file)
    try:
        import psycopg
        from psycopg.rows import dict_row
    except ImportError:
        parser.error("Install requirements.txt first (includes psycopg[binary])")

    started_at = datetime.now(timezone.utc)
    print(f"Backup started at {started_at.isoformat()}")
    counts: dict[str, int] = {}

    # One repeatable-read transaction guarantees all source tables come from the
    # same logical snapshot. The target replacement is one transaction too, so
    # a failure rolls back and preserves the previous Neon backup.
    with psycopg.connect(source_url, connect_timeout=10, sslmode="require", row_factory=dict_row) as source:
        source.execute("SET TRANSACTION ISOLATION LEVEL REPEATABLE READ READ ONLY")
        schema_path = Path(__file__).resolve().parents[1] / "bot" / "postgres_schema.sql"
        schema_text = schema_path.read_text(encoding="utf-8")
        tables = sorted(set(re.findall(r"(?i)CREATE\s+TABLE\s+IF\s+NOT\s+EXISTS\s+([a-z_][a-z0-9_]*)", schema_text)))
        if not tables:
            print("Could not determine ClassCode application tables from postgres_schema.sql.", file=sys.stderr)
            return 2
        source.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE'")
        source_available = {r["table_name"] for r in source.fetchall()}
        missing_source = sorted(set(tables) - source_available)
        if missing_source:
            print("Supabase is missing ClassCode tables: " + ", ".join(missing_source), file=sys.stderr)
            return 2

        with psycopg.connect(target_url, connect_timeout=10, sslmode="require", row_factory=dict_row) as target:
            target.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE'")
            target_available = {r["table_name"] for r in target.fetchall()}
            missing_target = sorted(set(tables) - target_available)
            if missing_target:
                print("Neon is missing ClassCode tables. Apply the ClassCode schema to Neon first: " + ", ".join(missing_target), file=sys.stderr)
                return 2

            with target.transaction():
                # Do not cascade into unrelated tables in a shared Neon database.
                # If another table references these, fail and preserve the old backup.
                target.execute(
                    "TRUNCATE TABLE "
                    + ", ".join(f"public.{_quote_identifier(t)}" for t in tables)
                    + " RESTART IDENTITY"
                )
                for table in tables:
                    source.execute("SELECT column_name FROM information_schema.columns WHERE table_schema='public' AND table_name=%s ORDER BY ordinal_position", (table,))
                    source_columns = [r["column_name"] for r in source.fetchall()]
                    target.execute("SELECT column_name FROM information_schema.columns WHERE table_schema='public' AND table_name=%s ORDER BY ordinal_position", (table,))
                    target_columns = [r["column_name"] for r in target.fetchall()]
                    if source_columns != target_columns:
                        raise RuntimeError(f"Column mismatch for {table}; update the Neon schema before backing up")
                    quoted_columns = ", ".join(_quote_identifier(c) for c in source_columns)
                    quoted_table = f"public.{_quote_identifier(table)}"
                    insert_sql = f"INSERT INTO {quoted_table} ({quoted_columns}) VALUES (" + ", ".join(["%s"] * len(source_columns)) + ")"
                    source_cursor = source.cursor()
                    source_cursor.execute(f"SELECT {quoted_columns} FROM {quoted_table}")
                    copied = 0
                    while True:
                        rows = source_cursor.fetchmany(500)
                        if not rows:
                            break
                        target_cursor = target.cursor()
                        target_cursor.executemany(insert_sql, [tuple(row[c] for c in source_columns) for row in rows])
                        target_cursor.close()
                        copied += len(rows)
                    source_cursor.close()
                    target_count = target.execute(
                        f"SELECT COUNT(*) AS row_count FROM {quoted_table}"
                    ).fetchone()["row_count"]
                    if target_count != copied:
                        raise RuntimeError(f"Row-count verification failed for {table}")
                    counts[table] = copied
                    print(f"Backed up {table}: {copied} rows")

                # Restore both IDENTITY and SERIAL/BIGSERIAL sequences after
                # copying explicit IDs; TRUNCATE RESTART IDENTITY alone does
                # not cover sequences backed by SERIAL defaults.
                target.execute(
                    "SELECT table_name, column_name FROM information_schema.columns "
                    "WHERE table_schema='public' AND table_name = ANY(%s) AND "
                    "(is_identity='YES' OR column_default LIKE 'nextval(%')",
                    (tables,),
                )
                for sequence_column in target.fetchall():
                    table, column = sequence_column["table_name"], sequence_column["column_name"]
                    quoted_table = f"public.{_quote_identifier(table)}"
                    quoted_column = _quote_identifier(column)
                    target.execute(f"SELECT MAX({quoted_column}) AS max_id FROM {quoted_table}")
                    max_id = target.fetchone()["max_id"]
                    if max_id is not None:
                        target.execute("SELECT setval(pg_get_serial_sequence(%s, %s), %s, true)", (f'public.{table}', column, max_id))
            target.commit()
        source.commit()

    completed_at = datetime.now(timezone.utc)
    _write_success_status(args.status_file, started_at, completed_at, counts, (urlsplit(source_url).hostname or "").lower(), (urlsplit(target_url).hostname or "").lower())
    print(f"Neon backup snapshot completed at {completed_at.isoformat()}.")
    print("Row counts were verified. Run a restore verification before relying on it for disaster recovery.")
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SystemExit:
        raise
    except Exception as exc:
        sqlstate = getattr(exc, "sqlstate", None)
        diagnostic = f" SQLSTATE={sqlstate}." if sqlstate else ""
        print(
            f"Backup failed ({type(exc).__name__}).{diagnostic} "
            "Check the private backup-job logs. Confirm the Neon snapshot before retrying.",
            file=sys.stderr,
        )
        raise SystemExit(1) from None
