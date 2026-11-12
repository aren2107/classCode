"""Supabase-only PostgreSQL data access for ClassCode."""
from __future__ import annotations

import asyncio
import logging
import re
import threading
import time
from contextlib import closing
from pathlib import Path
from typing import Any

from bot.config import Config

logger = logging.getLogger("ClassCodeBot.database")


def _normalize_query_for_postgres(query: str) -> str:
    """Normalize the application's parameterized query conventions for PostgreSQL.

    This function is kept for backward compatibility but should be a no-op
    for native PostgreSQL queries that already use %s placeholders, ON CONFLICT,
    and CURRENT_TIMESTAMP.
    """
    sql = query.strip().rstrip(";")
    # Handle legacy patterns if any remain in the codebase
    ignore_insert = bool(re.match(r"(?is)^INSERT\s+OR\s+IGNORE\s+INTO\s+", sql))
    if ignore_insert:
        sql = re.sub(r"(?is)^INSERT\s+OR\s+IGNORE\s+INTO\s+", "INSERT INTO ", sql, count=1)
    sql = re.sub(r"(?is)datetime\(\s*'now'\s*,\s*'-(\d+)\s+day'\s*\)", r"(CURRENT_TIMESTAMP - INTERVAL '\1 days')", sql)
    sql = re.sub(r"(?is)date\(\s*'now'\s*\)", "CURRENT_DATE", sql)
    sql = re.sub(r"(?is)date\(\s*([a-z_][a-z0-9_.]*)\s*\)", r"(\1)::date", sql)
    sql = _replace_sql_placeholders(sql)
    if ignore_insert and not re.search(r"(?is)\bON\s+CONFLICT\b", sql):
        sql += " ON CONFLICT DO NOTHING"
    return sql


def _replace_sql_placeholders(sql: str) -> str:
    """Replace SQLite-style placeholders without changing quoted SQL text.

    Kept for backward compatibility - all new code should use %s directly.
    """
    result = []
    i = 0
    length = len(sql)

    while i < length:
        # Single-quoted strings.
        if sql[i] == "'":
            result.append(sql[i])
            i += 1
            while i < length:
                result.append(sql[i])
                if sql[i] == "'":
                    if i + 1 < length and sql[i + 1] == "'":
                        result.append(sql[i + 1])
                        i += 2
                        continue
                    i += 1
                    break
                if sql[i] == "\\" and i + 1 < length:
                    result.append(sql[i + 1])
                    i += 2
                    continue
                i += 1
            continue

        # Double-quoted identifiers.
        if sql[i] == '"':
            result.append(sql[i])
            i += 1
            while i < length:
                result.append(sql[i])
                if sql[i] == '"':
                    if i + 1 < length and sql[i + 1] == '"':
                        result.append(sql[i + 1])
                        i += 2
                        continue
                    i += 1
                    break
                i += 1
            continue

        # Line comments.
        if sql.startswith("--", i):
            end = sql.find("\n", i)
            if end == -1:
                result.append(sql[i:])
                break
            result.append(sql[i:end + 1])
            i = end + 1
            continue

        # Block comments.
        if sql.startswith("/*", i):
            end = sql.find("*/", i + 2)
            if end == -1:
                result.append(sql[i:])
                break
            result.append(sql[i:end + 2])
            i = end + 2
            continue

        # PostgreSQL dollar-quoted strings.
        if sql[i] == "$":
            delimiter_end = sql.find("$", i + 1)
            if delimiter_end != -1:
                tag = sql[i:delimiter_end + 1]
                if tag[1:-1] == "" or (
                    tag[1:-1][0].isalpha() or tag[1:-1][0] == "_"
                ) and all(
                    char.isalnum() or char == "_"
                    for char in tag[1:-1]
                ):
                    closing = sql.find(tag, delimiter_end + 1)
                    if closing == -1:
                        result.append(sql[i:])
                        break
                    result.append(sql[i:closing + len(tag)])
                    i = closing + len(tag)
                    continue

        result.append("%s" if sql[i] == "?" else sql[i])
        i += 1

    return "".join(result)


class _PostgresConnection:
    """Small adapter for query normalization; all I/O is handled by psycopg.

    Now passes queries directly to psycopg since all queries use native %s placeholders.
    """
    def __init__(self, connection):
        self._connection = connection

    def execute(self, query, params=()):
        params = tuple(int(value) if isinstance(value, bool) else value for value in (params or ()))
        return self._connection.execute(query, params)

    def __getattr__(self, name):
        return getattr(self._connection, name)

    def __enter__(self):
        self._connection.__enter__()
        return self

    def __exit__(self, exc_type, exc, tb):
        return self._connection.__exit__(exc_type, exc, tb)

    def close(self):
        return self._connection.close()


