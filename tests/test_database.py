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


class TestPostgresConnection:
    """Test _PostgresConnection adapter."""

    def test_execute_uses_normalized_query(self, mock_db_connection):
        """_PostgresConnection.execute should normalize query before execution."""
        from bot.database import _PostgresConnection

        adapter = _PostgresConnection(mock_db_connection)
        adapter.execute("SELECT * FROM users WHERE id = ?", (123,))

        # Verify normalized query was passed
        call_args = mock_db_connection.execute.call_args
        assert "%s" in call_args[0][0]
        assert call_args[0][1] == (123,)

    def test_execute_converts_bool_to_int(self, mock_db_connection):
        """Boolean parameters should be converted to int."""
        from bot.database import _PostgresConnection

        adapter = _PostgresConnection(mock_db_connection)
        adapter.execute("SELECT * FROM users WHERE active = ?", (True,))

        call_args = mock_db_connection.execute.call_args
        assert call_args[0][1] == (1,)

        adapter.execute("SELECT * FROM users WHERE active = ?", (False,))
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