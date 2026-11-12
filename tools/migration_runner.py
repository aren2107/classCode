
"""Explicit, staging-only PostgreSQL migration runner with fail-closed tracking."""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import os
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit

FORWARD_MIGRATION_FILES = (
    "2026-11-01_practice_quiz_xp_rewards.sql",
    "2026-11-01_integrity_constraints.sql",
    "2026-11-03_daily_submissions_manila_timezone.sql",
)

ROLLBACK_SOURCE_FILES = (
    "2026-11-01_integrity_constraints_rollback.sql",
)

REQUIRED_SOURCE_FILES = FORWARD_MIGRATION_FILES + ROLLBACK_SOURCE_FILES

TRACKING_TABLE = "classcode_schema_migrations"
ADVISORY_LOCK_KEY = 728194631

# Exact objects created by 2026-11-01_integrity_constraints.sql.
EXPECTED_FOREIGN_KEYS = {
    "fk_cc_user_progress_user_id_users": "user_progress",
    "fk_cc_quiz_attempts_user_id_users": "quiz_attempts",
    "fk_cc_practice_quiz_xp_rewards_user_id_users": "practice_quiz_xp_rewards",
    "fk_cc_user_badges_user_id_users": "user_badges",
    "fk_cc_daily_submissions_user_id_users": "daily_submissions",
    "fk_cc_xp_history_user_id_users": "xp_history",
    "fk_cc_daily_goals_user_id_users": "daily_goals",
    "fk_cc_project_progress_user_id_users": "project_progress",
    "fk_cc_project_progress_project_id_projects": "project_progress",
    "fk_cc_classes_teacher_id_users": "classes",
    "fk_cc_class_members_class_id_classes": "class_members",
    "fk_cc_class_members_user_id_users": "class_members",
    "fk_cc_assignments_class_id_classes": "assignments",
    "fk_cc_assignment_submissions_assignment_id_assignments": "assignment_submissions",
    "fk_cc_assignment_submissions_user_id_users": "assignment_submissions",
    "fk_cc_code_snippets_user_id_users": "code_snippets",
    "fk_cc_personal_notes_user_id_users": "personal_notes",
    "fk_cc_user_titles_user_id_users": "user_titles",
    "fk_cc_user_stats_user_id_users": "user_stats",
    "fk_cc_daily_missions_user_id_users": "daily_missions",
    "fk_cc_bug_attempts_user_id_users": "bug_attempts",
    "fk_cc_bug_attempts_puzzle_id_bug_puzzles": "bug_attempts",
    "fk_cc_study_groups_owner_id_users": "study_groups",
    "fk_cc_study_group_members_group_id_study_groups": "study_group_members",
    "fk_cc_study_group_members_user_id_users": "study_group_members",
    "fk_cc_pair_queue_user_id_users": "pair_queue",
    "fk_cc_event_progress_user_id_users": "event_progress",
    "fk_cc_portfolio_projects_user_id_users": "portfolio_projects",
    "fk_cc_portfolio_projects_project_id_projects": "portfolio_projects",
    "fk_cc_certificates_user_id_users": "certificates",
    "fk_cc_practical_exams_created_by_users": "practical_exams",
    "fk_cc_practical_exam_submissions_exam_id_practical_exams": "practical_exam_submissions",
    "fk_cc_practical_exam_submissions_user_id_users": "practical_exam_submissions",
    "fk_cc_attendance_records_user_id_users": "attendance_records",
    "fk_cc_lesson_mastery_user_id_users": "lesson_mastery",
}

