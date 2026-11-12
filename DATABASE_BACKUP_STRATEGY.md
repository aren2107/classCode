# ClassCode Database Backup Strategy

**Authority:** Supabase remains the primary. Neon remains backup-only. HOKAS remains the bot host. This guide does not change runtime database configuration or replace the current backup job.

## Current row-copy backup

`tools/backup_supabase_to_neon.py` reads the 32 PostgreSQL application tables named in `bot/postgres_schema.sql` inside one repeatable-read, read-only source transaction. It does not open or copy SQLite files. It copies rows into a pre-created, column-compatible Neon schema in one target transaction, verifies each copied row count, and restores identity/serial sequence positions. A failed target transaction rolls back and preserves the previous target contents. The success status marker is written only after the database commits and row-count checks pass; it records the source and target hostnames for later restore provenance checks. A new confirmed attempt invalidates the prior marker before it starts database I/O, so a failed or interrupted run cannot leave an old success marked current.

The `practice_quiz_xp_rewards` ledger is included in the schema-driven backup table list. Before the next backup after this change, update the Neon backup schema from the reviewed application schema so the destination contains this table. Neon remains backup-only and is not configured as the bot's runtime database.

This is a ClassCode **application-table snapshot**, not a complete PostgreSQL backup. It does not copy table/schema definitions, PK/FK/check constraints, indexes, views, functions, triggers, extensions, ACLs, role definitions, database settings, Supabase Auth/Storage/Realtime configuration, or project secrets. The target schema must be applied separately. The script currently has no test against live Supabase/Neon.

## Full logical backup option to test separately

For Supabase-to-Supabase portability, use the Supabase CLI's filtered PostgreSQL dump workflow, keeping separate private files for roles, schema, and data. The CLI wraps `pg_dump` with Supabase-specific filtering; do not replace it with an unfiltered dump until the output has been reviewed for platform-managed objects and permission errors. In a private operator shell, use environment variables so credentials are not written into repository files or committed scripts:

```powershell
$env:SOURCE_DB_URL = '<source Supabase connection string>'
$backupDir = '<private encrypted backup directory>'
New-Item -ItemType Directory -Force -Path $backupDir | Out-Null
supabase db dump --db-url $env:SOURCE_DB_URL -f "$backupDir\roles.sql" --role-only
supabase db dump --db-url $env:SOURCE_DB_URL -f "$backupDir\schema.sql"
supabase db dump --db-url $env:SOURCE_DB_URL -f "$backupDir\data.sql" --use-copy --data-only
Get-FileHash "$backupDir\roles.sql","$backupDir\schema.sql","$backupDir\data.sql" -Algorithm SHA256
```

Use the provider's dedicated full-project backup/PITR as the strongest same-platform recovery layer when available. For a portable single-database archive, PostgreSQL `pg_dump -Fc` plus `pg_restore` captures schema and data objects such as tables, constraints, indexes, views, triggers, functions, and sequence state in a compressed archive. `pg_dump` does not define cluster-global roles; role/ACL restoration and provider-managed schemas need separate treatment. The Supabase CLI route documents separate role/schema/data dumps and warns that customizations to managed `auth`/`storage` schemas may need separate migration capture. Extensions must exist and be compatible on the destination. Supabase-managed settings, project secrets, Auth configuration, API settings, network rules, and publication configuration require provider-level inventory and manual recreation.

The `pg_dump` archive format is more complete than the current row-copy script for database objects and supports archive inspection/selection during restore. A full dump still does not clone the Supabase project control plane, secrets, network settings, or managed service configuration. Keep the application-table copy as a second independent recovery path until a full dump has passed a new-project rehearsal and is covered by an operator-owned schedule and retention policy.

## Isolated Supabase staging restore rehearsal

Never use the production host for these commands. The rehearsal requires a newly created, isolated Supabase project with no student data, a separate private backup directory, Supabase CLI/Docker or compatible PostgreSQL client tools, and credentials for the staging project. Do not place connection strings in source control or command output.

1. Create a disposable staging Supabase project in the intended region. Disable production integrations and keep only a separate staging Discord bot/application if a bot smoke is needed.
2. Copy the exact production, Neon, and staging hostnames from their dashboards. Verify that staging host differs from both production Supabase and Neon. Verify both URLs with a read-only `SELECT current_database(), current_user, inet_server_addr()` before any restore. Do not infer the host from a project label.
3. Pause ClassCode writes during separate CLI schema/data dumps, or use a provider snapshot/PITR point that supplies a single consistent recovery point. Do not assume three separately invoked CLI dumps share one source snapshot. During the same write pause, capture a read-only source inventory to a private path outside the repository:

   ```powershell
   $env:VERIFY_DATABASE_URL = $env:SOURCE_DB_URL
   python tools/verify_staging_restore.py capture --expected-host '<exact-source-staging-supabase-host>' --expected-project-id '<source-staging-project-id>' --manifest '<private encrypted directory>\source-manifest.json' --confirm-source-capture
   ```

   The manifest contains aggregate row counts and object definitions/hashes, never row contents or credentials. Protect it as private operational metadata.
