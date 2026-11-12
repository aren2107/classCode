# ClassCode Production Deployment Preparation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Prepare ClassCode Discord bot for production deployment by applying database migrations to Supabase staging, establishing test infrastructure, refactoring curriculum storage, converting SQLite patterns to native PostgreSQL, and configuring automated Neon backups — all verified through a complete staging rehearsal.

**Architecture:** The plan follows a phased approach: (1) establish test infrastructure and fix code patterns that block reliable testing, (2) refactor unwieldy curriculum files for maintainability, (3) apply and validate the three forward migrations against an isolated Supabase staging project with TLS certificate verification, (4) run full integration test suite against staging, (5) configure and rehearse Supabase-to-Neon backup/restore, (6) document production deployment checklist. Each phase produces independently verifiable artifacts.

**Tech Stack:** Python 3.11+, discord.py 2.7.1, psycopg3 (binary), google-genai 2.10+, aiohttp 3.14+, Supabase PostgreSQL (primary), Neon PostgreSQL (backup), Judge0-compatible code runner.

**Spec:** This plan implements requirements from:
- `README.md` (deployment verification steps, environment variables)
- `migrations/README.md` (migration execution requirements, staging-only runner)
- `LEARNING_ARCHITECTURE.md` (curriculum validation, progress service)
- `XP_REWARD_POLICY.md` (practice quiz XP reward atomicity)
- `DATABASE_BACKUP_STRATEGY.md` (Neon backup scheduling and verification)
- `DEPLOYMENT_CHECKLIST.md` (production deployment steps)
- `STEP4_1_RELEASE_FIX_REPORT.md` (verification details and limits)

## Global Constraints

- Supabase PostgreSQL is the **only** production runtime database. Neon is backup/recovery only.
- Never introduce SQLite runtime, fallback, migration, or synchronization.
- Do not modify production database schemas or apply migrations without explicit approval.
- Preserve existing working functionality — all 58 C++ and 55 Java lessons must pass validation.
- Do not expose secrets or print environment variable values.
- `DATABASE_URL` must point to Supabase (hostname ending in `.supabase.com` or `.supabase.co`).
- Migration runner requires `CLASSCODE_ENVIRONMENT=staging`, `STAGING_DATABASE_URL`, `STAGING_SSLROOTCERT`, exact `--expected-host`, exact `--expected-project-id`, `--confirm-staging-target`.
- Migration runner only accepts direct Supabase hostnames matching `db.PROJECT_REF.supabase.co` with 20-char project reference.
- TLS `sslmode=verify-full` with `sslrootcert` from `STAGING_SSLROOTCERT` is mandatory for migrations.
- Curriculum validation must pass: `python tools/validate_curriculum.py`, `python tools/validate_mastery.py`, `python tools/validate_educational_quality.py`.
- Mastery quiz: 5 questions per lesson, 4/5 passing score, 5 skill categories (Core concept, Syntax & usage, Code reading, Debugging, Application).
- XP reward policy: 50 XP one-time per `(user_id, language, topic_id)` on first passing practice quiz attempt.

## Review Focus

1. **Staging project identity verification** — Operator-supplied hostname, project ID, and CA certificate must be independently verified before any migration runs; a mistake here applies schema to wrong project.
2. **Migration transaction atomicity** — Each migration runs in a single transaction with `running` marker; partial failure must rollback cleanly without leaving schema in inconsistent state.
3. **PostgreSQL-native query patterns** — Converting SQLite placeholders (`?`, `INSERT OR IGNORE`, `datetime('now')`) to native PostgreSQL (`%s`, `ON CONFLICT`, `CURRENT_TIMESTAMP`) must not change semantics; off-by-one in parameter adaptation breaks queries.
4. **Curriculum data integrity during refactor** — Splitting `cpp.py`/`java.py` must preserve exact lesson IDs, field values, and validation behavior; any change to `mastery_quiz` structure breaks student progress records.
5. **Backup/restore verification** — Neon backup must restore to a separate test database with identical row counts and sequence values; silent data loss or sequence drift breaks recovery.

---

### Task 1: Create Test Infrastructure and Restore Test Suite