EXPECTED_INDEXES = {
    "ix_cc_quiz_attempts_user_attempted": "quiz_attempts",
    "ix_cc_xp_history_user_id": "xp_history",
    "ix_cc_project_progress_project_user": "project_progress",
    "ix_cc_classes_teacher_class": "classes",
    "ix_cc_class_members_user_class": "class_members",
    "ix_cc_assignments_class_assignment": "assignments",
    "ix_cc_assignment_submissions_user_assignment": "assignment_submissions",
    "ix_cc_code_snippets_user_snippet": "code_snippets",
    "ix_cc_personal_notes_user_title_note": "personal_notes",
    "ix_cc_bug_attempts_puzzle_user": "bug_attempts",
    "ix_cc_study_groups_owner_group": "study_groups",
    "ix_cc_study_group_members_user_group": "study_group_members",
    "ix_cc_portfolio_projects_project_user": "portfolio_projects",
    "ix_cc_certificates_user_certificate": "certificates",
    "ix_cc_practical_exams_creator_exam": "practical_exams",
    "ix_cc_practical_exam_submissions_exam_submission": "practical_exam_submissions",
    "ix_cc_practical_exam_submissions_user_submitted": "practical_exam_submissions",
}


@dataclass(frozen=True)
class Migration:
    migration_id: str
    path: Path
    sha256: str
    sql: str


class MigrationStateError(RuntimeError):
    pass


def load_migrations(directory: Path) -> list[Migration]:
    """Load only approved forward migrations in their declared order."""
    missing = [
        name for name in REQUIRED_SOURCE_FILES
        if not (directory / name).is_file()
    ]
    if missing:
        raise MigrationStateError(
            "Required migration source is missing: " + ", ".join(missing)
        )

    allowed_sql = set(REQUIRED_SOURCE_FILES)
    present_sql = {path.name for path in directory.glob("*.sql")}
    unexpected = sorted(present_sql - allowed_sql)
    if unexpected:
        raise MigrationStateError(
            "Unexpected SQL file(s) in migrations directory; "
            "explicitly review and allowlist: " + ", ".join(unexpected)
        )

    migrations = []
    for name in FORWARD_MIGRATION_FILES:
        path = directory / name
        migration_id = path.stem

        if not re.fullmatch(
            r"[0-9]{4}-[0-9]{2}-[0-9]{2}_[a-z0-9_]+",
            migration_id,
        ):
            raise MigrationStateError(
                f"Invalid migration filename: {path.name}"
            )

        sql = path.read_text(encoding="utf-8")
        if not sql.strip():
            raise MigrationStateError(f"Migration is empty: {path.name}")

        migrations.append(Migration(
            migration_id=migration_id,
            path=path,
            sha256=hashlib.sha256(sql.encode("utf-8")).hexdigest(),
            sql=sql,
        ))

    return migrations


def classify_migration_state(
    migrations: list[Migration],
    existing_rows: list[dict],
) -> list[Migration]:
    """Reject unknown, changed, duplicate, failed, partial, or out-of-order state."""
    available = {item.migration_id: item for item in migrations}
    known = {}

    for row in existing_rows:
        migration_id = row["migration_id"]

        if migration_id in known:
            raise MigrationStateError(
                f"Duplicate tracking records for migration {migration_id}"
            )

        known[migration_id] = row

        if migration_id not in available:
            raise MigrationStateError(
                f"Database tracks migration absent from source tree: {migration_id}"
            )

        migration = available[migration_id]
        if row["sha256"] != migration.sha256:
            raise MigrationStateError(
                f"Applied migration source hash changed: {migration_id}"
            )

        if row["status"] != "applied":
            raise MigrationStateError(
                f"Migration {migration_id} has status '{row['status']}'; "
                "manual schema inspection is required before continuing"
            )

        if row.get("applied_at") is None:
            raise MigrationStateError(
                f"Migration {migration_id} is marked applied without an applied timestamp"
            )

    # Applied migrations must form a continuous prefix of the declared order.
    missing_seen = False

    for migration in migrations:
        if migration.migration_id not in known:
            missing_seen = True
        elif missing_seen:
            raise MigrationStateError(
                f"Migration history is out of order: "
                f"{migration.migration_id} is applied while an earlier "
                "migration is missing"
            )

    return [
        item for item in migrations
        if item.migration_id not in known
    ]


