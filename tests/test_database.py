"""Tests for database layer - ensuring native PostgreSQL patterns."""
import pytest
from unittest.mock import MagicMock, AsyncMock, patch


class TestDatabasePlaceholders:
    """Verify database layer uses native PostgreSQL %s placeholders."""

    def test_normalize_query_placeholder_conversion(self):
        """Test that ? placeholders are converted to %s."""
        from bot.database import _normalize_query_for_postgres

        # Basic placeholder conversion
        result = _normalize_query_for_postgres("SELECT * FROM users WHERE user_id = ?")
        assert "%s" in result
        assert "?" not in result or result.count("?") == 0

        # Multiple placeholders
        result = _normalize_query_for_postgres("INSERT INTO users (id, name) VALUES (?, ?)")
        assert result.count("%s") == 2

    def test_normalize_query_preserves_quoted_strings(self):
        """Quoted strings should not have placeholders converted."""
        from bot.database import _normalize_query_for_postgres

        query = "SELECT * FROM users WHERE name = 'O''Brien' AND id = ?"
        result = _normalize_query_for_postgres(query)
        assert "O''Brien" in result
        assert "%s" in result

    def test_normalize_query_handles_insert_or_ignore(self):
        """INSERT OR IGNORE should become INSERT ... ON CONFLICT DO NOTHING."""
        from bot.database import _normalize_query_for_postgres

        query = "INSERT OR IGNORE INTO users (id, name) VALUES (?, ?)"
        result = _normalize_query_for_postgres(query)
        assert "ON CONFLICT DO NOTHING" in result
        assert "INSERT OR IGNORE" not in result

    def test_normalize_query_datetime_now(self):
        """datetime('now', '-N day') should become CURRENT_TIMESTAMP - INTERVAL."""
        from bot.database import _normalize_query_for_postgres

        # The current implementation only handles datetime('now', '-N day') pattern
        query = "SELECT datetime('now', '-7 day')"
        result = _normalize_query_for_postgres(query)
        assert "CURRENT_TIMESTAMP - INTERVAL '7 days'" in result
        assert "datetime('now'" not in result

    def test_normalize_query_date_now(self):
        """date('now') should become CURRENT_DATE."""
        from bot.database import _normalize_query_for_postgres

        query = "SELECT date('now')"
        result = _normalize_query_for_postgres(query)
        assert "CURRENT_DATE" in result
        assert "date('now')" not in result


