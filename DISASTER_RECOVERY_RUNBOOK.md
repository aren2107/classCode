# ClassCode Database Recovery Runbook

**Status:** Designed on 2026-11-01; not rehearsed against PostgreSQL or production.

## Data authority

- Supabase is the live primary database.
- Neon is an off-site copy only. Never point the running bot at Neon during an outage.
- The new Supabase deployment starts with an empty PostgreSQL project. Do not migrate old SQLite accounts, XP, attempts, attendance, progress, projects, tickets, or any other records. Keep the existing SQLite database and its backup files offline and unchanged. Neon receives snapshots only from the new Supabase primary.
- The repository has Supabase-to-Neon snapshot and guarded Neon-to-Supabase restore tools. A restore must first be rehearsed against an empty staging Supabase project. Do not overwrite the live project during a rehearsal.
- The Neon utility copies ClassCode table rows and sequence state; it is not a full PostgreSQL project backup. For full-dump object coverage and a staging restore checklist, use `DATABASE_BACKUP_STRATEGY.md`.

## Recovery targets

No measured RPO or RTO is available. The Neon-copy RPO cannot be better than the scheduled backup interval plus the time needed to complete and verify a backup. The Supabase RPO/RTO depends on the project's plan, enabled backup or point-in-time recovery features, project size, and recovery choice. Set and document actual targets after choosing a backup schedule and completing a restore rehearsal.

## 1. Supabase has a temporary outage

1. Keep `DATABASE_URL` pointed at Supabase. Do not set it to Neon.
2. Do not tell students that a progress, XP, attendance, assignment, or exam change succeeded unless the bot confirms it after the database commit.
3. Check HOKAS logs for database connection errors and check Supabase status from its dashboard.
4. When Supabase recovers, retry the student's action only after checking its stored result if the first response was ambiguous.
5. Confirm the bot reconnects and that a small, non-destructive read works. Do not run schema or data repair commands during the outage.

## 2. Supabase data was deleted or corrupted

1. Stop the bot so it cannot add new writes to the damaged primary.
2. Preserve the current Supabase project and the latest Neon snapshot. Do not truncate or restore over either one while investigating.
3. Restore a Supabase provider backup or point-in-time snapshot to a **new project** when available. For a Neon recovery, first apply the reviewed base schema to that explicitly marked staging project, verify a separate pre-restore snapshot of the destination, and use the restore tool only with independent source/destination project identity markers plus both staging and overwrite confirmations. Never run the restore against the damaged/live project during rehearsal.
4. Compare ClassCode table row counts, inspect representative progress/XP/attendance records, verify ID sequences, and run the application's read-only validation against staging.
5. After an operator reviews and authorizes the recovery, point HOKAS `DATABASE_URL` at the recovered Supabase project and restart the bot.
6. Keep the damaged project read-only for investigation until the recovered service is confirmed.

