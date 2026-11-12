"""Fail when the latest verified ClassCode backup marker is missing or stale."""
from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone
import json
import math
from pathlib import Path
import sys


def backup_age_error(path: Path, max_age_hours: float, now: datetime | None = None) -> str | None:
    if not math.isfinite(max_age_hours) or max_age_hours <= 0:
        return "Maximum backup age must be a finite positive number of hours."
    now = now or datetime.now(timezone.utc)
    try:
        status = json.loads(path.read_text(encoding="utf-8"))
        completed_at = datetime.fromisoformat(status["completed_at"])
        if completed_at.tzinfo is None:
            return "Backup marker timestamp is missing a timezone."
        if status.get("status") != "succeeded" or status.get("verification") != "row_counts_passed":
            return "Latest backup marker is not a verified success."
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError):
        return "Backup marker is missing or invalid."

    age = now - completed_at.astimezone(timezone.utc)
    if age < timedelta(0):
        return "Backup marker timestamp is in the future."
    if age > timedelta(hours=max_age_hours):
        return f"Latest verified backup is older than {max_age_hours:g} hours."
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--status-file", required=True, type=Path)
    parser.add_argument("--max-age-hours", type=float, default=26)
    args = parser.parse_args()
    if args.max_age_hours <= 0:
        parser.error("--max-age-hours must be positive")
    error = backup_age_error(args.status_file, args.max_age_hours)
    if error:
        print(f"Backup age check failed: {error}", file=sys.stderr)
        return 1
    print("Latest backup age and row-count verification: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
