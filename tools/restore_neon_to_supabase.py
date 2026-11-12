"""Restore a verified Neon staging snapshot into an explicitly identified Supabase staging project.

This is a manual recovery utility only. It is never imported by the bot and
never acts as a runtime fallback. Both databases must carry operator-managed
PostgreSQL identity markers before any table replacement is possible.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit


def _parsed_postgres_url(value: str, label: str):
    parsed = urlsplit(value)
    if parsed.scheme not in {"postgres", "postgresql"} or not parsed.hostname:
        raise ValueError(f"{label} must be a PostgreSQL connection URL")
    if parsed.username is None or parsed.password is None:
        raise ValueError(f"{label} must contain database authentication credentials")
    return parsed


def _is_neon_host(host: str) -> bool:
    return host.endswith(".neon.tech")


def _is_supabase_host(host: str) -> bool:
    return host.endswith(".supabase.com") or host.endswith(".supabase.co")


def _quote_identifier(value: str) -> str:
    return '"' + value.replace('"', '""') + '"'


def _manifest_path(path_value: str) -> Path:
    path = Path(path_value).expanduser().resolve()
    project_root = Path(__file__).resolve().parents[1]
    if path == project_root or project_root in path.parents:
        raise ValueError("Keep the pre-restore backup marker outside the project and release directory")
    if not path.is_file():
        raise ValueError("A verified pre-restore backup marker file is required")
    return path


def validate_restore_targets(
    source_url: str,
    target_url: str,
    expected_source_host: str,
    expected_target_host: str,
    expected_source_project_id: str,
    expected_target_project_id: str,
    confirm_overwrite: bool,
) -> tuple[str, str]:
    """Validate provider direction and operator-confirmed staging identities."""
    source = _parsed_postgres_url(source_url, "NEON_DATABASE_URL")
    target = _parsed_postgres_url(target_url, "DATABASE_URL")
    source_host = source.hostname.lower()
    target_host = target.hostname.lower()
    if source_host == target_host or source_url == target_url:
        raise ValueError("Source and destination must be different database endpoints")
    if not _is_neon_host(source_host):
        raise ValueError("Recovery source must be a Neon PostgreSQL endpoint")
    if not _is_supabase_host(target_host):
        raise ValueError("Recovery destination must be a Supabase PostgreSQL endpoint")
    if source_host != (expected_source_host or "").strip().lower():
        raise ValueError("Neon source hostname does not match the explicitly confirmed hostname")
    if target_host != (expected_target_host or "").strip().lower():
        raise ValueError("Supabase destination hostname does not match the explicitly confirmed hostname")
    if not expected_source_project_id or not expected_target_project_id:
        raise ValueError("Explicit source and destination staging project IDs are required")
    if expected_source_project_id == expected_target_project_id:
        raise ValueError("Source and destination project identities must be different")
    if not confirm_overwrite:
        raise ValueError("Explicit destructive overwrite authorization is required")
    return source_host, target_host


def verify_database_identity(conn, expected_project_id: str, label: str) -> dict[str, str]:
    row = conn.execute(
        "SELECT current_setting('classcode.environment', true) AS environment, "
        "current_setting('classcode.project_id', true) AS project_id, "
        "current_database() AS database_name"
    ).fetchone()
    environment = (row.get("environment") or "").strip().lower()
    project_id = (row.get("project_id") or "").strip()
    database_name = (row.get("database_name") or "").strip()
    if environment != "staging":
        raise ValueError(f"{label} database environment marker is missing or is not staging")
    if not project_id or project_id != expected_project_id:
        raise ValueError(f"{label} database project identity marker does not match the operator confirmation")
    if not database_name:
        raise ValueError(f"{label} database name could not be verified")
    return {"environment": environment, "project_id": project_id, "database_name": database_name}


def verify_pre_restore_backup(
    marker_path: Path,
    expected_destination_host: str,
    restore_source_host: str,
    required_tables: list[str],
) -> dict:
    """Require a successful, row-count-verified snapshot of the destination itself."""
    if not marker_path.is_file():
        raise ValueError("Pre-restore backup marker does not exist")
    try:
        marker = json.loads(marker_path.read_text(encoding="utf-8"))
    except Exception:
        raise ValueError("Pre-restore backup marker is unreadable or invalid JSON") from None
    if marker.get("status") != "succeeded" or marker.get("verification") != "row_counts_passed":
        raise ValueError("Pre-restore backup marker does not report a verified successful snapshot")
    if (marker.get("source_host") or "").lower() != expected_destination_host:
        raise ValueError("Pre-restore backup was not taken from the exact restore destination")
    backup_target = (marker.get("target_host") or "").lower()
    if not backup_target or backup_target == restore_source_host or not _is_neon_host(backup_target):
        raise ValueError("Pre-restore backup must be stored in a separate Neon endpoint, not the restore source")
    counts = marker.get("table_counts")
    if not isinstance(counts, dict) or not set(required_tables).issubset(counts):
        raise ValueError("Pre-restore backup marker does not verify every required ClassCode table")
    if any(not isinstance(counts[name], int) or counts[name] < 0 for name in required_tables):
        raise ValueError("Pre-restore backup marker contains invalid table row counts")
    if not marker.get("completed_at"):
        raise ValueError("Pre-restore backup marker is missing its completion timestamp")
    return marker


def _classcode_tables(schema_path: Path) -> list[str]:
    schema_text = schema_path.read_text(encoding="utf-8")
    tables = sorted(set(re.findall(
        r"(?i)CREATE\s+TABLE\s+IF\s+NOT\s+EXISTS\s+([a-z_][a-z0-9_]*)",
        schema_text,
    )))
    if not tables:
        raise RuntimeError("Could not determine ClassCode tables from postgres_schema.sql")
    return tables


def restore_snapshot(
    source_url: str,
    target_url: str,
    expected_source_host: str,
    expected_target_host: str,
    expected_source_project_id: str,
    expected_target_project_id: str,
    confirm_overwrite: bool,
    backup_marker: Path,
    connect,
    schema_path: Path | None = None,
) -> dict[str, int]:
    """Restore only after independent staging identity and backup checks pass."""
    source_host, target_host = validate_restore_targets(
        source_url, target_url, expected_source_host, expected_target_host,
        expected_source_project_id, expected_target_project_id, confirm_overwrite,
    )
    if schema_path is None:
        schema_path = Path(__file__).resolve().parents[1] / "bot" / "postgres_schema.sql"
    tables = _classcode_tables(schema_path)
    verify_pre_restore_backup(backup_marker, target_host, source_host, tables)
    counts: dict[str, int] = {}

    with connect(source_url, connect_timeout=10, sslmode="require") as source:
        source.execute("SET TRANSACTION ISOLATION LEVEL REPEATABLE READ READ ONLY")
        source_identity = verify_database_identity(source, expected_source_project_id, "Neon source")
        source.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE'")
        source_available = {row["table_name"] for row in source.fetchall()}
        missing_source = sorted(set(tables) - source_available)
        if missing_source:
            raise RuntimeError("Neon staging snapshot is missing required ClassCode tables: " + ", ".join(missing_source))

        with connect(target_url, connect_timeout=10, sslmode="require") as target:
            target_identity = verify_database_identity(target, expected_target_project_id, "Supabase destination")
            if source_identity["project_id"] == target_identity["project_id"]:
                raise ValueError("Source and destination database identities resolve to the same project")
            target.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE'")
            target_available = {row["table_name"] for row in target.fetchall()}
            missing_target = sorted(set(tables) - target_available)
            if missing_target:
                raise RuntimeError("Supabase staging destination is missing required ClassCode tables: " + ", ".join(missing_target))

            source_columns: dict[str, list[str]] = {}
            for table in tables:
                source.execute(
                    "SELECT column_name FROM information_schema.columns WHERE table_schema='public' AND table_name=%s ORDER BY ordinal_position",
                    (table,),
                )
                source_columns[table] = [row["column_name"] for row in source.fetchall()]
                target.execute(
                    "SELECT column_name FROM information_schema.columns WHERE table_schema='public' AND table_name=%s ORDER BY ordinal_position",
                    (table,),
                )
                target_cols = [row["column_name"] for row in target.fetchall()]
                if not source_columns[table] or source_columns[table] != target_cols:
                    raise RuntimeError(f"Column mismatch for {table}; destination schema must be reconciled before recovery")

            with target.transaction():
                target.execute(
                    "TRUNCATE TABLE " + ", ".join(f"public.{_quote_identifier(table)}" for table in tables)
                    + " RESTART IDENTITY"
                )
                for table in tables:
                    columns = source_columns[table]
                    quoted_columns = ", ".join(_quote_identifier(column) for column in columns)
                    quoted_table = f"public.{_quote_identifier(table)}"
                    insert_sql = (
                        f"INSERT INTO {quoted_table} ({quoted_columns}) VALUES ("
                        + ", ".join(["%s"] * len(columns)) + ")"
                    )
                    source_cursor = source.cursor()
                    source_cursor.execute(f"SELECT {quoted_columns} FROM {quoted_table}")
                    copied = 0
                    try:
                        while True:
                            rows = source_cursor.fetchmany(500)
                            if not rows:
                                break
                            target_cursor = target.cursor()
                            try:
                                target_cursor.executemany(insert_sql, [tuple(row[column] for column in columns) for row in rows])
                            finally:
                                target_cursor.close()
                            copied += len(rows)
                    finally:
                        source_cursor.close()
                    target.execute(f"SELECT COUNT(*) AS row_count FROM {quoted_table}")
                    target_count = target.fetchone()["row_count"]
                    if target_count != copied:
                        raise RuntimeError(f"Row-count verification failed for {table}")
                    counts[table] = copied

                target.execute(
                    "SELECT table_name, column_name FROM information_schema.columns "
                    "WHERE table_schema='public' AND table_name = ANY(%s) AND "
                    "(is_identity='YES' OR column_default LIKE 'nextval(%')",
                    (tables,),
                )
                for sequence_column in target.fetchall():
                    table, column = sequence_column["table_name"], sequence_column["column_name"]
                    target.execute(f"SELECT MAX({_quote_identifier(column)}) AS max_id FROM public.{_quote_identifier(table)}")
                    max_id = target.fetchone()["max_id"]
                    if max_id is not None:
                        target.execute("SELECT setval(pg_get_serial_sequence(%s, %s), %s, true)", (f"public.{table}", column, max_id))
    return counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--confirm-overwrite", action="store_true", help="Authorize replacement of all ClassCode tables in the staging destination")
    parser.add_argument("--confirm-staging-target", action="store_true", help="Confirm that both independently marked databases are disposable staging projects")
    parser.add_argument("--expected-source-host", required=True)
    parser.add_argument("--expected-target-host", required=True)
    parser.add_argument("--expected-source-project-id", required=True)
    parser.add_argument("--expected-target-project-id", required=True)
    parser.add_argument("--pre-restore-backup-marker", required=True, help="Verified marker from a backup of the destination to a separate Neon endpoint")
    args = parser.parse_args()
    source_url = os.getenv("NEON_DATABASE_URL", "").strip()
    target_url = os.getenv("DATABASE_URL", "").strip()
    try:
        if not args.confirm_staging_target:
            raise ValueError("Explicit --confirm-staging-target is required")
        backup_marker = _manifest_path(args.pre_restore_backup_marker)
        validate_restore_targets(
            source_url, target_url, args.expected_source_host, args.expected_target_host,
            args.expected_source_project_id, args.expected_target_project_id, args.confirm_overwrite,
        )
        tables = _classcode_tables(Path(__file__).resolve().parents[1] / "bot" / "postgres_schema.sql")
        verify_pre_restore_backup(backup_marker, args.expected_target_host.strip().lower(), args.expected_source_host.strip().lower(), tables)
        import psycopg
        from psycopg.rows import dict_row
        def connect_with_dict_rows(*connect_args, **connect_kwargs):
            connect_kwargs["row_factory"] = dict_row
            return psycopg.connect(*connect_args, **connect_kwargs)
        counts = restore_snapshot(
            source_url, target_url, args.expected_source_host, args.expected_target_host,
            args.expected_source_project_id, args.expected_target_project_id,
            args.confirm_overwrite, backup_marker, connect_with_dict_rows,
        )
    except Exception as exc:
        sqlstate = getattr(exc, "sqlstate", None)
        diagnostic = f" SQLSTATE={sqlstate}." if sqlstate else ""
        print(f"Restore refused or failed ({type(exc).__name__}).{diagnostic} No connection details were logged.", file=sys.stderr)
        return 2
    print(f"Staging restore completed at {datetime.now(timezone.utc).isoformat()}.")
    for table, count in sorted(counts.items()):
        print(f"Restored {table}: {count} rows (verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