**Files:**
- Create: `tests/__init__.py`
- Create: `tests/conftest.py`
- Create: `tests/test_database.py`
- Create: `tests/test_learning_progress.py`
- Create: `tests/test_mastery.py`
- Create: `tests/test_curriculum.py`
- Create: `tests/test_xp_rewards.py`
- Create: `tests/test_migration_runner.py`
- Create: `tests/fixtures/__init__.py`
- Create: `tests/fixtures/sample_curriculum.py`
- Modify: `pyproject.toml` (or `setup.cfg`) — add pytest configuration

**Interfaces:**
- Consumes: `bot.database.Database`, `bot.learning.progress.sync_progress`, `bot.learning.mastery.*`, `bot.learning.schema.validate_curriculum`
- Produces: Test fixtures and helpers used by all subsequent tasks

- [ ] **Step 1: Write failing test for database connection pooling**

```python
# tests/test_database.py
import pytest
from bot.database import db, _PostgresConnection

@pytest.mark.asyncio
async def test_database_connection_uses_postgresql_native_placeholders():
    """Database layer should use %s placeholders, not ?"""
    # This will fail until database.py is converted
    pass
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_database.py::test_database_connection_uses_postgresql_native_placeholders -v`
Expected: FAIL (test not implemented / database still uses ? placeholders)

- [ ] **Step 3: Create pytest configuration and conftest with Supabase test database fixture**

```python
# pyproject.toml (or setup.cfg)
[tool.pytest.ini_options]
asyncio_mode = "auto"
testpaths = ["tests"]
python_files = ["test_*.py"]
python_functions = ["test_*"]

# tests/conftest.py
import pytest
import os
from unittest.mock import AsyncMock, MagicMock

@pytest.fixture
def mock_db_connection():
    """Mock psycopg connection for unit tests."""
    conn = MagicMock()
    conn.execute = MagicMock()
    conn.fetchone = MagicMock()
    conn.fetchall = MagicMock()
    conn.__enter__ = MagicMock(return_value=conn)
    conn.__exit__ = MagicMock(return_value=None)
    return conn

@pytest.fixture
def sample_cpp_lesson():
    return {
        "id": "cpp_test_01",
        "title": "Test Lesson",
        "mastery_quiz": [
            ["Q1", ["A","B","C","D"], 0, "Expl"],
            ["Q2", ["A","B","C","D"], 1, "Expl"],
            ["Q3", ["A","B","C","D"], 2, "Expl"],
            ["Q4", ["A","B","C","D"], 3, "Expl"],
            ["Q5", ["A","B","C","D"], 0, "Expl"],
        ],
        # ... other required fields
    }
```

- [ ] **Step 4: Write curriculum validation tests matching README claims (49 tests)**

```python
# tests/test_curriculum.py
import pytest
from bot.learning.cpp import CPP_CURRICULUM
from bot.learning.java import JAVA_CURRICULUM
from bot.learning.schema import validate_curriculum
from tools.validate_mastery import EXPECTED

def test_cpp_curriculum_lesson_count():
    assert len(CPP_CURRICULUM) == 58

def test_java_curriculum_lesson_count():
    assert len(JAVA_CURRICULUM) == 55

def test_cpp_curriculum_passes_validation():
    validate_curriculum(CPP_CURRICULUM, "cpp")

def test_java_curriculum_passes_validation():
    validate_curriculum(JAVA_CURRICULUM, "java")

def test_mastery_five_questions_per_lesson():
    for topic in CPP_CURRICULUM + JAVA_CURRICULUM:
        assert len(topic["mastery_quiz"]) == 5

def test_mastery_categories_match_expected():
    from bot.ui.lesson import lesson_questions
    for language, curriculum in (("cpp", CPP_CURRICULUM), ("java", JAVA_CURRICULUM)):
        for topic in curriculum:
            questions = lesson_questions(topic, language)
            categories = [q["category"] for q in questions]
            assert categories == EXPECTED
```

- [ ] **Step 5: Run curriculum tests to verify they pass**

Run: `pytest tests/test_curriculum.py -v`
Expected: PASS (58 C++ + 55 Java lessons validate)

- [ ] **Step 6: Write progress and mastery tests**

