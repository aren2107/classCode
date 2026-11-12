# ClassCode Deployment Rehearsal Report

**Date:** 2026-11-13  
**Status:** Local tasks complete; external infrastructure tasks pending

---

## Summary

This report documents the local preparation work completed for ClassCode Discord bot production deployment. Tasks requiring external Supabase/Neon infrastructure are noted as pending.

---

## Completed Tasks (Local)

### Task 1: Test Infrastructure Restoration ✅
**Commit:** 59de3ce  
**Tests:** 14/14 passing

- Restored pytest infrastructure with 14 tests covering:
  - Database placeholder conversion
  - PostgreSQL connection adapter
  - Database integration (mocked)
  - Slow operation logging
- Added `tests/conftest.py` with fixtures for mocking Config and psycopg
- Verified all tests pass with `pytest tests/test_database.py -v`

### Task 2: Convert Database Layer to Native PostgreSQL Patterns ✅
**Commit:** 76070e9  
**Tests:** 23/23 passing

Converted 7 files from SQLite patterns to native PostgreSQL:
- `bot/database.py` - Removed normalization call from `_PostgresConnection.execute`, kept functions for backward compatibility
- `bot/learning/mastery.py` - 11 SQL statements: `?` → `%s`, `INSERT OR IGNORE` → `ON CONFLICT`, `datetime('now')` → `CURRENT_TIMESTAMP`
- `bot/learning/progress.py` - 5 SQL statements converted
- `bot/cogs/quizzes.py` - `_save_practice_quiz_in_transaction` converted
- `bot/cogs/progress.py` - 5 SQL statements converted
- `bot/cogs/admin.py` - 2 execute calls + dynamic IN clause converted
- `bot/ui/lesson.py` - `get_mastery` and `record_mastery` functions converted
- Added `TestNativePostgreSQLPatterns` with 9 tests verifying no SQLite patterns remain

### Task 3: Refactor Curriculum Storage ✅
**Commit:** 4fe47da  
**Tests:** 4/4 passing + validation tools PASS

- Split `bot/learning/cpp.py` (9,525 lines) into 58 individual lesson files in `bot/learning/cpp/`
- Split `bot/learning/java.py` (8,947 lines) into 55 individual lesson files in `bot/learning/java/`
- Created dynamic loaders in `__init__.py` files that import and combine lessons
- Updated `cpp.py` and `java.py` to re-export from package
- All curriculum validation tools pass:
  - `validate_curriculum.py`: PASS (58 C++ + 55 Java lessons)
  - `validate_mastery.py`: PASS (5 questions per lesson, 5 skill categories)
  - `validate_educational_quality.py`: PASS

### Task 4: Add Missing Database Indexes ✅
**Commit:** 9c6901c  
**Tests:** 29/29 passing

Created migration `2026-11-13_add_missing_indexes.sql` with 3 indexes:
- `ix_cc_lesson_mastery_review_due` on `lesson_mastery(review_due_at) WHERE review_due_at IS NOT NULL`
- `ix_cc_user_progress_status` on `user_progress(status)`
- `ix_cc_quiz_attempts_topic_language` on `quiz_attempts(topic_id, language)`

Updated `tools/migration_runner.py`:
- Added migration to `FORWARD_MIGRATION_FILES`
- Added indexes to `EXPECTED_INDEXES`

Updated `migrations/README.md` with documentation.

Verified with `python tools/migration_runner.py --plan` — lists all 4 migrations.

---

## Pending Tasks (Require External Infrastructure)

### Task 5: Supabase Staging Migration Rehearsal ⏳
**Requires:** Isolated Supabase staging project
- Provision Supabase project (not production)
- Set `CLASSCODE_ENVIRONMENT=staging`, `STAGING_DATABASE_URL`, `STAGING_SSLROOTCERT`
- Verify project identity independently (hostname format, 20-char project ref, CA cert provenance)
- Run migration runner `--plan` then `--apply`
- Verify tracking table, FKs, indexes, curriculum validation

### Task 6: Full Integration Test Suite Against Staging ⏳
**Requires:** Staging Supabase DATABASE_URL
- Create integration tests in `tests/integration/`
- Test database connectivity, schema completeness, learning flow, XP reward atomicity
- Run against staging database

### Task 7: Configure and Rehearse Supabase-to-Neon Backup ⏳
**Requires:** Neon backup project
- Provision Neon project
- Run `backup_supabase_to_neon.py`
- Verify backup on Neon
- Rehearse restore to test database
- Run `verify_staging_restore.py`

---

## Deployment Readiness Assessment

| Component | Status |
|-----------|--------|
| Code quality (TDD, no SQLite patterns) | ✅ Complete |
| Database schema (native PostgreSQL) | ✅ Complete |
| Curriculum structure (maintainable) | ✅ Complete |
| Performance indexes | ✅ Migration ready |
| Staging migration rehearsal | ⏳ Requires Supabase project |
| Integration test suite | ⏳ Requires staging DB |
| Backup/restore rehearsal | ⏳ Requires Neon project |
| Production deployment checklist | 📝 Partial (see below) |

---

## Next Steps

1. **Provision Supabase staging project** — Run Task 5 steps
2. **Run staging migration rehearsal** — Complete Task 5 verification
3. **Run integration tests against staging** — Complete Task 6
4. **Provision Neon backup project** — Run Task 7 steps
5. **Complete production deployment checklist** — Final sign-off

---

## Local Verification Commands

All local tests pass:
```bash
pytest tests/ -v                    # 29 tests pass
python tools/validate_curriculum.py # PASS
python tools/validate_mastery.py    # PASS
python tools/validate_educational_quality.py # PASS
python tools/migration_runner.py --plan # 4 migrations listed
```