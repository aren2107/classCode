"""Shared invite-code creation and validation for classes and study groups."""
from __future__ import annotations

import re
import secrets

_VALID_INVITE_CODE = re.compile(r"^(?:[0-9A-F]{6}|[0-9A-F]{16})$")


def new_invite_code() -> str:
    """Return a 64-bit code for new invites; six-character legacy codes remain accepted."""
    return secrets.token_hex(8).upper()


def normalize_invite_code(value: str) -> str | None:
    if not isinstance(value, str):
        return None
    candidate = value.strip().upper()
    return candidate if _VALID_INVITE_CODE.fullmatch(candidate) else None