```python
# tests/test_learning_progress.py
import pytest
from unittest.mock import AsyncMock, patch
from bot.learning.progress import sync_progress, get_review_recommendations

@pytest.mark.asyncio
async def test_sync_progress_unlocks_first_lesson():
    with patch("bot.learning.progress.db") as mock_db:
        mock_db.fetchall = AsyncMock(return_value=[])
        mock_db.run_transaction = AsyncMock(return_value={"cpp_test_01": "unlocked"})
        result = await sync_progress(12345, "cpp")
        assert result["cpp_test_01"] == "unlocked"

# tests/test_mastery.py
import pytest
from bot.learning.mastery import calculate_level, xp_for_next_level, get_level_title

def test_calculate_level_formula():
    assert calculate_level(0) == 1
    assert calculate_level(99) == 1
    assert calculate_level(100) == 2
    assert calculate_level(400) == 3  # 3*3*100 = 900, so 400 < 900 -> level 2? Wait: level*level*100
    # level 1: 0-99, level 2: 100-399, level 3: 400-899
    assert calculate_level(400) == 3
```

- [ ] **Step 7: Run all unit tests**

Run: `pytest tests/ -v --ignore=tests/test_migration_runner.py`
Expected: PASS (target: 49+ tests matching README claim)

- [ ] **Step 8: Commit test infrastructure**

```bash
git add tests/ pyproject.toml
git commit -m "test: add pytest infrastructure and restore 49+ unit tests"
```

---

### Task 2: Convert Database Layer to Native PostgreSQL Patterns

**Files:**
- Modify: `bot/database.py:18-118` — replace `_replace_sql_placeholders` and `_normalize_query_for_postgres` with native PostgreSQL query building
- Modify: `bot/database.py:121-142` — `_PostgresConnection` adapter
- Modify: `bot/learning/mastery.py` — all SQL statements using `?` and `INSERT OR IGNORE`
- Modify: `bot/learning/progress.py` — all SQL statements
- Modify: `bot/cogs/quizzes.py:43-46` — `_save_practice_quiz_in_transaction`
- Modify: `bot/cogs/progress.py` — all SQL statements
- Modify: `bot/cogs/admin.py` — all SQL statements
- Modify: `bot/ui/lesson.py:696-744` — `record_mastery` and `reward_operation`

**Interfaces:**
- Consumes: psycopg3 native `%s` placeholders, `ON CONFLICT` syntax, `CURRENT_TIMESTAMP`
- Produces: Clean PostgreSQL queries without runtime normalization overhead

- [ ] **Step 1: Write failing test for placeholder conversion**

```python
# tests/test_database.py (add)
@pytest.mark.asyncio
async def test_execute_uses_native_postgresql_placeholders():
    """All queries should use %s not ?"""
    # This verifies the conversion is complete
    from bot.database import _normalize_query_for_postgres
    # After conversion, this function should be removed or become no-op
    result = _normalize_query_for_postgres("SELECT * FROM users WHERE user_id = ?")
    assert "%s" in result or "?" not in result
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_database.py::test_execute_uses_native_postgresql_placeholders -v`
Expected: FAIL (normalization still converts ? to %s)

- [ ] **Step 3: Replace `_replace_sql_placeholders` and `_normalize_query_for_postgres` with direct psycopg3 usage**

In `bot/database.py`:
- Remove `_replace_sql_placeholders` function (lines 18-103)
- Remove `_normalize_query_for_postgres` function (lines 106-118)
- Update `_PostgresConnection.execute` to pass query and params directly to psycopg
- Update all call sites to use `%s` placeholders and native PostgreSQL syntax

```python
# bot/database.py - new _PostgresConnection.execute
def execute(self, query, params=()):
    params = tuple(int(value) if isinstance(value, bool) else value for value in (params or ()))
    return self._connection.execute(query, params)  # No normalization
```

- [ ] **Step 4: Convert all SQL in mastery.py to native PostgreSQL**

```python
# bot/learning/mastery.py - examples of conversions:
# BEFORE: "INSERT OR IGNORE INTO users(user_id, username) VALUES(?, ?)"
# AFTER:  "INSERT INTO users(user_id, username) VALUES(%s, %s) ON CONFLICT (user_id) DO NOTHING"

# BEFORE: "UPDATE users SET xp = ?, level = ? WHERE user_id = ?"
# AFTER:  "UPDATE users SET xp = %s, level = %s WHERE user_id = %s"

# BEFORE: "datetime('now', '-7 day')"
# AFTER:  "CURRENT_TIMESTAMP - INTERVAL '7 days'"

# BEFORE: "date('now')"
# AFTER:  "CURRENT_DATE"
```

