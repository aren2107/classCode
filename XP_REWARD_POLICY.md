# Practice Quiz XP Reward Policy

**Status:** Approved and implemented in source; not deployed and not applied to production data.

## Rule

- A student may practice without an attempt limit, and every finished attempt continues to be recorded.
- The 50 XP practice reward is issued only on the student's first passing attempt for a stable `(user_id, language, topic_id)` key. Current language IDs are `cpp` and `java`; topic IDs come from the curriculum. Display titles are not used in the key.
- Failing attempts issue no practice XP and do not consume eligibility.
- Lesson completion and mastery rewards remain unchanged. Existing XP and XP history are preserved; no prior reward is clawed back.

## Atomicity and migration

`practice_quiz_xp_rewards` uses `(user_id, language, topic_id)` as its primary key. A passing attempt inserts its claim with `ON CONFLICT DO NOTHING`; only the transaction that inserts the key calls the existing XP helper. The attempt, daily quiz count, claim, XP balance/history, and daily XP total commit or roll back together. The database uniqueness key arbitrates duplicate submissions from multiple processes.

The new Supabase deployment must start from an empty PostgreSQL project. The bot does not create the ledger or import historical records at startup; the reviewed PostgreSQL migration creates the ledger empty. No historical database records are imported.

For PostgreSQL staging rehearsal, run `migrations/2026-11-01_practice_quiz_xp_rewards.sql` only against an isolated staging database after setting `classcode.environment=staging`. It creates the empty ledger and is safe to rerun. Do not drop the ledger during rollback: it is the idempotency record. The old application version ignores it and would restore repeat rewards, so any code rollback must retain a version with the one-time guard or be followed by a forward fix.

The backup target schema must be updated to include this ledger before the next Supabase-to-Neon table-copy backup. Neon remains backup-only. Do not switch the bot runtime to Neon.

## Verification status

Offline unit and mocked tests must cover first/repeat pass, failures, concurrent submissions, stable identifiers, rollback atomicity, and unlimited attempt recording. Real PostgreSQL integration and staging migration results must be reported separately; mock tests are not a substitute.
