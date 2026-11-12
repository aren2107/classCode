# ClassCode Pre-Deployment Checklist

## Before starting HOKAS

1. Upload this ZIP and extract/replace the project files.
2. This release has no local database mode. Do not add database snapshots or local database files to the package.
3. Configure these environment variables in HOKAS:

```env
DISCORD_TOKEN=your_real_bot_token
GUILD_ID=your_test_or_server_id
GEMINI_API_KEY=your_real_gemini_api_key
GEMINI_MODEL=gemini-3.8-flash
DATABASE_URL=your_supabase_postgresql_connection_string
CODE_RUNNER_URL=https://ce.judge0.com
CODE_RUNNER_API_KEY=
CODE_RUNNER_AUTH_USER=
```

- `DATABASE_URL` must point to Supabase.
- Do not configure `DATABASE_PATH` or any local database setting; no local database is supported.
- Do not configure `NEON_DATABASE_URL` in the Discord bot runtime. Neon is reserved for a separate backup process.
- Keep all tokens and database credentials private.

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Start the bot:

```bash
python -m bot
```

The bot should stop with a clear traceback if a required extension cannot load. Do not continue to student testing if startup reports a required cog failure.

## Discord setup

- Server Members Intent: enabled
- Message Content Intent: enabled
- Bot role is above `Admin`, `Student`, and `Unverified`
- Bot has Manage Roles
- Bot has Manage Channels
- Bot can send/read messages and threads in ClassCode channels

Run `/setup` as an administrator.

## Database verification

- Confirm HOKAS has a valid Supabase `DATABASE_URL`.
- Verify the bot uses the configured Supabase PostgreSQL database; no fallback exists.
- Run the separate Supabase-to-Neon backup and verify its results.
- Never use Neon as the bot's normal read/write database.

---

## Production Readiness Tasks (2026-11-13 Plan)

### Local Preparation ✅ COMPLETE

- [x] **Task 1: Test Infrastructure** — 14 unit tests restored, all passing
- [x] **Task 2: Native PostgreSQL Conversion** — 7 files converted, 23 tests passing, zero SQLite patterns remain
- [x] **Task 3: Curriculum Refactor** — 113 lessons split into individual files, all validation tools PASS
- [x] **Task 4: Missing Database Indexes** — Migration created with 3 indexes, migration runner updated

### External Infrastructure Required ⏳ PENDING

- [ ] **Task 5: Supabase Staging Migration Rehearsal**
  - [ ] Provision isolated Supabase staging project
  - [ ] Set migration environment variables
  - [ ] Verify project identity independently
  - [ ] Run migration runner `--plan` and `--apply`
  - [ ] Verify tracking table, FKs, indexes, curriculum validation

- [ ] **Task 6: Full Integration Test Suite Against Staging**
  - [ ] Create integration tests in `tests/integration/`
  - [ ] Run against staging DATABASE_URL
  - [ ] Verify learning flow, XP rewards, schema completeness

- [ ] **Task 7: Supabase-to-Neon Backup Rehearsal**
  - [ ] Provision Neon backup project
  - [ ] Run backup script and verify on Neon
  - [ ] Rehearse restore to test database
  - [ ] Run verification script

### Final Sign-off ⏳ PENDING

- [ ] **Task 8: Production Deployment Checklist Completion**
  - [ ] All above tasks verified
  - [ ] DEPLOYMENT_REHEARSAL_REPORT.md reviewed
  - [ ] Final sign-off by authorized personnel
