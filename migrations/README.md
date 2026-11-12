# ClassCode PostgreSQL migrations — Step 3 replacement set

**These are newly authored replacement migrations.** The original historical SQL files could not be recovered from the available source package or backup. Nothing in this directory is represented as recovered original SQL.

## Source basis

The replacements were designed from the Step 2 source files: `bot/postgres_schema.sql`, `bot/database.py`, `bot/cogs/quizzes.py`, `bot/learning/mastery.py`, `bot/learning/progress.py`, `SCHEMA_RELATIONSHIP_REPORT.md`, `XP_REWARD_POLICY.md`, `tools/migration_runner.py`, `MIGRATION_TRACKING_REPORT.md`, and this migration directory's prior README.

The older SQLite schema was not used as a PostgreSQL DDL source.

## Forward migration order

The runner explicitly allows only these forward migrations, in this order:

1. `2026-11-01_practice_quiz_xp_rewards.sql`
2. `2026-11-01_integrity_constraints.sql`
3. `2026-11-03_daily_submissions_manila_timezone.sql`

`2026-11-01_integrity_constraints_rollback.sql` is an operator-reviewed rollback script, never a forward migration.

The runner requires all declared source files to exist and rejects unexpected `.sql` files. Rollback scripts are excluded from forward execution.

Any new SQL migration must be explicitly reviewed and added to the forward allowlist.

## Execution environment, TLS, and identity limitations

The intended operator workflow requires:

- `CLASSCODE_ENVIRONMENT=staging`
- `STAGING_DATABASE_URL` pointing to an isolated Supabase staging project
- `STAGING_SSLROOTCERT` pointing to the trusted Supabase root CA certificate
- Exact `--expected-host`
- Exact `--expected-project-id`
- `--confirm-staging-target`

### Connection restrictions

The migration runner accepts only direct Supabase database hostnames matching:

`db.PROJECT_REF.supabase.co`

It checks that:

- The project reference is exactly 20 lowercase alphanumeric characters.
- The hostname contains the expected project reference.
- The supplied expected hostname matches that exact hostname.
- The certificate path is configured and points to an existing file.

Pooler hostnames and custom hostnames are rejected.

The migration connection uses:

- `sslmode=verify-full`
- `sslrootcert` from `STAGING_SSLROOTCERT`

This requires TLS certificate-chain and hostname verification. A missing certificate file causes the runner to refuse the connection.

The certificate must be obtained from an official Supabase source and its provenance must be verified before use. The existence of a file alone does not prove that it is an authentic or appropriate CA certificate.

Do not use an arbitrary certificate or disable certificate verification to work around connection errors.

The bot's normal `DATABASE_URL` remains separate. These settings apply only to the migration runner.

### Windows CMD environment setup

The migration runner does not automatically load `.env` or `.env.example`. Before invoking it, the operator must explicitly set the migration-only environment variables in the current CMD session.

Example using placeholders:

```cmd
set "CLASSCODE_ENVIRONMENT=staging"
set "STAGING_DATABASE_URL=postgresql://USER:PASSWORD@db.PROJECT_REF.supabase.co:5432/postgres"
set "STAGING_SSLROOTCERT=C:\path\to\supabase-ca.crt"
```

Replace the placeholders with the approved staging configuration. Do not paste real credentials into shared logs, screenshots, or support messages.

These variables remain available only in the current CMD session and its child processes. Closing the terminal clears them.

Setting these variables does not authorize a migration or establish independent proof of the target project's identity. Do not run `--apply` until the deployment blockers and approval requirements documented above have been resolved.

The `--plan` option can inspect the migration list without establishing a database connection.

### Project identity limitations

**IMPORTANT: The PostgreSQL project identity markers are NOT independent proof of the actual Supabase project.**

The runner sets transaction-local PostgreSQL settings:

- `classcode.environment`
- `classcode.project_id`

It then reads those settings back using `current_setting(...)`.

This confirms that the supplied values were set successfully. It does not independently establish the identity of the connected Supabase project.

The hostname check verifies the configured endpoint's project-reference format and its match with the operator-supplied expected project ID. TLS `verify-full` verifies the server certificate against the configured trusted CA and hostname.

These checks strengthen endpoint verification, but they are not an independent query of Supabase project metadata. DNS, endpoint configuration, certificate provenance, and the actual project association must still be reviewed.

The operating-system environment variable and command-line confirmations are also operator-supplied values. They do not independently authenticate the database project's identity.

**Deployment blocker:** Before any staging migration is approved, the complete endpoint and project identity verification procedure must be independently reviewed and documented. The trusted CA certificate's source must also be verified.

Do not treat the transaction-local markers alone as sufficient project identity protection.