4. Inspect dump warnings and roles/schema SQL. Redact any credentials before retaining logs. Compare extensions, custom schemas, roles, grants, RLS policies, triggers, functions, views, publications, database settings, and schema versions against the new staging project's supported configuration.
5. Restore only to the new staging host using the Supabase documented `psql --single-transaction --set ON_ERROR_STOP=1` procedure. Keep the destination URL in a private environment variable. Do not add `--clean`, `--create`, or point to a production host. If an object already exists because Supabase pre-provisioned it, stop and review instead of blindly ignoring errors.
6. Verify the restored public database against the source manifest using read-only staging access:

   ```powershell
   $env:VERIFY_DATABASE_URL = $env:STAGING_DB_URL
   python tools/verify_staging_restore.py verify --expected-host '<exact-restore-target-staging-host>' --expected-project-id '<restore-target-project-id>' --source-host '<exact-source-staging-host>' --source-project-id '<source-staging-project-id>' --manifest '<private encrypted directory>\source-manifest.json' --confirm-staging-target
   ```

   The tool compares public table counts, relation definitions, constraints, index definitions, view/routine hashes, triggers, RLS policies, table grants, role attributes/memberships, database settings, extensions, sequence states, and representative ClassCode join queries. If anything differs, stop and reconcile it; do not switch HOKAS. Use aggregate counts and synthetic test accounts; do not publish student row content.
7. For app-level smoke, configure a separate HOKAS test process or local bot with `DATABASE_URL` set only to staging, a test Discord token/server, and non-production external API credentials. Confirm bot startup performs only a read-only schema check, then run read-only profile/progress queries and a synthetic write/read/rollback using a disposable test account. Confirm Supabase is still the configured primary and Neon is not used by runtime code. Never put a production bot token or production URL into this test process.
8. Record failures, remove the staging project only after preserving the report needed for review, and keep the source backup intact. Rehearse again after schema changes.

## Current guarded row-copy restore requirements

The updated `tools/restore_neon_to_supabase.py` is staging-only. Both the Neon restore source and Supabase restore destination must expose database-level custom settings `classcode.environment=staging` and distinct `classcode.project_id` values. The command requires exact source and destination hostnames/project IDs, `--confirm-staging-target`, `--confirm-overwrite`, and a pre-restore success marker generated by backing up the destination Supabase staging database to a **different Neon endpoint/branch**. The marker must be stored outside the repository and contain verified row counts for all ClassCode tables. Old markers without source/target host provenance are rejected. The restore has not been run against any real database.

The base schema tool now also requires an explicitly marked staging database. Bot startup does not create schema or run migrations; it only checks required tables. The migration runner is separate and remains blocked until all authoritative migration SQL files are recovered.

## Required manual configuration

- Select and verify a provider backup/PITR plan and the actual retention window.
- Install compatible PostgreSQL client tools and Supabase CLI/Docker in a private operator environment.
- Create the isolated staging Supabase project, isolated Discord test application/server, and separate test API credentials.
- Configure private encrypted backup storage, scheduler, retention copies, log retention, and alerts on job failure/staleness.
- Inventory and re-create required extensions, roles/passwords, grants, RLS policies, API exposure, Auth/Storage configuration, network restrictions, project secrets, and Realtime publications.
- Do not grant the bot production owner/superuser privileges. The actual current runtime role and privileges have not been inspected.

## Comparison

| Property | Current row-copy to Neon | Full PostgreSQL/Supabase dump |
|---|---|---|
| ClassCode table rows | Yes, 32 schema-listed tables | Yes, subject to CLI filtering and dump permissions |
| Consistent data snapshot | Yes, repeatable-read source transaction | A single `pg_dump` archive is snapshot-consistent; separate Supabase CLI role/schema/data commands need writes paused or a provider snapshot |
| Constraints and indexes | No; requires pre-applied target schema | Included in schema dump/archive where permissions and CLI filtering allow |
| Views, triggers, functions | No | Included in database schema dump, except filtered/managed objects requiring separate capture |
| Sequences | Resets target and sets serial/identity from copied maxima | Sequence state is included in PostgreSQL data dump |
| Roles/ACLs | No | Role definitions require separate role/global dump; credentials and managed roles require manual handling |
| Provider project settings | No | No; configure separately or use provider-native restore/clone where supported |
| Current verification | Mock tests only; no live DB run | Not installed or tested in this environment |

**Decision:** Keep the current row-copy as the existing Neon secondary until a full-dump workflow is rehearsed on isolated staging, object/role/config gaps are understood, and replacement/dual-run is explicitly reviewed. No production backup or restore was run in this audit.

Reference procedures: [PostgreSQL `pg_dump` documentation](https://www.postgresql.org/docs/current/app-pgdump.html) describes custom archives, sequence data, and object sections; [Supabase's CLI backup/restore guide](https://supabase.com/docs/guides/platform/migrating-within-supabase/backup-restore) documents separate role, schema, and data dumps and managed-schema caveats.