def validate_staging_url(
    url: str,
    expected_host: str,
    expected_project_id: str,
) -> str:
    try:
        parsed = urlsplit(url)
        port = parsed.port
    except ValueError:
        raise ValueError(
            "STAGING_DATABASE_URL contains an invalid URL or port"
        ) from None

    if parsed.scheme not in {"postgres", "postgresql"}:
        raise ValueError(
            "STAGING_DATABASE_URL must use a PostgreSQL URL scheme"
        )

    if not parsed.hostname:
        raise ValueError(
            "STAGING_DATABASE_URL must contain a hostname"
        )

    if parsed.username is None or parsed.password is None:
        raise ValueError(
            "STAGING_DATABASE_URL must contain database credentials"
        )

    if not parsed.path or parsed.path == "/":
        raise ValueError(
            "STAGING_DATABASE_URL must specify a database name"
        )

    if parsed.query or parsed.fragment:
        raise ValueError(
            "STAGING_DATABASE_URL must not contain query parameters or fragments"
        )

    if port not in {None, 5432, 6543}:
        raise ValueError(
            "STAGING_DATABASE_URL uses an unsupported PostgreSQL port"
        )

    host = parsed.hostname.lower()
    confirmed_host = (expected_host or "").strip().lower()
    project_id = (expected_project_id or "").strip().lower()

    if not re.fullmatch(r"[a-z0-9]{20}", project_id):
        raise ValueError(
            "Expected project ID must be a valid 20-character Supabase project reference"
        )

    expected_project_host = f"db.{project_id}.supabase.co"

    if host != expected_project_host:
        raise ValueError(
            "Database hostname does not identify the expected Supabase project"
        )

    if confirmed_host != expected_project_host:
        raise ValueError(
            "Expected hostname must exactly match the confirmed project database hostname"
        )

    return host


def validate_staging_ca(certificate_path: str) -> str:
    if not certificate_path.strip():
        raise ValueError(
            "STAGING_SSLROOTCERT must point to the Supabase root certificate"
        )

    path = Path(certificate_path).expanduser()
    if not path.is_file():
        raise ValueError(
            "STAGING_SSLROOTCERT does not point to an existing certificate file"
        )

    return str(path.resolve())


def _establish_transaction_staging_identity(
    conn,
    expected_project_id: str,
) -> None:
    """Set transaction-local guards; these do not independently prove identity."""
    conn.execute(
        "SELECT set_config('classcode.environment', %s, true)",
        ("staging",),
    )
    conn.execute(
        "SELECT set_config('classcode.project_id', %s, true)",
        (expected_project_id,),
    )
    _verify_staging_identity(conn, expected_project_id)


def _verify_staging_identity(conn, expected_project_id: str) -> None:
    row = conn.execute(
        "SELECT current_setting('classcode.environment', true) AS environment, "
        "current_setting('classcode.project_id', true) AS project_id"
    ).fetchone()

    if (row.get("environment") or "").strip().lower() != "staging":
        raise MigrationStateError(
            "Database staging environment marker is missing or invalid"
        )

    if (row.get("project_id") or "").strip() != expected_project_id:
        raise MigrationStateError(
            "Database staging project identity marker does not match"
        )


def _normalized_default(value: str | None) -> str:
    return re.sub(r"\s+", "", value or "").lower()


