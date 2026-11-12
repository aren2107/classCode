from datetime import date, datetime
from zoneinfo import ZoneInfo


MANILA_TIMEZONE = ZoneInfo("Asia/Manila")


def manila_now() -> datetime:
    """Return the current timezone-aware Manila datetime."""
    return datetime.now(MANILA_TIMEZONE)


def manila_today() -> date:
    """Return the current calendar date in Manila."""
    return manila_now().date()


def manila_timestamp(value: datetime | None = None) -> datetime:
    """
    Return a Manila-local, timezone-naive datetime.

    This format is compatible with the existing PostgreSQL
    TIMESTAMP WITHOUT TIME ZONE columns.
    """
    if value is None:
        value = manila_now()

    if value.tzinfo is None or value.utcoffset() is None:
        raise ValueError("A timezone-aware datetime is required")

    return value.astimezone(MANILA_TIMEZONE).replace(tzinfo=None)