Supabase documents daily backups for eligible paid plans and point-in-time recovery as a plan/add-on feature. Confirm the actual project plan and recovery window in the dashboard; do not assume a backup cadence or retention period. See [Supabase database backups](https://supabase.com/docs/guides/platform/backups).

## 3. A migration damaged the schema

1. Stop the bot to prevent writes. Bot startup no longer applies schema changes or migrations.
2. Identify the exact migration and the last known-good backup point.
3. Prefer restoring to a new Supabase project from a provider backup/PITR snapshot. Rehearse any Neon-based restore in staging first.
4. Verify schema columns, row counts, ID sequences, and key learning records before switching HOKAS.
5. Do not re-run the bot until the migration is corrected or the database is recovered.

The bot startup path is read-only with respect to schema: it checks required tables and fails if they are missing. Schema and migration changes are operator-invoked and must be tracked and rehearsed in staging first.

## 4. A Neon backup job fails

1. Keep Supabase primary and leave the last known Neon snapshot untouched.
2. Review the private scheduler output. The backup command prints UTC start/completion timestamps, per-table copied row counts, and a safe SQLSTATE when available; it does not print connection URLs.
3. Check that both URLs point to the intended providers and that Neon has the current ClassCode schema.
4. Retry only with `--confirm-overwrite` after verifying both targets. The target table replacement is transactional; a failure before commit rolls back the replacement.
5. Alert the operator if the most recent successful snapshot exceeds the agreed RPO.

The repository does not schedule backups, retain job logs, or verify provider-side encryption/permissions. Configure those in the trusted backup job and Neon project.

## Recommended schedule and retention

- Run the Supabase-to-Neon application-table snapshot daily at **02:00 Asia/Manila** from a trusted scheduler. This is a 24-hour logical-backup RPO; enable Supabase native backups/PITR as a separate layer if the plan supports a tighter recovery point. Store the marker outside the release directory and pass `--status-file <private-path>` to the backup command.
- After each successful run, execute `python tools/check_backup_age.py --status-file <private-path> --max-age-hours 26`; alert on a nonzero exit or any backup-job failure. The marker is atomically replaced only after commit and table row-count verification. A confirmed new run removes the previous success marker before database I/O; if that run fails, the age check reports a missing marker rather than treating an older run as current. Keep scheduler logs private and retain at least 90 days of success/failure metadata.
- Retain **30 daily** and **12 monthly** recovery points using distinct Neon branches/databases or a separate encrypted backup store. The current script replaces a single target, so retention is not achieved until the scheduler supplies separate targets and records each successful snapshot.
- Run an isolated staging restore rehearsal quarterly and after schema changes. Keep one known-good snapshot untouched while testing newer snapshots.
- If the acceptable RPO is less than 24 hours, run this full snapshot every 6 hours or rely on verified Supabase PITR for the shorter interval; account for provider connection/cost limits before scheduling.

## Restore rehearsal and command

The restore utility has automated isolated tests with mocked PostgreSQL connections. These verify endpoint direction and host confirmation, schema mismatch rejection before truncation, transactional table replacement, row-count verification, and safe identifier quoting. No real PostgreSQL restore has been run; conduct the first operational rehearsal against a new, empty staging Supabase project.

1. Stop HOKAS and prepare a new staging Supabase project. Preserve the current primary project unchanged.
2. Set `NEON_DATABASE_URL` to the intended backup and `DATABASE_URL` to the staging project's Supabase connection string in a private operator shell.
3. Configure both staging databases with the database-level custom settings `classcode.environment=staging` and a unique `classcode.project_id` matching the IDs you will confirm on the command line.
4. Apply the base schema only to the explicitly marked Supabase staging target, using `CLASSCODE_ENVIRONMENT=staging` and `python tools/apply_postgres_schema.py --target supabase --expected-host <exact-supabase-host> --expected-project-id <supabase-stage-id> --confirm-staging-target`.
5. Before restore, create and verify a backup of the destination Supabase staging project to a **separate Neon endpoint/branch**. Save its success marker outside the repository.
6. Run `python tools/restore_neon_to_supabase.py --expected-source-host <exact-neon-source-host> --expected-target-host <exact-supabase-host> --expected-source-project-id <neon-stage-id> --expected-target-project-id <supabase-stage-id> --pre-restore-backup-marker <private-marker-path> --confirm-staging-target --confirm-overwrite`.
7. Review the private output and compare source/target counts, inspect representative test data, verify sequences with safe inserts inside a rolled-back transaction, and run application validators before authorizing any production cutover.

The restore code verifies Neon and Supabase staging markers and project IDs independently, requires a verified pre-restore backup marker from a separate Neon endpoint, checks all ClassCode table/column names before truncation, reads Neon in a repeatable-read read-only transaction, replaces only listed ClassCode tables transactionally, verifies row counts, and repairs identity/serial sequences. These safeguards do not replace operator review.

## 5. HOKAS restarts unexpectedly

1. Confirm the bot environment still contains the Supabase `DATABASE_URL`, Discord token, and required intents; do not add `NEON_DATABASE_URL` to the bot runtime.
2. Restart with `pip install -r requirements.txt && python -m bot`.
3. Check startup, cog-load, Discord-ready, and database connection logs.
4. Confirm the bot is connected and reads current Supabase progress before inviting students back to retry failed actions.
5. Never restore or upload a local SQLite database from the deployment archive.

## Restore approval boundary

The restore utility is implemented and mock-tested but has not been run against a database. An actual restore, especially one targeting the live Supabase project, remains a separate destructive operation and requires explicit approval. Never place the only valid backup at risk during a test or rehearsal.
