# ClassCode Hosting Setup

1. Set `DISCORD_TOKEN`, `GUILD_ID`, `GEMINI_API_KEY`, and `GEMINI_MODEL=gemini-3.8-flash` in the host variables.
2. Set `DATABASE_URL` to the Supabase PostgreSQL connection string. Supabase is the only application database. There is no local database mode, `DATABASE_PATH`, or fallback.
3. Configure `NEON_DATABASE_URL` only in the separate backup job environment. Use `python tools/apply_postgres_schema.py --target neon` once, then schedule `python tools/backup_supabase_to_neon.py --confirm-overwrite` after carefully verifying both connection strings.
4. `CODE_RUNNER_URL=https://ce.judge0.com` is suitable for initial testing, but do not assume the public endpoint is production-reliable. For practical exams, verify live execution from HOKAS or use a dedicated Judge0-compatible service.
5. Before bot startup, an operator must apply the approved base schema and tracked migrations to the intended Supabase project. The bot startup path only checks required tables; it never applies DDL.
6. Startup Command: `pip install -r requirements.txt && python -m bot`
7. Restart after changing environment variables.

## Discord role security

- The ClassCode `Admin` role is a label only. ClassCode administrative actions require the member's actual Discord Administrator permission.
- Review any pre-existing `Admin` role before launch. Remove its Discord `Administrator` permission unless you intentionally want it to grant full server control, and remove it from non-administrators.
- `/setup` refreshes ClassCode channel overwrites so only Discord administrators can access the restricted admin category.

## Pre-launch integrity checks
- `/event-points` is staff-only; students cannot award themselves event points.
- Re-running `/setup` refreshes the verification and questionnaire panels instead of creating duplicates.
- The final ZIP must not contain database snapshots, `.env` files, credentials, `__pycache__`, `.pyc`, or test caches.
