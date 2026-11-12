"""Read-only aggregate preflight for the proposed ClassCode integrity migration.

Use STAGING_DATABASE_URL, --expected-host, and --confirm-staging-target. The
script never prints the connection string or student row contents.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from urllib.parse import urlsplit


RELATIONSHIPS = (
    ("user_progress", "user_id", "users", "user_id"),
    ("quiz_attempts", "user_id", "users", "user_id"),
    ("practice_quiz_xp_rewards", "user_id", "users", "user_id"),
    ("user_badges", "user_id", "users", "user_id"),
    ("daily_submissions", "user_id", "users", "user_id"),
    ("xp_history", "user_id", "users", "user_id"),
    ("daily_goals", "user_id", "users", "user_id"),
    ("project_progress", "user_id", "users", "user_id"),
    ("project_progress", "project_id", "projects", "project_id"),
    ("classes", "teacher_id", "users", "user_id"),
    ("class_members", "class_id", "classes", "class_id"),
    ("class_members", "user_id", "users", "user_id"),
    ("assignments", "class_id", "classes", "class_id"),
    ("assignment_submissions", "assignment_id", "assignments", "assignment_id"),
    ("assignment_submissions", "user_id", "users", "user_id"),
    ("code_snippets", "user_id", "users", "user_id"),
    ("personal_notes", "user_id", "users", "user_id"),
    ("user_titles", "user_id", "users", "user_id"),
    ("user_stats", "user_id", "users", "user_id"),
    ("daily_missions", "user_id", "users", "user_id"),
    ("bug_attempts", "user_id", "users", "user_id"),
    ("bug_attempts", "puzzle_id", "bug_puzzles", "puzzle_id"),
    ("study_groups", "owner_id", "users", "user_id"),
    ("study_group_members", "group_id", "study_groups", "group_id"),
    ("study_group_members", "user_id", "users", "user_id"),
    ("pair_queue", "user_id", "users", "user_id"),
    ("event_progress", "user_id", "users", "user_id"),
    ("portfolio_projects", "user_id", "users", "user_id"),
    ("portfolio_projects", "project_id", "projects", "project_id"),
    ("certificates", "user_id", "users", "user_id"),
    ("practical_exams", "created_by", "users", "user_id"),
    ("practical_exam_submissions", "exam_id", "practical_exams", "exam_id"),
    ("practical_exam_submissions", "user_id", "users", "user_id"),
    ("attendance_records", "user_id", "users", "user_id"),
    ("lesson_mastery", "user_id", "users", "user_id"),
)

# (name, table, predicate). Predicates identify values the proposed CHECK or
# NOT NULL constraints reject. All output is aggregate counts only.
CHECKS = (
    ("users_xp_level_streak", "users", "xp IS NULL OR xp < 0 OR level IS NULL OR level < 1 OR streak_count IS NULL OR streak_count < 0"),
    ("user_progress_status", "user_progress", "status IS NULL OR status NOT IN ('locked','unlocked','review','completed')"),
    ("quiz_attempt_bounds", "quiz_attempts", "total IS NULL OR total <= 0 OR score < 0 OR score > total OR passed IS NULL OR passed NOT IN (0,1)"),
    ("daily_submission_values", "daily_submissions", "score IS NULL OR score < 0 OR status NOT IN ('passed','partial') OR language NOT IN ('cpp','java')"),
    ("xp_history_amount", "xp_history", "amount < 0"),
    ("daily_goal_counters", "daily_goals", "lessons IS NULL OR lessons < 0 OR quizzes IS NULL OR quizzes < 0 OR challenges IS NULL OR challenges < 0 OR xp_earned IS NULL OR xp_earned < 0"),
    ("project_xp", "projects", "xp IS NULL OR xp < 0"),
    ("project_progress_status", "project_progress", "status IS NULL OR status NOT IN ('available','completed')"),
    ("class_member_role", "class_members", "role IS NULL OR role NOT IN ('student','teacher')"),
    ("daily_mission_values", "daily_missions", "target IS NULL OR target <= 0 OR progress IS NULL OR progress < 0 OR reward IS NULL OR reward < 0"),
    ("user_stats_counters", "user_stats", "coding_runs IS NULL OR coding_runs < 0 OR bugs_fixed IS NULL OR bugs_fixed < 0 OR problems_solved IS NULL OR problems_solved < 0 OR projects_completed IS NULL OR projects_completed < 0 OR study_minutes IS NULL OR study_minutes < 0"),
    ("bug_attempt_values", "bug_attempts", "solved IS NULL OR solved NOT IN (0,1) OR attempts IS NULL OR attempts < 0"),
    ("event_points", "event_progress", "points IS NULL OR points < 0"),
    ("portfolio_featured", "portfolio_projects", "featured IS NULL OR featured NOT IN (0,1)"),
    ("exam_active", "practical_exams", "active IS NULL OR active NOT IN (0,1)"),
    ("exam_submission_values", "practical_exam_submissions", "score IS NULL OR score < 0 OR score > 100 OR passed_tests IS NULL OR passed_tests < 0 OR total_tests IS NULL OR total_tests < 0 OR passed_tests > total_tests OR status NOT IN ('pending_review','manual')"),
    ("mastery_values", "lesson_mastery", "best_score IS NULL OR best_score NOT BETWEEN 0 AND 5 OR last_score IS NULL OR last_score NOT BETWEEN 0 AND 5 OR attempts IS NULL OR attempts < 0 OR passed IS NULL OR passed NOT IN (0,1) OR xp_awarded IS NULL OR xp_awarded NOT IN (0,1) OR demonstration_completed IS NULL OR demonstration_completed NOT IN (0,1)"),
)

DUPLICATE_CANDIDATES = (
    ("portfolio_projects_user_project", "portfolio_projects", "user_id, project_id"),
    ("certificates_user_language", "certificates", "user_id, language"),
)


def _quote(identifier: str) -> str:
    if not re.fullmatch(r"[a-z_][a-z0-9_]*", identifier):
        raise ValueError("Unexpected SQL identifier")
    return '"' + identifier + '"'


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expected-host", required=True, help="Exact hostname copied from the isolated staging connection string")
    parser.add_argument("--confirm-staging-target", action="store_true", help="Acknowledge that STAGING_DATABASE_URL points to a disposable staging database")
    args = parser.parse_args(argv)
    dsn = os.getenv("STAGING_DATABASE_URL", "").strip()
    if not dsn:
        parser.error("Set STAGING_DATABASE_URL in the private environment; do not use production credentials")
    if not args.confirm_staging_target:
        parser.error("This read-only preflight still requires --confirm-staging-target")
    parsed = urlsplit(dsn)
    host = (parsed.hostname or "").lower()
    expected = args.expected_host.strip().lower()
    if not host or host != expected:
        parser.error("STAGING_DATABASE_URL hostname does not exactly match --expected-host")
    print(f"Read-only schema preflight target host: {host}")

    try:
        import psycopg
    except ImportError:
        print("Install requirements.txt to run this PostgreSQL preflight.", file=sys.stderr)
        return 2

    schema_path = os.path.join(os.path.dirname(__file__), "..", "bot", "postgres_schema.sql")
    schema = open(schema_path, encoding="utf-8").read()
    expected_tables = set(re.findall(r"(?i)CREATE\s+TABLE\s+IF\s+NOT\s+EXISTS\s+([a-z_][a-z0-9_]*)", schema))
    errors = 0
    try:
        with psycopg.connect(dsn, connect_timeout=10, sslmode="require") as conn:
            conn.execute("SET TRANSACTION READ ONLY")
            conn.execute("SET LOCAL statement_timeout = '30s'")
            actual_tables = {
                row[0] for row in conn.execute(
                    "SELECT table_name FROM information_schema.tables "
                    "WHERE table_schema='public' AND table_type='BASE TABLE'"
                ).fetchall()
            }
            missing = sorted(expected_tables - actual_tables)
            print(f"application_tables_expected={len(expected_tables)} missing={len(missing)}")
            for table in missing:
                print(f"BLOCK missing_table={table}")
                errors += 1

            for child, child_col, parent, parent_col in RELATIONSHIPS:
                if child not in actual_tables or parent not in actual_tables:
                    continue
                c, cc, p, pc = map(_quote, (child, child_col, parent, parent_col))
                null_count = conn.execute(f"SELECT count(*) FROM public.{c} WHERE {cc} IS NULL").fetchone()[0]
                orphan_count = conn.execute(
                    f"SELECT count(*) FROM public.{c} child WHERE child.{cc} IS NOT NULL "
                    f"AND NOT EXISTS (SELECT 1 FROM public.{p} parent WHERE parent.{pc}=child.{cc})"
                ).fetchone()[0]
                if null_count or orphan_count:
                    print(f"BLOCK relation={child}.{child_col}->{parent}.{parent_col} nulls={null_count} orphans={orphan_count}")
                    errors += 1

            for name, table, predicate in CHECKS:
                if table not in actual_tables:
                    continue
                t = _quote(table)
                count = conn.execute(f"SELECT count(*) FROM public.{t} WHERE {predicate}").fetchone()[0]
                if count:
                    print(f"BLOCK check={name} offending_rows={count}")
                    errors += 1

            for name, table, columns in DUPLICATE_CANDIDATES:
                if table not in actual_tables:
                    continue
                t = _quote(table)
                cols = ",".join(_quote(part.strip()) for part in columns.split(","))
                count = conn.execute(
                    f"SELECT count(*) FROM (SELECT 1 FROM public.{t} GROUP BY {cols} HAVING count(*) > 1) duplicates"
                ).fetchone()[0]
                print(f"INFO duplicate_candidate={name} duplicate_groups={count} (no unique constraint proposed)")
    except Exception as exc:
        print(f"Preflight failed ({type(exc).__name__}); no row values or connection string were logged.", file=sys.stderr)
        return 2

    if errors:
        print(f"Preflight BLOCKED: {errors} finding(s). No data was changed.")
        return 1
    print("Preflight PASS: proposed relationship/check values are clean. No data was changed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
