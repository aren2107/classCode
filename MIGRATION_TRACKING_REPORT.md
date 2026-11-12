# Migration Tracking Report — Step 3

The three previously missing historical SQL files were not recovered. Step 3 adds a **newly authored replacement set** based on the current Step 2 PostgreSQL source package. These replacements must not be described as historical originals.

Forward order:
1. `2026-11-01_practice_quiz_xp_rewards.sql`
2. `2026-11-01_integrity_constraints.sql`

`2026-11-01_integrity_constraints_rollback.sql` is excluded from forward execution. The runner hashes exact file bytes, checks stored hashes/status/timestamps, refuses unknown/changed/partial states, and wraps each forward migration plus its applied tracking update in one transaction. The integrity preflight is scoped to ClassCode tables parsed from `bot/postgres_schema.sql` so unrelated Supabase public objects do not cause false positives.

No database was connected and no migration was executed. PostgreSQL integration remains unverified.