def verify_existing_xp_ledger(conn) -> None:
    """Require the exact approved XP ledger shape if the table already exists."""
    exists = conn.execute(
        "SELECT 1 FROM information_schema.tables "
        "WHERE table_schema='public' "
        "AND table_name='practice_quiz_xp_rewards'"
    ).fetchone()

    if not exists:
        return

    rows = conn.execute(
        "SELECT column_name, data_type, is_nullable, column_default "
        "FROM information_schema.columns "
        "WHERE table_schema='public' "
        "AND table_name='practice_quiz_xp_rewards' "
        "ORDER BY ordinal_position"
    ).fetchall()

    actual = [
        (row["column_name"], row["data_type"], row["is_nullable"])
        for row in rows
    ]
    expected = [
        ("user_id", "bigint", "NO"),
        ("language", "text", "NO"),
        ("topic_id", "text", "NO"),
        ("xp_awarded", "bigint", "NO"),
        ("recorded_at", "timestamp without time zone", "YES"),
    ]

    if actual != expected:
        raise MigrationStateError(
            "Existing practice_quiz_xp_rewards columns do not match the approved ledger shape"
        )

    if _normalized_default(rows[-1]["column_default"]) != "current_timestamp":
        raise MigrationStateError(
            "Existing practice_quiz_xp_rewards.recorded_at default is incompatible"
        )

    key_rows = conn.execute(
        "SELECT kcu.column_name "
        "FROM information_schema.table_constraints tc "
        "JOIN information_schema.key_column_usage kcu "
        "ON tc.constraint_name=kcu.constraint_name "
        "AND tc.table_schema=kcu.table_schema "
        "AND tc.table_name=kcu.table_name "
        "WHERE tc.table_schema='public' "
        "AND tc.table_name='practice_quiz_xp_rewards' "
        "AND tc.constraint_type='PRIMARY KEY' "
        "ORDER BY kcu.ordinal_position"
    ).fetchall()

    if [row["column_name"] for row in key_rows] != [
        "user_id", "language", "topic_id"
    ]:
        raise MigrationStateError(
            "Existing practice_quiz_xp_rewards primary key is incompatible"
        )


def verify_tracking_table(conn) -> None:
    """Validate the tracking table instead of trusting CREATE TABLE IF NOT EXISTS."""
    rows = conn.execute(
        "SELECT column_name, data_type, character_maximum_length, "
        "is_nullable, column_default "
        "FROM information_schema.columns "
        "WHERE table_schema='public' "
        "AND table_name=%s ORDER BY ordinal_position",
        (TRACKING_TABLE,),
    ).fetchall()

    expected = [
        ("migration_id", "text", None, "NO"),
        ("sha256", "character", 64, "NO"),
        ("status", "text", None, "NO"),
        ("started_at", "timestamp with time zone", None, "NO"),
        ("applied_at", "timestamp with time zone", None, "YES"),
        ("last_error_class", "text", None, "YES"),
    ]

    actual = [
        (
            row["column_name"],
            row["data_type"],
            row["character_maximum_length"],
            row["is_nullable"],
        )
        for row in rows
    ]

    if actual != expected:
        raise MigrationStateError(
            "Existing migration tracking table columns are incompatible"
        )

    started_at_default = _normalized_default(rows[3]["column_default"])
    if started_at_default != "current_timestamp":
        raise MigrationStateError(
            "Migration tracking started_at default is incompatible"
        )

    pk_rows = conn.execute(
        "SELECT kcu.column_name "
        "FROM information_schema.table_constraints tc "
        "JOIN information_schema.key_column_usage kcu "
        "ON tc.constraint_name=kcu.constraint_name "
        "AND tc.table_schema=kcu.table_schema "
        "AND tc.table_name=kcu.table_name "
        "WHERE tc.table_schema='public' "
        "AND tc.table_name=%s "
        "AND tc.constraint_type='PRIMARY KEY' "
        "ORDER BY kcu.ordinal_position",
        (TRACKING_TABLE,),
    ).fetchall()

    if [row["column_name"] for row in pk_rows] != ["migration_id"]:
        raise MigrationStateError(
            "Migration tracking table primary key is incompatible"
        )

    checks = conn.execute(
        "SELECT pg_get_constraintdef(c.oid) AS definition, c.convalidated "
        "FROM pg_constraint c "
        "JOIN pg_class t ON t.oid=c.conrelid "
        "JOIN pg_namespace n ON n.oid=t.relnamespace "
        "WHERE n.nspname='public' AND t.relname=%s AND c.contype='c'",
        (TRACKING_TABLE,),
    ).fetchall()

    if len(checks) != 1 or not checks[0]["convalidated"]:
        raise MigrationStateError(
            "Migration tracking table must have exactly one validated status check"
        )

    definition = " ".join(
        (checks[0]["definition"] or "").lower().split()
    )

    expected_definition = (
        "check ((status = any (array["
        "'running'::text, 'applied'::text, 'failed'::text])))"
    )

    if definition != expected_definition:
        raise MigrationStateError(
            "Migration tracking status check is incompatible"
        )