class TestNativePostgreSQLPatterns:
    """Verify all database queries use native PostgreSQL patterns (no normalization needed)."""

    def test_no_sqlite_placeholders_in_mastery(self):
        """mastery.py should use %s not ? placeholders."""
        from bot.learning import mastery
        import inspect
        source = inspect.getsource(mastery)
        # Should not contain ? placeholders in SQL
        assert "? " not in source or source.count("? ") == 0
        # Should use %s
        assert "%s" in source

    def test_no_sqlite_placeholders_in_progress(self):
        """progress.py should use %s not ? placeholders."""
        from bot.learning import progress
        import inspect
        source = inspect.getsource(progress)
        # Should not contain ? placeholders in SQL
        assert "? " not in source or source.count("? ") == 0
        # Should use %s
        assert "%s" in source

    def test_no_sqlite_placeholders_in_quizzes_cog(self):
        """quizzes.py should use %s not ? placeholders."""
        from bot.cogs import quizzes
        import inspect
        source = inspect.getsource(quizzes)
        assert "? " not in source or source.count("? ") == 0
        assert "%s" in source

    def test_no_sqlite_placeholders_in_progress_cog(self):
        """progress.py cog should use %s not ? placeholders."""
        from bot.cogs import progress as progress_cog
        import inspect
        source = inspect.getsource(progress_cog)
        assert "? " not in source or source.count("? ") == 0
        assert "%s" in source

    def test_no_sqlite_placeholders_in_admin_cog(self):
        """admin.py should use %s not ? placeholders."""
        from bot.cogs import admin
        import inspect
        source = inspect.getsource(admin)
        assert "? " not in source or source.count("? ") == 0
        assert "%s" in source

    def test_no_sqlite_placeholders_in_lesson_ui(self):
        """lesson.py should use %s not ? placeholders."""
        from bot.ui import lesson
        import inspect
        source = inspect.getsource(lesson)
        assert "? " not in source or source.count("? ") == 0
        assert "%s" in source

    def test_no_insert_or_ignore_in_codebase(self):
        """No INSERT OR IGNORE should remain; should use ON CONFLICT."""
        import inspect
        from bot.learning import mastery, progress
        from bot.cogs import quizzes, progress as progress_cog, admin
        from bot.ui import lesson

        for module in [mastery, progress, quizzes, progress_cog, admin, lesson]:
            source = inspect.getsource(module)
            # Check for raw INSERT OR IGNORE (not in comments)
            lines = source.split('\n')
            for line in lines:
                stripped = line.strip()
                if stripped.startswith('#') or stripped.startswith('"""') or "'''" in stripped:
                    continue
                assert "INSERT OR IGNORE" not in stripped.upper(), f"Found INSERT OR IGNORE in {module.__name__}: {line}"

    def test_no_datetime_now_in_codebase(self):
        """No datetime('now') patterns should remain; should use CURRENT_TIMESTAMP."""
        import inspect
        from bot.learning import mastery, progress
        from bot.cogs import quizzes, progress as progress_cog, admin
        from bot.ui import lesson

        for module in [mastery, progress, quizzes, progress_cog, admin, lesson]:
            source = inspect.getsource(module)
            lines = source.split('\n')
            for line in lines:
                stripped = line.strip()
                if stripped.startswith('#') or stripped.startswith('"""') or "'''" in stripped:
                    continue
                # datetime('now') should be replaced with CURRENT_TIMESTAMP
                assert "datetime('now')" not in stripped, f"Found datetime('now') in {module.__name__}: {line}"

    def test_database_normalization_is_noop(self):
        """After conversion, _normalize_query_for_postgres should be a no-op for native queries."""
        from bot.database import _normalize_query_for_postgres

        # Native PostgreSQL query should pass through unchanged
        native_query = "SELECT * FROM users WHERE user_id = %s"
        result = _normalize_query_for_postgres(native_query)
        assert result == native_query

        # ON CONFLICT queries should pass through unchanged
        upsert_query = "INSERT INTO users (id, name) VALUES (%s, %s) ON CONFLICT DO NOTHING"
        result = _normalize_query_for_postgres(upsert_query)
        assert result == upsert_query

        # CURRENT_TIMESTAMP should pass through unchanged
        ts_query = "SELECT CURRENT_TIMESTAMP"
        result = _normalize_query_for_postgres(ts_query)
        assert result == ts_query


class TestPostgresConnection:
    """Test _PostgresConnection adapter."""

    def test_execute_passes_query_directly(self, mock_db_connection):
        """_PostgresConnection.execute should pass query directly to psycopg (no normalization needed for native queries)."""
        from bot.database import _PostgresConnection

        adapter = _PostgresConnection(mock_db_connection)
        adapter.execute("SELECT * FROM users WHERE id = %s", (123,))

        # Verify query was passed directly (no normalization since all queries use native %s)
        call_args = mock_db_connection.execute.call_args
        assert call_args[0][0] == "SELECT * FROM users WHERE id = %s"
        assert call_args[0][1] == (123,)

    def test_execute_converts_bool_to_int(self, mock_db_connection):
        """Boolean parameters should be converted to int."""
        from bot.database import _PostgresConnection

        adapter = _PostgresConnection(mock_db_connection)
        adapter.execute("SELECT * FROM users WHERE active = %s", (True,))

        call_args = mock_db_connection.execute.call_args
        assert call_args[0][1] == (1,)

        adapter.execute("SELECT * FROM users WHERE active = %s", (False,))
        call_args = mock_db_connection.execute.call_args
        assert call_args[0][1] == (0,)