class Database:
    """A lazy, Supabase-only database facade. It never creates or migrates schema."""
    _operation_lock = threading.RLock()
    SLOW_OPERATION_THRESHOLD_MS = 1000

    def __init__(self):
        self._schema_path = Path(__file__).with_name("postgres_schema.sql")

    def _get_connection(self):
        if not Config.DATABASE_URL:
            raise RuntimeError("DATABASE_URL is required; configure Supabase PostgreSQL before starting ClassCode.")
        try:
            import psycopg
            from psycopg.rows import dict_row
        except ImportError as exc:
            raise RuntimeError("psycopg is not installed. Install dependencies from requirements.txt.") from exc
        try:
            connection = psycopg.connect(
                Config.DATABASE_URL,
                connect_timeout=10,
                sslmode="require",
                options="-c timezone=Asia/Manila",
                row_factory=dict_row,
            )
        except Exception as exc:
            logger.error("Supabase primary database connection failed (%s)", type(exc).__name__)
            raise RuntimeError("Could not connect to the configured Supabase PostgreSQL database.") from None
        return _PostgresConnection(connection)

    async def check_schema(self) -> None:
        """Read-only startup check; schema changes must be applied by an operator."""
        schema_text = self._schema_path.read_text(encoding="utf-8")
        expected = sorted(set(re.findall(
            r"(?i)CREATE\s+TABLE\s+IF\s+NOT\s+EXISTS\s+([a-z_][a-z0-9_]*)",
            schema_text,
        )))
        if not expected:
            raise RuntimeError("Could not determine the required ClassCode PostgreSQL tables.")

        def verify():
            with closing(self._get_connection()) as conn:
                rows = conn.execute(
                    "SELECT table_name FROM information_schema.tables "
                    "WHERE table_schema='public' AND table_type='BASE TABLE'"
                ).fetchall()
                available = {row["table_name"] for row in rows}
                missing = sorted(set(expected) - available)
                if missing:
                    raise RuntimeError(
                        "Supabase schema is incomplete. Missing tables: " + ", ".join(missing)
                        + ". Apply the reviewed PostgreSQL schema/migrations using the operator procedure; bot startup will not create them."
                    )
        await asyncio.to_thread(verify)

    def _measure_operation(self, label: str, operation):
        started = time.perf_counter()
        try:
            return operation()
        except Exception as exc:
            elapsed_ms = int((time.perf_counter() - started) * 1000)
            logger.warning("Database operation failed operation=%s elapsed_ms=%s error_type=%s", label, elapsed_ms, type(exc).__name__)
            raise
        finally:
            elapsed_ms = int((time.perf_counter() - started) * 1000)
            if elapsed_ms >= self.SLOW_OPERATION_THRESHOLD_MS:
                logger.warning("Slow database operation operation=%s elapsed_ms=%s", label, elapsed_ms)

    async def execute(self, query: str, params: tuple[Any, ...] = ()):
        def run():
            with self._operation_lock, closing(self._get_connection()) as conn:
                with conn:
                    return conn.execute(query, params)
        return await asyncio.to_thread(lambda: self._measure_operation("execute", run))

    async def run_transaction(self, operation):
        """Run an application transaction on the primary database only."""
        def run():
            with self._operation_lock, closing(self._get_connection()) as conn:
                try:
                    result = operation(conn)
                    conn.commit()
                    return result
                except BaseException:
                    if conn.info.transaction_status != 0:
                        conn.rollback()
                    raise
        return await asyncio.to_thread(lambda: self._measure_operation("transaction", run))

    async def fetchone(self, query: str, params: tuple[Any, ...] = ()):
        def run():
            with self._operation_lock, closing(self._get_connection()) as conn:
                return conn.execute(query, params).fetchone()
        return await asyncio.to_thread(lambda: self._measure_operation("fetchone", run))

    async def fetchall(self, query: str, params: tuple[Any, ...] = ()):
        def run():
            with self._operation_lock, closing(self._get_connection()) as conn:
                return conn.execute(query, params).fetchall()
        return await asyncio.to_thread(lambda: self._measure_operation("fetchall", run))


db = Database()