def verify_integrity_migration_not_applied(conn) -> None:
    """Reject conflicts with the exact 35 constraints and 17 indexes in the migration."""
    constraint_names = list(EXPECTED_FOREIGN_KEYS)
    index_names = list(EXPECTED_INDEXES)

    existing_constraints = conn.execute(
        "SELECT c.conname, t.relname AS table_name "
        "FROM pg_constraint c "
        "JOIN pg_class t ON t.oid=c.conrelid "
        "JOIN pg_namespace n ON n.oid=t.relnamespace "
        "WHERE n.nspname='public' AND c.conname=ANY(%s)",
        (constraint_names,),
    ).fetchall()

    for row in existing_constraints:
        expected_table = EXPECTED_FOREIGN_KEYS[row["conname"]]
        raise MigrationStateError(
            f"Integrity migration constraint name already exists: "
            f"{row['conname']} on {row['table_name']} "
            f"(expected table: {expected_table})"
        )

    existing_indexes = conn.execute(
        "SELECT obj.relname, obj.relkind, tbl.relname AS table_name "
        "FROM pg_class obj "
        "JOIN pg_namespace n ON n.oid=obj.relnamespace "
        "LEFT JOIN pg_index i ON i.indexrelid=obj.oid "
        "LEFT JOIN pg_class tbl ON tbl.oid=i.indrelid "
        "WHERE n.nspname='public' AND obj.relname=ANY(%s)",
        (index_names,),
    ).fetchall()

    for row in existing_indexes:
        expected_table = EXPECTED_INDEXES[row["relname"]]
        raise MigrationStateError(
            f"Integrity migration index name already exists: "
            f"{row['relname']} (existing table: {row['table_name']}; "
            f"expected table: {expected_table})"
        )

def release_advisory_lock(conn) -> None:
    """Release the migration lock and report failures without hiding errors."""
    try:
        result = conn.execute(
            "SELECT pg_advisory_unlock(%s) AS unlocked",
            (ADVISORY_LOCK_KEY,),
        ).fetchone()

        if not result or result["unlocked"] is not True:
            raise MigrationStateError(
                "PostgreSQL did not confirm advisory lock release"
            )

        conn.commit()

    except Exception as unlock_error:
        try:
            conn.rollback()
        except Exception:
            pass

        print(
            "WARNING: Advisory lock release could not be confirmed "
            f"({type(unlock_error).__name__}). "
            "The lock will be released when the database session closes.",
            file=sys.stderr,
        )