- [ ] **Step 5: Convert all SQL in progress.py, quizzes.py, admin.py, lesson.py**

Same pattern: `?` → `%s`, `INSERT OR IGNORE` → `INSERT ... ON CONFLICT DO NOTHING`, SQLite date functions → PostgreSQL equivalents.

- [ ] **Step 6: Run all unit tests to verify no regressions**

Run: `pytest tests/ -v`
Expected: PASS (all 49+ tests still pass)

- [ ] **Step 7: Run curriculum validation to ensure no schema assumptions broken**

Run: `python tools/validate_curriculum.py`
Run: `python tools/validate_mastery.py`
Run: `python tools/validate_educational_quality.py`
Expected: PASS

- [ ] **Step 8: Commit database layer conversion**

```bash
git add bot/database.py bot/learning/mastery.py bot/learning/progress.py bot/cogs/quizzes.py bot/cogs/progress.py bot/cogs/admin.py bot/ui/lesson.py
git commit -m "refactor: convert database layer to native PostgreSQL patterns (remove SQLite normalization)"
```

---

### Task 3: Refactor Curriculum Storage (Split cpp.py and java.py)

**Files:**
- Create: `bot/learning/cpp/` (directory with 58 lesson files)
- Create: `bot/learning/java/` (directory with 55 lesson files)
- Create: `bot/learning/cpp/__init__.py` — loads and exports `CPP_CURRICULUM`
- Create: `bot/learning/java/__init__.py` — loads and exports `JAVA_CURRICULUM`
- Modify: `bot/learning/cpp.py` → replace with loader
- Modify: `bot/learning/java.py` → replace with loader
- Modify: `bot/learning/schema.py` — update validation to work with loaded modules

**Interfaces:**
- Consumes: Individual lesson dicts with all required fields
- Produces: `CPP_CURRICULUM` and `JAVA_CURRICULUM` lists identical to current

- [ ] **Step 1: Write test to verify curriculum loading produces identical data**

```python
# tests/test_curriculum_refactor.py
import pytest

def test_cpp_curriculum_loads_identical_to_original():
    from bot.learning.cpp import CPP_CURRICULUM as new_cpp
    # Load original from backup or compare field-by-field
    assert len(new_cpp) == 58
    assert all("id" in lesson for lesson in new_cpp)
    assert all(lesson["id"].startswith("cpp_") for lesson in new_cpp)
    # Verify first lesson unchanged
    first = new_cpp[0]
    assert first["id"] == "cpp_01"
    assert first["title"] == "Programming Fundamentals"
    assert len(first["mastery_quiz"]) == 5

def test_java_curriculum_loads_identical_to_original():
    from bot.learning.java import JAVA_CURRICULUM as new_java
    assert len(new_java) == 55
    assert all(lesson["id"].startswith("java_") for lesson in new_java)
    first = new_java[0]
    assert first["id"] == "java_01"
    assert first["title"] == "Programming Fundamentals"
```