The SQL migration environment guards provide an additional execution safeguard, but they also rely on PostgreSQL settings supplied by the runner. They do not independently identify the cloud project.

Do not connect this runner to Supabase or Neon while these review requirements remain unresolved.

## Migration transaction behavior

The runner uses a dedicated psycopg connection rather than an application connection pool.

It records a durable `running` marker before executing each migration. The migration SQL and its final tracking update execute in a transaction.

If execution fails, the transaction is rolled back and the tracking record is marked `failed`. A failed or interrupted migration requires manual inspection before another attempt.

The runner does not automatically retry a migration recorded as running or failed.

## XP reward migration

Creates an empty `public.practice_quiz_xp_rewards` ledger with:

- `user_id BIGINT NOT NULL`
- `language TEXT NOT NULL`
- `topic_id TEXT NOT NULL`
- `xp_awarded BIGINT NOT NULL`
- `recorded_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP`
- Primary key `(user_id, language, topic_id)`

It uses `CREATE TABLE IF NOT EXISTS` so the already-declared exact shape in `bot/postgres_schema.sql` is compatible.

The runner checks any pre-existing table's ordered columns, nullability, timestamp default, and composite primary key before proceeding.

No records are imported or seeded. Existing XP balances and history are untouched.

## Integrity migration design

Adds only the foreign-key relationships listed in `SCHEMA_RELATIONSHIP_REPORT.md`, using named constraints, `ON DELETE RESTRICT`, `NOT VALID`, and explicit validation.

It adds the documented query-supporting indexes from that report.

No `CHECK` constraints or `NOT NULL` alterations are added. The available application write paths do not consistently prove all proposed closed value domains/defaulted nullable columns safe across every feature, and no data preflight has been run.

The migration never repairs or deletes rows. Validation errors abort the transaction.

No challenge FK, portfolio uniqueness, certificate uniqueness, or cascading delete behavior is introduced.

## Daily challenge Manila timezone migration

The daily challenge uses `Asia/Manila` as its calendar timezone.

The application captures the Manila date when a submission starts. That same captured date is used for:

- Selecting the daily challenge
- Checking whether the student already earned the daily challenge reward
- Saving the submission timestamp
- Recording the XP reward date
- Updating the daily challenge goal

This ensures a submission that starts before Manila midnight remains assigned to that date even if code execution finishes after midnight.

The `daily_submissions.submitted_at` column remains `TIMESTAMP WITHOUT TIME ZONE`.

New application submissions explicitly store Manila-local wall-clock timestamps. The schema default and timezone migration also use:

`timezone('Asia/Manila', CURRENT_TIMESTAMP)`

Existing submission timestamps are deliberately not rewritten. Their original session timezone may be unknown, so converting historical values could produce incorrect dates. Legacy records near midnight may not be reliably reconstructible.

The migration changes the default for future database inserts. It does not modify existing submission rows.

## Rollback limits

The integrity rollback drops only the exact named foreign keys and indexes created by the integrity migration.

It does not change application rows, nullability, the XP ledger, XP balances, or XP history. It does not roll back the XP migration.

It is safe to consider only after confirming the integrity migration's objects and code dependencies. A coordinated code/schema rollback may be required if later application code depends on the constraints.

The rollback script uses PostgreSQL settings as execution guards. Those settings are operator-supplied markers, not independent proof of the connected Supabase project.

Do not execute a rollback against any cloud database until the actual project identity has been independently verified and the target has been explicitly approved.

The migration runner never automatically invokes rollback scripts.

## Verification status and safety boundary

A historical Step 4.1 PostgreSQL integration rehearsal was run against a disposable local PostgreSQL 18.6 database named `classcode_test`.

That earlier rehearsal covered the base schema and the two previously declared forward migrations. Its historical report recorded 49 passing tests.

**Those results do not verify the newly added Manila timezone migration or the current source changes.** Fresh local tests and a new review are required.

The current source changes have passed Python syntax checks for `bot/cogs/challenges.py` and `tools/migration_runner.py`. Local fake-hostname validation tests passed, and certificate-path rejection tests passed. These checks do not establish database integration correctness or the authenticity of a real Supabase server certificate.

This local history is not an isolated Supabase staging rehearsal.

No Supabase, Neon, HOKAS, staging, or production database connection is authorized by this documentation update.

No cloud migration, backup, restore, SQLite import, or deployment is authorized.

An isolated Supabase staging rehearsal, including data preflight and query-plan/index review, remains required before production approval. The independent project identity verification blocker must also be resolved first.

Supabase is the only primary runtime database. Neon is backup/recovery only. PostgreSQL is the only database technology.