def apply_migrations(
    conn,
    migrations: list[Migration],
    expected_project_id: str,
) -> list[str]:
    """Apply migrations with durable markers and a session-level advisory lock."""
    lock_acquired = False
    applied_now = []

    try:
        # psycopg starts a transaction automatically on the first statement.
        _establish_transaction_staging_identity(conn, expected_project_id)
        conn.commit()

        # Session-level lock survives commits and protects the whole run.
        conn.execute(
            "SELECT pg_advisory_lock(%s)",
            (ADVISORY_LOCK_KEY,),
        )
        conn.commit()
        lock_acquired = True

        conn.execute(f"""CREATE TABLE IF NOT EXISTS public.{TRACKING_TABLE} (
            migration_id TEXT PRIMARY KEY,
            sha256 CHAR(64) NOT NULL,
            status TEXT NOT NULL CHECK (status IN ('running','applied','failed')),
            started_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
            applied_at TIMESTAMPTZ,
            last_error_class TEXT
        )""")
        verify_tracking_table(conn)
        conn.commit()

        rows = conn.execute(
            f"SELECT migration_id, sha256, status, applied_at "
            f"FROM public.{TRACKING_TABLE} ORDER BY migration_id"
        ).fetchall()

        pending = classify_migration_state(migrations, rows)

        for migration in pending:
            if migration.migration_id.endswith(
                "_practice_quiz_xp_rewards"
            ):
                verify_existing_xp_ledger(conn)

            if migration.migration_id.endswith(
                "_integrity_constraints"
            ):
                verify_integrity_migration_not_applied(conn)

            # Commit a durable marker before attempting migration SQL.
            conn.execute(
                f"INSERT INTO public.{TRACKING_TABLE} "
                "(migration_id, sha256, status) "
                "VALUES (%s, %s, 'running')",
                (migration.migration_id, migration.sha256),
            )
            conn.commit()

            try:
                _establish_transaction_staging_identity(
                    conn, expected_project_id
                )
                conn.execute(migration.sql, prepare=False)
                conn.execute(
                    f"UPDATE public.{TRACKING_TABLE} "
                    "SET status='applied', applied_at=CURRENT_TIMESTAMP, "
                    "last_error_class=NULL WHERE migration_id=%s",
                    (migration.migration_id,),
                )
                conn.commit()
                applied_now.append(migration.migration_id)

            except Exception as exc:
                conn.rollback()

                try:
                    conn.execute(
                        f"UPDATE public.{TRACKING_TABLE} "
                        "SET status='failed', last_error_class=%s "
                        "WHERE migration_id=%s",
                        (type(exc).__name__, migration.migration_id),
                    )
                    conn.commit()
                except Exception:
                    conn.rollback()
                    raise MigrationStateError(
                        f"Migration {migration.migration_id} failed and "
                        "the failure marker could not be saved; manual "
                        "database inspection is required"
                    ) from None

                raise MigrationStateError(
                    f"Migration {migration.migration_id} failed "
                    f"({type(exc).__name__}); state is marked failed "
                    "and requires manual inspection"
                ) from None

        return applied_now

    finally:
        if lock_acquired:
            release_advisory_lock(conn)
            

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        "--plan",
        action="store_true",
        help="List required migration files without connecting to a database",
    )
    mode.add_argument(
        "--apply",
        action="store_true",
        help="Explicitly apply pending migrations to the confirmed staging project",
    )
    parser.add_argument("--expected-host")
    parser.add_argument("--expected-project-id")
    parser.add_argument("--confirm-staging-target", action="store_true")
    args = parser.parse_args(argv)

    directory = Path(__file__).resolve().parents[1] / "migrations"

    try:
        migrations = load_migrations(directory)

        if args.plan:
            for item in migrations:
                print(f"{item.migration_id} sha256={item.sha256}")
            return 0

        if os.getenv("CLASSCODE_ENVIRONMENT", "").strip().lower() != "staging":
            raise ValueError("CLASSCODE_ENVIRONMENT=staging is required")

        if not args.confirm_staging_target:
            raise ValueError("--confirm-staging-target is required")

        if not args.expected_host or not args.expected_project_id:
            raise ValueError(
                "--expected-host and --expected-project-id are required"
            )

        url = os.getenv("STAGING_DATABASE_URL", "").strip()
        validate_staging_url(
            url, args.expected_host, args.expected_project_id
        )

        sslrootcert = validate_staging_ca(
            os.getenv("STAGING_SSLROOTCERT", "")
        )

        import psycopg
        from psycopg.rows import dict_row

        with psycopg.connect(
            url,
            connect_timeout=10,
            sslmode="verify-full",
            sslrootcert=sslrootcert,
            row_factory=dict_row,
        ) as conn:
            applied = apply_migrations(
                conn, migrations, args.expected_project_id
            )

        print(
            "Applied migrations: "
            + (
                ", ".join(applied)
                if applied
                else "none; all are already applied"
            )
        )
        return 0

    except Exception as exc:
        print(
            f"Migration operation refused or failed "
            f"({type(exc).__name__}): {exc}",
            file=sys.stderr,
        )
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
