"""Capture/compare a private logical-database manifest and run read-only smoke queries.

The connection string is read only from VERIFY_DATABASE_URL and is never stored
in the manifest or printed. See DATABASE_BACKUP_STRATEGY.md before use.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import sys
from urllib.parse import urlsplit


def _digest(value: str | None) -> str | None:
    if value is None:
        return None
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _practice_quiz_reward_integrity(conn) -> dict[str, int]:
    """Return aggregate-only checks linking reward claims, attempts, and XP history."""
    passed = "LOWER(CAST(q.passed AS TEXT)) IN ('1','true','t')"
    checks = {
        "invalid_reward_amounts": (
            "SELECT count(*) FROM practice_quiz_xp_rewards WHERE xp_awarded <> 50"
        ),
        "reward_without_passed_attempt": (
            "SELECT count(*) FROM practice_quiz_xp_rewards r WHERE NOT EXISTS ("
            "SELECT 1 FROM quiz_attempts q WHERE q.user_id=r.user_id AND q.language=r.language "
            "AND q.topic_id=r.topic_id AND q.difficulty='lesson-practice' AND " + passed + ")"
        ),
        "passed_topic_without_reward": (
            "SELECT count(*) FROM (SELECT DISTINCT q.user_id,q.language,q.topic_id "
            "FROM quiz_attempts q WHERE q.difficulty='lesson-practice' AND " + passed + ") q "
            "WHERE NOT EXISTS (SELECT 1 FROM practice_quiz_xp_rewards r WHERE "
            "r.user_id=q.user_id AND r.language=q.language AND r.topic_id=q.topic_id)"
        ),
        "reward_history_mismatch": (
            "SELECT count(*) FROM practice_quiz_xp_rewards r WHERE "
            "(SELECT count(*) FROM xp_history h WHERE h.user_id=r.user_id AND h.amount >= 50 "
            "AND h.reason = ('Passed ' || upper(r.language) || ' lesson practice quiz [' "
            "|| r.language || ':' || r.topic_id || ']')) <> 1"
        ),
        "duplicate_reward_keys": (
            "SELECT count(*) FROM (SELECT user_id,language,topic_id FROM practice_quiz_xp_rewards "
            "GROUP BY user_id,language,topic_id HAVING count(*) > 1) duplicate_keys"
        ),
    }
    return {name: conn.execute(query).fetchone()[0] for name, query in checks.items()}


def database_manifest(conn) -> dict:
    server_version = int(conn.execute("SHOW server_version_num").fetchone()[0])
    table_rows = {}
    tables = conn.execute(
        "SELECT tablename FROM pg_tables WHERE schemaname='public' ORDER BY tablename"
    ).fetchall()
    for (table,) in tables:
        # Names come from PostgreSQL catalog metadata, then are identifier-quoted.
        quoted = '"' + table.replace('"', '""') + '"'
        table_rows[table] = conn.execute(f"SELECT count(*) FROM public.{quoted}").fetchone()[0]

    relations = conn.execute(
        "SELECT c.relname,c.relkind FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace "
        "WHERE n.nspname='public' AND c.relkind IN ('r','p','v','m','S','f') ORDER BY c.relkind,c.relname"
    ).fetchall()
    constraints = conn.execute(
        "SELECT t.relname,c.conname,c.contype,c.convalidated,pg_get_constraintdef(c.oid,true) "
        "FROM pg_constraint c JOIN pg_class t ON t.oid=c.conrelid JOIN pg_namespace n ON n.oid=t.relnamespace "
        "WHERE n.nspname='public' ORDER BY t.relname,c.conname"
    ).fetchall()
    indexes = conn.execute(
        "SELECT tablename,indexname,indexdef FROM pg_indexes WHERE schemaname='public' ORDER BY tablename,indexname"
    ).fetchall()
    views = conn.execute(
        "SELECT c.relname,c.relkind,pg_get_viewdef(c.oid,true) FROM pg_class c "
        "JOIN pg_namespace n ON n.oid=c.relnamespace WHERE n.nspname='public' AND c.relkind IN ('v','m') "
        "ORDER BY c.relkind,c.relname"
    ).fetchall()
    routines = conn.execute(
        "SELECT p.proname,pg_get_function_identity_arguments(p.oid),p.prokind,"
        "md5(pg_get_functiondef(p.oid)) FROM pg_proc p JOIN pg_namespace n ON n.oid=p.pronamespace "
        "WHERE n.nspname='public' AND p.prokind IN ('f','p') ORDER BY p.proname,2"
    ).fetchall()
    triggers = conn.execute(
        "SELECT t.relname,g.tgname,pg_get_triggerdef(g.oid,true) FROM pg_trigger g "
        "JOIN pg_class t ON t.oid=g.tgrelid JOIN pg_namespace n ON n.oid=t.relnamespace "
        "WHERE n.nspname='public' AND NOT g.tgisinternal ORDER BY t.relname,g.tgname"
    ).fetchall()
    policies = conn.execute(
        "SELECT schemaname,tablename,policyname,roles,cmd,qual,with_check FROM pg_policies "
        "WHERE schemaname='public' ORDER BY schemaname,tablename,policyname"
    ).fetchall()
    extensions = conn.execute(
        "SELECT extname,extversion FROM pg_extension ORDER BY extname"
    ).fetchall()
    roles = conn.execute(
        "SELECT rolname,rolsuper,rolinherit,rolcreaterole,rolcreatedb,rolcanlogin,rolreplication,rolbypassrls "
        "FROM pg_roles WHERE rolname !~ '^pg_' ORDER BY rolname"
    ).fetchall()
    role_memberships = conn.execute(
        "SELECT member.rolname,granted.rolname,m.admin_option FROM pg_auth_members m "
        "JOIN pg_roles member ON member.oid=m.member JOIN pg_roles granted ON granted.oid=m.roleid "
        "WHERE member.rolname !~ '^pg_' AND granted.rolname !~ '^pg_' ORDER BY member.rolname,granted.rolname"
    ).fetchall()
    database_config = conn.execute(
        "SELECT d.datname,owner.rolname,d.encoding,d.datcollate,d.datctype,d.datconnlimit,d.datallowconn "
        "FROM pg_database d JOIN pg_roles owner ON owner.oid=d.datdba "
        "WHERE d.datname=current_database()"
    ).fetchall()
    role_database_settings = conn.execute(
        "SELECT COALESCE(r.rolname,''),COALESCE(d.datname,''),s.setconfig "
        "FROM pg_db_role_setting s LEFT JOIN pg_roles r ON r.oid=s.setrole "
        "LEFT JOIN pg_database d ON d.oid=s.setdatabase ORDER BY 1,2"
    ).fetchall()
    grants = conn.execute(
        "SELECT table_schema,table_name,grantee,privilege_type,is_grantable "
        "FROM information_schema.table_privileges WHERE table_schema='public' "
        "ORDER BY table_schema,table_name,grantee,privilege_type"
    ).fetchall()
    sequences = conn.execute(
        "SELECT schemaname,sequencename,last_value FROM pg_sequences "
        "WHERE schemaname='public' ORDER BY schemaname,sequencename"
    ).fetchall()

    smoke_queries = {
        "users": "SELECT count(*) FROM users",
        "progress_join": "SELECT count(*) FROM user_progress p JOIN users u ON u.user_id=p.user_id",
        "xp_history_join": "SELECT count(*) FROM xp_history x JOIN users u ON u.user_id=x.user_id",
        "notes_owner_query": "SELECT count(*) FROM personal_notes n JOIN users u ON u.user_id=n.user_id",
        "attendance_owner_query": "SELECT count(*) FROM attendance_records a JOIN users u ON u.user_id=a.user_id",
        "class_assignment_query": "SELECT count(*) FROM assignments a JOIN classes c ON c.class_id=a.class_id",
        "portfolio_project_query": "SELECT count(*) FROM portfolio_projects p JOIN projects pr ON pr.project_id=p.project_id",
        "exam_submission_query": "SELECT count(*) FROM practical_exam_submissions s JOIN practical_exams e ON e.exam_id=s.exam_id",
        "mastery_owner_query": "SELECT count(*) FROM lesson_mastery m JOIN users u ON u.user_id=m.user_id",
    }
    smoke = {name: conn.execute(query).fetchone()[0] for name, query in smoke_queries.items()}
    practice_reward_integrity = _practice_quiz_reward_integrity(conn)
    return {
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "server_major": server_version // 10000,
        "public_table_rows": table_rows,
        "public_relations": [list(row) for row in relations],
        "public_constraints": [list(row) for row in constraints],
        "public_indexes": [list(row) for row in indexes],
        "public_view_definition_sha256": [[r[0], r[1], _digest(r[2])] for r in views],
        "public_routine_definition_md5": [list(row) for row in routines],
        "public_triggers": [list(row) for row in triggers],
        "public_rls_policies": [list(row) for row in policies],
        "extensions": [list(row) for row in extensions],
        "roles": [list(row) for row in roles],
        "role_memberships": [list(row) for row in role_memberships],
        "database_config": [list(row) for row in database_config],
        "role_database_settings": [list(row) for row in role_database_settings],
        "public_table_grants": [list(row) for row in grants],
        "public_sequences": [list(row) for row in sequences],
        "representative_query_counts": smoke,
        "practice_quiz_reward_integrity": practice_reward_integrity,
    }


def _database_url(args) -> tuple[str, str]:
    dsn = os.getenv("VERIFY_DATABASE_URL", "").strip()
    if not dsn:
        raise ValueError("Set VERIFY_DATABASE_URL in the private operator environment")
    parsed = urlsplit(dsn)
    host = (parsed.hostname or "").lower()
    if parsed.scheme not in {"postgres", "postgresql"} or not host:
        raise ValueError("VERIFY_DATABASE_URL must be a PostgreSQL connection URL")
    if host != args.expected_host.strip().lower():
        raise ValueError("VERIFY_DATABASE_URL hostname does not match --expected-host")
    if not (host.endswith(".supabase.co") or host.endswith(".supabase.com")):
        raise ValueError("Verification is restricted to a Supabase staging project")
    if not args.expected_project_id:
        raise ValueError("--expected-project-id is required")
    if os.getenv("CLASSCODE_ENVIRONMENT", "").strip().lower() != "staging":
        raise ValueError("CLASSCODE_ENVIRONMENT=staging is required; this does not configure PostgreSQL session settings")
    if args.mode == "verify":
        if not args.source_host or not args.source_project_id:
            raise ValueError("verify mode requires --source-host and --source-project-id")
        if host == args.source_host.strip().lower() or args.expected_project_id == args.source_project_id:
            raise ValueError("Verification destination must be a distinct staging project")
        if not args.confirm_staging_target:
            raise ValueError("Verify requires --confirm-staging-target")
    elif not args.confirm_source_capture:
        raise ValueError("Capture requires --confirm-source-capture")
    return dsn, host


def _verify_staging_identity(conn, expected_project_id: str) -> None:
    # Caller must be inside a transaction. true = transaction-local; no pool leakage.
    conn.execute("SELECT set_config('classcode.environment', %s, true)", ("staging",))
    conn.execute("SELECT set_config('classcode.project_id', %s, true)", (expected_project_id,))
    row = conn.execute(
        "SELECT current_setting('classcode.environment', true) AS environment, "
        "current_setting('classcode.project_id', true) AS project_id"
    ).fetchone()
    if (row[0] or "").strip().lower() != "staging":
        raise ValueError("Database environment marker is missing or is not staging")
    if (row[1] or "").strip() != expected_project_id:
        raise ValueError("Database project identity marker does not match --expected-project-id")


def _manifest_path(path_value: str) -> Path:
    path = Path(path_value).expanduser().resolve()
    project_root = Path(__file__).resolve().parents[1]
    if path == project_root or project_root in path.parents:
        raise ValueError("Keep database manifests outside the project/release directory")
    return path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("capture", "verify"))
    parser.add_argument("--expected-host", required=True)
    parser.add_argument("--manifest", required=True, help="Private manifest path outside the repository")
    parser.add_argument("--source-host", help="Required for verify mode; exact source Supabase hostname")
    parser.add_argument("--expected-project-id", required=True, help="Database-level classcode.project_id marker")
    parser.add_argument("--source-project-id", help="Required for verify mode; source staging project marker")
    parser.add_argument("--confirm-source-capture", action="store_true")
    parser.add_argument("--confirm-staging-target", action="store_true")
    args = parser.parse_args(argv)
    if args.mode == "verify" and not args.source_host:
        parser.error("verify mode requires --source-host")
    try:
        path = _manifest_path(args.manifest)
        dsn, host = _database_url(args)
        import psycopg
        print(f"Read-only database verification host: {host}")
        with psycopg.connect(dsn, connect_timeout=10, sslmode="require") as conn:
            conn.execute("SET TRANSACTION READ ONLY")
            conn.execute("SET LOCAL statement_timeout = '60s'")
            _verify_staging_identity(conn, args.expected_project_id)
            actual = database_manifest(conn)

        if args.mode == "capture":
            manifest = {"source_host": host, "source_project_id": args.expected_project_id, "database_manifest": actual}
            path.parent.mkdir(parents=True, exist_ok=True)
            temp = path.with_suffix(path.suffix + ".tmp")
            temp.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            os.replace(temp, path)
            print(f"Private source manifest captured: {path}")
            print(f"public_tables={len(actual['public_table_rows'])} representative_queries={len(actual['representative_query_counts'])}")
            return 0

        expected = json.loads(path.read_text(encoding="utf-8"))
        if expected.get("source_host", "").lower() != args.source_host.strip().lower():
            raise ValueError("Manifest source hostname does not match --source-host")
        if expected.get("source_project_id") != args.source_project_id:
            raise ValueError("Manifest source project identity does not match --source-project-id")
        expected_db = expected["database_manifest"]
        differences = []
        for key in sorted(set(expected_db) - {"captured_at"} | set(actual) - {"captured_at"}):
            if expected_db.get(key) != actual.get(key):
                differences.append(key)
        if differences:
            print("Restore verification mismatch categories: " + ", ".join(differences), file=sys.stderr)
            return 1
        reward_checks = actual["practice_quiz_reward_integrity"]
        failed_reward_checks = {name: count for name, count in reward_checks.items() if count}
        if failed_reward_checks:
            print("Practice reward ledger integrity check failed: " + ", ".join(
                f"{name}={count}" for name, count in sorted(failed_reward_checks.items())
            ), file=sys.stderr)
            return 1
        print("PASS: staging database matches the private source manifest for captured objects and row counts.")
        print(f"public_tables={len(actual['public_table_rows'])} representative_queries={len(actual['representative_query_counts'])}")
        return 0
    except Exception as exc:
        print(f"Verification failed ({type(exc).__name__}); no connection string was logged.", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
