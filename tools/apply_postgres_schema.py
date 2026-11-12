"""Apply the base PostgreSQL schema to an explicitly marked staging database only."""
from __future__ import annotations
import argparse
import os
from pathlib import Path
from urllib.parse import urlsplit


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", choices=("supabase", "neon"), required=True)
    parser.add_argument("--expected-host", required=True)
    parser.add_argument("--expected-project-id", required=True)
    parser.add_argument("--confirm-staging-target", action="store_true")
    args = parser.parse_args()
    if os.getenv("CLASSCODE_ENVIRONMENT", "").strip().lower() != "staging":
        parser.error("CLASSCODE_ENVIRONMENT=staging is required")
    if not args.confirm_staging_target:
        parser.error("--confirm-staging-target is required")
    env_name = "DATABASE_URL" if args.target == "supabase" else "NEON_DATABASE_URL"
    url = os.getenv(env_name, "").strip()
    if not url:
        parser.error(f"{env_name} must be set in the private operator environment")
    parsed = urlsplit(url)
    host = (parsed.hostname or "").lower()
    if parsed.scheme not in {"postgres", "postgresql"} or not host:
        parser.error(f"{env_name} must be a PostgreSQL connection URL")
    valid_host = host.endswith((".supabase.com", ".supabase.co")) if args.target == "supabase" else host.endswith(".neon.tech")
    if not valid_host or host != args.expected_host.strip().lower():
        parser.error(f"{env_name} does not match the explicitly confirmed {args.target} staging host")
    try:
        import psycopg
    except ImportError:
        parser.error("Install requirements.txt first (includes psycopg[binary])")
    schema_path = Path(__file__).resolve().parents[1] / "bot" / "postgres_schema.sql"
    statements = [statement.strip() for statement in schema_path.read_text(encoding="utf-8").split(";") if statement.strip()]
    statements += [
        "ALTER TABLE practical_exams ADD COLUMN IF NOT EXISTS exam_channel_id BIGINT",
        "ALTER TABLE practical_exams ADD COLUMN IF NOT EXISTS message_id BIGINT",
        "ALTER TABLE quiz_attempts ADD COLUMN IF NOT EXISTS total BIGINT DEFAULT 1",
        "ALTER TABLE lesson_mastery ADD COLUMN IF NOT EXISTS last_score BIGINT DEFAULT 0",
        "ALTER TABLE lesson_mastery ADD COLUMN IF NOT EXISTS weak_categories TEXT DEFAULT ''",
        "ALTER TABLE lesson_mastery ADD COLUMN IF NOT EXISTS review_due_at TIMESTAMP",
        "ALTER TABLE lesson_mastery ADD COLUMN IF NOT EXISTS demonstration_completed BIGINT DEFAULT 0",
    ]
    try:
        with psycopg.connect(url, connect_timeout=10, sslmode="require") as conn:
            with conn.transaction():
                conn.execute("SELECT set_config('classcode.environment', %s, true)", ("staging",))
                conn.execute("SELECT set_config('classcode.project_id', %s, true)", (args.expected_project_id,))
                identity = conn.execute(
                    "SELECT current_setting('classcode.environment', true), current_setting('classcode.project_id', true)"
                ).fetchone()
                if (identity[0] or "").strip().lower() != "staging" or (identity[1] or "").strip() != args.expected_project_id:
                    raise ValueError("Transaction-local staging identity does not match the explicit confirmation")
                for statement in statements:
                    conn.execute(statement, prepare=False)
    except Exception as exc:
        print(f"Schema operation refused or failed ({type(exc).__name__}); no connection details were logged.")
        return 2
    print(f"Base schema applied to the explicitly identified {args.target} staging database.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