class TestDatabaseIntegration:
    """Integration-style tests for Database class (mocked)."""

    @pytest.mark.asyncio
    async def test_database_execute_returns_cursor(self, mock_db_connection):
        """Database.execute should return cursor from connection."""
        from bot.database import Database

        db = Database()
        mock_cursor = MagicMock()
        mock_db_connection.execute.return_value = mock_cursor

        with patch("psycopg.connect", return_value=mock_db_connection):
            result = await db.execute("SELECT 1")

        # Should return the cursor
        assert result == mock_cursor
        mock_db_connection.execute.assert_called_once()

    @pytest.mark.asyncio
    async def test_database_fetchone_returns_row(self, mock_db_connection):
        """Database.fetchone should return a single row."""
        from bot.database import Database

        db = Database()
        mock_row = {"id": 1, "name": "test"}
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = mock_row
        mock_db_connection.execute.return_value = mock_cursor

        with patch("psycopg.connect", return_value=mock_db_connection):
            result = await db.fetchone("SELECT * FROM users WHERE id = %s", (1,))

        assert result == mock_row
        mock_db_connection.execute.assert_called_once()
        mock_cursor.fetchone.assert_called_once()

    @pytest.mark.asyncio
    async def test_database_fetchall_returns_rows(self, mock_db_connection):
        """Database.fetchall should return multiple rows."""
        from bot.database import Database

        db = Database()
        mock_rows = [{"id": 1}, {"id": 2}]
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = mock_rows
        mock_db_connection.execute.return_value = mock_cursor

        with patch("psycopg.connect", return_value=mock_db_connection):
            result = await db.fetchall("SELECT * FROM users")

        assert result == mock_rows
        mock_db_connection.execute.assert_called_once()
        mock_cursor.fetchall.assert_called_once()

    @pytest.mark.asyncio
    async def test_database_run_transaction_commits(self, mock_db_connection):
        """Database.run_transaction should commit on success."""
        from bot.database import Database

        db = Database()
        mock_cursor = MagicMock()
        mock_db_connection.execute.return_value = mock_cursor
        mock_db_connection.info = MagicMock()
        mock_db_connection.info.transaction_status = 0

        def test_operation(conn):
            return "success"

        with patch("psycopg.connect", return_value=mock_db_connection):
            result = await db.run_transaction(test_operation)

        assert result == "success"
        mock_db_connection.commit.assert_called_once()

    @pytest.mark.asyncio
    async def test_database_run_transaction_rollbacks_on_error(self, mock_db_connection):
        """Database.run_transaction should rollback on error."""
        from bot.database import Database

        db = Database()
        mock_db_connection.info = MagicMock()
        mock_db_connection.info.transaction_status = 1  # In transaction

        def failing_operation(conn):
            raise ValueError("test error")

        with patch("psycopg.connect", return_value=mock_db_connection):
            with pytest.raises(ValueError):
                await db.run_transaction(failing_operation)

        mock_db_connection.rollback.assert_called_once()


class TestSlowOperationLogging:
    """Test slow operation threshold logging."""

    def test_slow_operation_logged(self, mock_db_connection, caplog):
        """Operations exceeding threshold should be logged."""
        from bot.database import Database
        import time

        db = Database()
        db.SLOW_OPERATION_THRESHOLD_MS = 1  # Very low threshold for testing

        mock_cursor = MagicMock()
        mock_db_connection.execute.return_value = mock_cursor
        mock_db_connection.info = MagicMock()
        mock_db_connection.info.transaction_status = 0

        with patch("psycopg.connect", return_value=mock_db_connection):
            # Use a sync operation that sleeps
            def slow_op():
                time.sleep(0.01)
                return "done"

            db._measure_operation("test", slow_op)

        # Check that warning was logged
        assert any("Slow database operation" in record.message for record in caplog.records)

    def test_fast_operation_not_logged(self, mock_db_connection, caplog):
        """Operations under threshold should not be logged."""
        from bot.database import Database

        db = Database()
        db.SLOW_OPERATION_THRESHOLD_MS = 1000  # Normal threshold

        mock_cursor = MagicMock()
        mock_db_connection.execute.return_value = mock_cursor
        mock_db_connection.info = MagicMock()
        mock_db_connection.info.transaction_status = 0

        with patch("psycopg.connect", return_value=mock_db_connection):
            def fast_op():
                return "done"

            db._measure_operation("test", fast_op)

        # Check that no warning was logged
        assert not any("Slow database operation" in record.message for record in caplog.records)


class TestMigrationIndexes:
    """Test that migration indexes are properly defined in migration runner."""

    def test_missing_indexes_in_expected_indexes(self):
        """New indexes from 2026-11-13 migration should be in EXPECTED_INDEXES."""
        from tools.migration_runner import EXPECTED_INDEXES

        assert "ix_cc_lesson_mastery_review_due" in EXPECTED_INDEXES
        assert EXPECTED_INDEXES["ix_cc_lesson_mastery_review_due"] == "lesson_mastery"

        assert "ix_cc_user_progress_status" in EXPECTED_INDEXES
        assert EXPECTED_INDEXES["ix_cc_user_progress_status"] == "user_progress"

        assert "ix_cc_quiz_attempts_topic_language" in EXPECTED_INDEXES
        assert EXPECTED_INDEXES["ix_cc_quiz_attempts_topic_language"] == "quiz_attempts"

    def test_new_migration_in_forward_list(self):
        """New migration should be in FORWARD_MIGRATION_FILES."""
        from tools.migration_runner import FORWARD_MIGRATION_FILES

        assert "2026-11-13_add_missing_indexes.sql" in FORWARD_MIGRATION_FILES