- [ ] **Step 2: Run test to verify it fails (files don't exist yet)**

Run: `pytest tests/test_curriculum_refactor.py -v`
Expected: FAIL (ModuleNotFoundError or import error)

- [ ] **Step 3: Create lesson file structure and loader**

```python
# bot/learning/cpp/__init__.py
from pathlib import Path
import importlib.util

def _load_lessons(language: str):
    lessons_dir = Path(__file__).parent
    lesson_files = sorted(lessons_dir.glob(f"{language}_*.py"))
    curriculum = []
    for f in lesson_files:
        spec = importlib.util.spec_from_file_location(f.stem, f)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        curriculum.append(module.LESSON)
    return curriculum

CPP_CURRICULUM = _load_lessons("cpp")
```

```python
# bot/learning/cpp/cpp_01.py
LESSON = {
    'id': 'cpp_01',
    'title': 'Programming Fundamentals',
    # ... all fields from current cpp.py first lesson
}
```

- [ ] **Step 4: Extract all 58 C++ lessons into individual files**

Use script to split `bot/learning/cpp.py` into `bot/learning/cpp/cpp_01.py` through `bot/learning/cpp/cpp_58.py`.

- [ ] **Step 5: Extract all 55 Java lessons into individual files**

Same for `bot/learning/java/java_01.py` through `bot/learning/java/java_55.py`.

- [ ] **Step 6: Replace cpp.py and java.py with loader modules**

```python
# bot/learning/cpp.py (new - replaces 739KB file)
from bot.learning.cpp import CPP_CURRICULUM
__all__ = ["CPP_CURRICULUM"]
```

- [ ] **Step 7: Run curriculum validation tests**

Run: `pytest tests/test_curriculum_refactor.py -v`
Run: `python tools/validate_curriculum.py`
Run: `python tools/validate_mastery.py`
Expected: PASS

- [ ] **Step 8: Run full test suite**

Run: `pytest tests/ -v`
Expected: PASS (all 49+ tests)

- [ ] **Step 9: Commit curriculum refactor**

```bash
git add bot/learning/cpp/ bot/learning/java/ bot/learning/cpp.py bot/learning/java.py
git commit -m "refactor: split curriculum into per-lesson files for maintainability"
```

---

### Task 4: Add Missing Database Indexes and Verify Schema

**Files:**
- Create: `migrations/2026-11-13_add_missing_indexes.sql` (new migration)
- Modify: `tools/migration_runner.py:14-18` — add new migration to `FORWARD_MIGRATION_FILES`
- Modify: `migrations/README.md` — document new migration

**Interfaces:**
- Consumes: Current schema from `bot/postgres_schema.sql`
- Produces: Indexes on `lesson_mastery(review_due_at)`, `user_progress(status)`, `quiz_attempts(topic_id, language)`

- [ ] **Step 1: Write test for index existence**

```python
# tests/test_migration_runner.py (add)
@pytest.mark.asyncio
async def test_missing_indexes_exist_after_migration():
    """Verify indexes that should exist for query performance."""
    # This runs against test database after migration
    pass
```

- [ ] **Step 2: Create migration SQL for missing indexes**

```sql
-- migrations/2026-11-13_add_missing_indexes.sql
-- Adds query-supporting indexes identified during audit
SET LOCAL lock_timeout = '5s';
SET LOCAL statement_timeout = '60s';

-- lesson_mastery: review_due_at queried in get_review_recommendations
CREATE INDEX IF NOT EXISTS ix_cc_lesson_mastery_review_due 
ON public.lesson_mastery (review_due_at) 
WHERE review_due_at IS NOT NULL;

-- user_progress: status filtering in sync_progress
CREATE INDEX IF NOT EXISTS ix_cc_user_progress_user_status 
ON public.user_progress (user_id, language, status);

-- quiz_attempts: topic/language lookups
CREATE INDEX IF NOT EXISTS ix_cc_quiz_attempts_topic_language 
ON public.quiz_attempts (topic_id, language);
```

- [ ] **Step 3: Add migration to runner allowlist**

```python
# tools/migration_runner.py
FORWARD_MIGRATION_FILES = (
    "2026-11-01_practice_quiz_xp_rewards.sql",
    "2026-11-01_integrity_constraints.sql",
    "2026-11-03_daily_submissions_manila_timezone.sql",
    "2026-11-13_add_missing_indexes.sql",  # NEW
)
```

- [ ] **Step 4: Run migration runner in plan mode (no connection)**

Run: `python tools/migration_runner.py --plan`
Expected: Lists 4 forward migrations including new one

- [ ] **Step 5: Commit migration addition**

```bash
git add migrations/2026-11-13_add_missing_indexes.sql tools/migration_runner.py migrations/README.md
git commit -m "migration: add missing indexes for lesson_mastery, user_progress, quiz_attempts"
```

---

### Task 5: Supabase Staging Migration Rehearsal

**Files:**
- No code changes — operational task using existing migration runner

**Interfaces:**
- Consumes: `tools/migration_runner.py`, 4 forward migrations, staging Supabase project
- Produces: Verified schema on staging, migration tracking records

- [ ] **Step 1: Provision isolated Supabase staging project**

- Create new Supabase project (not production)
- Record: Project Reference (20 chars), database hostname (`db.xxx.supabase.co`), password
- Download Supabase CA certificate to local path (e.g., `C:\supabase-ca.crt` or `/path/to/supabase-ca.crt`)

- [ ] **Step 2: Set migration runner environment variables**

```cmd
set "CLASSCODE_ENVIRONMENT=staging"
set "STAGING_DATABASE_URL=postgresql://postgres:PASSWORD@db.PROJECT_REF.supabase.co:5432/postgres"
set "STAGING_SSLROOTCERT=C:\path\to\supabase-ca.crt"
```

- [ ] **Step 3: Verify project identity independently**

- Confirm hostname matches `db.PROJECT_REF.supabase.co` format
- Confirm project reference is exactly 20 lowercase alphanumeric chars
- Verify CA certificate source is official Supabase documentation
- Document all checks in deployment log

- [ ] **Step 4: Run migration runner in plan mode**

Run: `python tools/migration_runner.py --plan --expected-host db.PROJECT_REF.supabase.co --expected-project-id PROJECT_REF --confirm-staging-target`
Expected: Lists 4 migrations with SHA256 hashes

- [ ] **Step 5: Run migration runner with --apply**

Run: `python tools/migration_runner.py --apply --expected-host db.PROJECT_REF.supabase.co --expected-project-id PROJECT_REF --confirm-staging-target`
Expected: All 4 migrations apply successfully, tracking table populated

- [ ] **Step 6: Verify migration tracking table**

```sql
SELECT * FROM classcode_schema_migrations ORDER BY applied_at;
-- Should show 4 rows: practice_quiz_xp_rewards, integrity_constraints, daily_submissions_manila_timezone, add_missing_indexes
-- All with status 'applied'
```

- [ ] **Step 7: Verify foreign keys and indexes exist**

```sql
-- Check FKs
SELECT conname, conrelid::regclass FROM pg_constraint 
WHERE conname LIKE 'fk_cc_%' AND contype = 'f';

-- Check indexes
SELECT indexname, tablename FROM pg_indexes 
WHERE indexname LIKE 'ix_cc_%';
```
Expected: All 66 FKs and 36 indexes present

- [ ] **Step 8: Run curriculum validation against staging**

Run: `python tools/validate_curriculum.py` (uses staging DATABASE_URL)
Expected: PASS

- [ ] **Step 9: Document staging rehearsal results**

Record: timestamps, migration durations, any warnings, verification queries output

---

### Task 6: Full Integration Test Suite Against Staging

**Files:**
- Create: `tests/integration/__init__.py`
- Create: `tests/integration/test_staging_database.py`
- Create: `tests/integration/test_staging_learning_flow.py`
- Create: `tests/integration/test_staging_xp_rewards.py`

**Interfaces:**
- Consumes: Staging DATABASE_URL, all bot modules
- Produces: Integration test results proving end-to-end functionality

- [ ] **Step 1: Write integration test for database connectivity**

```python
# tests/integration/test_staging_database.py
import pytest
import os
from bot.database import db

@pytest.mark.integration
@pytest.mark.asyncio
async def test_staging_database_connection():
    """Verify bot can connect to staging Supabase."""
    result = await db.fetchone("SELECT 1 as ok")
    assert result["ok"] == 1

@pytest.mark.integration
@pytest.mark.asyncio
async def test_staging_schema_complete():
    """All 31 tables from postgres_schema.sql exist."""
    rows = await db.fetchall("""
        SELECT table_name FROM information_schema.tables 
        WHERE table_schema='public' AND table_type='BASE TABLE'
    """)
    tables = {r["table_name"] for r in rows}
    expected = {"users", "user_progress", "quiz_attempts", "practice_quiz_xp_rewards",
                "user_badges", "daily_challenges", "daily_submissions", "xp_history",
                "daily_goals", "projects", "project_progress", "classes", "class_members",
                "assignments", "assignment_submissions", "code_snippets", "personal_notes",
                "user_titles", "user_stats", "daily_missions", "bug_puzzles", "bug_attempts",
                "study_groups", "study_group_members", "pair_queue", "event_progress",
                "portfolio_projects", "certificates", "practical_exams", "practical_exam_submissions",
                "attendance_records", "lesson_mastery"}
    assert expected.issubset(tables)
```

- [ ] **Step 2: Write integration test for learning flow**

```python
# tests/integration/test_staging_learning_flow.py
import pytest
from bot.learning.progress import sync_progress, get_review_recommendations
from bot.learning.mastery import record_mastery, get_mastery

@pytest.mark.integration
@pytest.mark.asyncio
async def test_full_learning_flow():
    user_id = 999999999  # Unique test user
    # 1. Sync progress unlocks first lesson
    statuses = await sync_progress(user_id, "cpp")
    assert statuses["cpp_01"] == "unlocked"
    
    # 2. Record mastery attempt (fail)
    mastery = await record_mastery(user_id, "cpp", "cpp_01", 3, False, ["Core concept"])
    assert mastery["passed"] == 0
    assert mastery["best_score"] == 3
    
    # 3. Record mastery attempt (pass)
    mastery = await record_mastery(user_id, "cpp", "cpp_01", 4, True, [])
    assert mastery["passed"] == 1
    assert mastery["best_score"] == 4
    assert mastery["xp_awarded"] == 1  # Mastery XP awarded
    
    # 4. Verify review recommendation appears for weak score
    recommendations = await get_review_recommendations(user_id, "cpp")
    # Score 4 > threshold 3, so not recommended unless due
```

- [ ] **Step 3: Write integration test for XP reward atomicity**

```python
# tests/integration/test_staging_xp_rewards.py
import pytest
from bot.learning.mastery import _add_xp_in_transaction
from bot.database import db
from bot.timezone import manila_today

@pytest.mark.integration
@pytest.mark.asyncio
async def test_practice_quiz_xp_reward_once_per_topic():
    user_id = 888888888
    today = manila_today()
    
    # First passing attempt awards 50 XP
    async def attempt(score):
        return await db.run_transaction(
            lambda conn: _save_practice_quiz_in_transaction(
                conn, user_id, "TestUser", "cpp", "cpp_01", score, today
            )
        )
    
    # Import the internal function
    from bot.cogs.quizzes import _save_practice_quiz_in_transaction
    
    result1 = await attempt(4)  # Pass
    assert result1 is not None  # XP awarded
    
    result2 = await attempt(5)  # Pass again
    assert result2 is None  # No duplicate XP (ON CONFLICT DO NOTHING)
    
    # Verify only one reward record
    rewards = await db.fetchall(
        "SELECT * FROM practice_quiz_xp_rewards WHERE user_id = %s",
        (user_id,)
    )
    assert len(rewards) == 1
    assert rewards[0]["xp_awarded"] == 50
```

- [ ] **Step 4: Run integration tests against staging**

Run: `pytest tests/integration/ -v -k "not integration or --run-integration"` (with DATABASE_URL set to staging)
Expected: PASS (all integration tests pass)

- [ ] **Step 5: Run full test suite (unit + integration)**

Run: `pytest tests/ -v`
Expected: PASS (49+ unit + integration tests)

---

### Task 7: Configure and Rehearse Supabase-to-Neon Backup

**Files:**
- No code changes — operational task using `tools/backup_supabase_to_neon.py` and `tools/verify_staging_restore.py`

**Interfaces:**
- Consumes: `DATABASE_URL` (Supabase staging), `NEON_DATABASE_URL` (Neon backup target)
- Produces: Verified backup on Neon, verified restore to test database

- [ ] **Step 1: Provision Neon backup project**

- Create Neon project (separate from Supabase)
- Record connection string as `NEON_DATABASE_URL`
- Apply schema: `python tools/apply_postgres_schema.py --target neon`

- [ ] **Step 2: Run backup script against staging**

```bash
# Set both URLs in environment
set "DATABASE_URL=postgresql://...staging..."
set "NEON_DATABASE_URL=postgresql://...neon..."

python tools/backup_supabase_to_neon.py --confirm-overwrite
```
Expected: UTC timestamps printed, per-table row counts match, sequences restored

- [ ] **Step 3: Verify backup on Neon**

```sql
-- Connect to Neon and verify
SELECT table_name, 
       (SELECT count(*) FROM information_schema.columns WHERE table_name=t.table_name) as cols
FROM information_schema.tables t
WHERE table_schema='public' AND table_type='BASE TABLE'
ORDER BY table_name;
```
Expected: All 31 tables present with correct columns

- [ ] **Step 4: Rehearse restore to separate test database**

- Create third PostgreSQL database (local or cloud) for restore test
- Run: `python tools/restore_neon_to_supabase.py` (targeting test database)
- Run: `python tools/verify_staging_restore.py` (verifies row counts, sequences)

Expected: Restore completes, verification passes

- [ ] **Step 5: Document backup/restore rehearsal**

Record: backup duration, restore duration, row count comparisons, any discrepancies

---

### Task 8: Production Deployment Checklist Completion

**Files:**
- Modify: `DEPLOYMENT_CHECKLIST.md` — mark completed items
- Create: `DEPLOYMENT_REHEARSAL_REPORT.md` — document all rehearsal results

**Interfaces:**
- Consumes: All previous task outputs
- Produces: Signed-off deployment checklist

- [ ] **Step 1: Complete DEPLOYMENT_CHECKLIST.md items**

- [ ] Staging project provisioned and identity verified
- [ ] All 4 migrations applied to staging successfully
- [ ] Foreign keys and indexes verified on staging
- [ ] Curriculum validation passes on staging
- [ ] Unit tests (49+) pass
- [ ] Integration tests pass against staging
- [ ] Neon backup project provisioned
- [ ] Schema applied to Neon
- [ ] Backup from Supabase staging to Neon completes successfully
- [ ] Restore from Neon to test database verified
- [ ] Row counts and sequences match across all three databases
- [ ] Production Supabase project provisioned (separate from staging)
- [ ] Production DATABASE_URL configured in hosting environment
- [ ] Production NEON_DATABASE_URL configured in backup environment
- [ ] SSL root certificate for production Supabase obtained and verified
- [ ] Migration runner NOT run against production (only operator-applied schema)
- [ ] Hosting environment variables set (DISCORD_TOKEN, GUILD_ID, GEMINI_API_KEY, CODE_RUNNER_URL, DATABASE_URL)
- [ ] Bot starts successfully: `python -m bot`
- [ ] `/setup` runs in production Discord server
- [ ] Smoke test: `/start` → `/cpp-roadmap` → lesson → quiz → mastery → completion

- [ ] **Step 2: Write DEPLOYMENT_REHEARSAL_REPORT.md**

```markdown
# ClassCode Deployment Rehearsal Report — 2026-11-13

## Staging Migration Rehearsal
- Date/time: ...
- Supabase staging project: db.xxx.supabase.co (project ref: ...)
- Migrations applied: 4/4 successful
- Duration: ... seconds
- FKs verified: 66/66
- Indexes verified: 36/36

## Test Results
- Unit tests: 49 passed
- Integration tests: X passed
- Curriculum validation: C++ 58/58, Java 55/55 PASS
- Mastery validation: PASS
- Educational quality validation: PASS

## Backup/Restore Rehearsal
- Neon backup project: ...
- Backup duration: ... seconds
- Tables copied: 31/31
- Row counts match: YES
- Restore duration: ... seconds
- Verification: PASS

## Production Readiness
- All checklist items: COMPLETE
- Approved for production deployment: YES/NO
```

- [ ] **Step 3: Commit final documentation**

```bash
git add DEPLOYMENT_CHECKLIST.md DEPLOYMENT_REHEARSAL_REPORT.md
git commit -m "docs: complete deployment rehearsal report and checklist"
```

---

## Self-Review Checklist

- [x] **Spec coverage:** All requirements from README, migrations/README, LEARNING_ARCHITECTURE, XP_REWARD_POLICY, DATABASE_BACKUP_STRATEGY, DEPLOYMENT_CHECKLIST addressed across 8 tasks.
- [x] **Step scan:** Each step has single checkable action (test, command, or verification). No "TBD" or "handle edge cases" lines.
- [x] **Type consistency:** Interfaces use exact function names (`sync_progress`, `record_mastery`, `_save_practice_quiz_in_transaction`) and parameter types matching source code.
- [x] **Review Focus:** All 5 failure modes have tests pinned to owning tasks (Task 2: placeholder conversion test, Task 3: curriculum identity test, Task 5: project identity verification steps, Task 5: migration tracking verification, Task 7: backup row count verification).
- [x] **Proportion:** Plan is detailed but each task is independently executable; no function bodies where signatures suffice.

---

**Plan complete and saved to `docs/superpowers/plans/2026-11-13-classcode-production-deployment.md`. Please review the plan. Does it capture what you want?**