from __future__ import annotations

from datetime import datetime
import re

from bot.timezone import manila_timestamp
from bot.database import db
from bot.learning.mastery import ensure_user_in_transaction
from bot.learning.cpp import CPP_CURRICULUM
from bot.learning.java import JAVA_CURRICULUM


def curriculum_for(language: str):
    normalized = language.lower()
    if normalized in ("cpp", "c++"):
        return CPP_CURRICULUM
    if normalized == "java":
        return JAVA_CURRICULUM
    raise ValueError(f"Unsupported learning language: {language}")


async def get_status(user_id: int, language: str, topic_id: str) -> str:
    row = await db.fetchone(
        "SELECT status FROM user_progress WHERE user_id=? AND language=? AND topic_id=?",
        (user_id, language, topic_id),
    )
    return row["status"] if row else "locked"


def _sync_progress_in_transaction(conn, user_id: int, language: str, curriculum: list[dict]):
    ensure_user_in_transaction(conn, user_id, None)
    rows = conn.execute(
        "SELECT topic_id, status FROM user_progress WHERE user_id=? AND language=?",
        (user_id, language),
    ).fetchall()
    statuses = {r["topic_id"]: r["status"] for r in rows}

    placement = conn.execute(
        "SELECT body FROM personal_notes WHERE user_id=? AND title=? ORDER BY note_id DESC LIMIT 1",
        (user_id, f"ClassCode Placement {language.upper()}"),
    ).fetchone()
    start_index = 0
    if placement:
        match = re.search(r"START_INDEX:\s*(\d+)", placement["body"] or "")
        if match:
            start_index = max(0, min(int(match.group(1)), len(curriculum) - 1))

    # An admin-assigned lesson is an explicit access grant. It does not alter
    # prior completion records, and remains the student's active lesson until
    # an admin assigns a different one.
    assignment = conn.execute(
        "SELECT body FROM personal_notes WHERE user_id=? AND title=? ORDER BY note_id DESC LIMIT 1",
        (user_id, f"ClassCode Assigned Lesson {language.upper()}"),
    ).fetchone()
    assigned_topic_id = (assignment["body"] or "").strip() if assignment else ""
    assigned_index = next(
        (i for i, topic in enumerate(curriculum) if topic["id"] == assigned_topic_id),
        None,
    )

    for index, topic in enumerate(curriculum):
        current = statuses.get(topic["id"])
        if current == "completed":
            continue

        # An admin assignment to a later lesson unlocks the path leading up to
        # it, so students can open previous lessons without falsely completing
        # them. The assigned lesson itself is also unlocked. Later lessons still
        # follow the normal prerequisite rules.
        if assigned_index is not None and index <= assigned_index:
            status = "unlocked"
        elif index < start_index:
            status = "review"
        else:
            prerequisites = topic.get("prerequisites", [])
            prereqs_done = all(statuses.get(dep) == "completed" for dep in prerequisites)
            # Placement explicitly grants access to the recommended starting lesson.
            placement_grant = index == start_index
            status = "unlocked" if (prereqs_done or placement_grant) else "locked"
        conn.execute(
            "INSERT INTO user_progress(user_id,language,topic_id,status) VALUES(?,?,?,?) "
            "ON CONFLICT(user_id,language,topic_id) DO UPDATE SET "
            "status=CASE WHEN user_progress.status='completed' THEN 'completed' ELSE excluded.status END",
            (user_id, language, topic["id"], status),
        )
        statuses[topic["id"]] = "completed" if current == "completed" else status
    return {
        r["topic_id"]: r["status"]
        for r in conn.execute(
            "SELECT topic_id,status FROM user_progress WHERE user_id=? AND language=?",
            (user_id, language),
        ).fetchall()
    }


async def sync_progress(user_id: int, language: str):
    curriculum = curriculum_for(language)
    return await db.run_transaction(
        lambda conn: _sync_progress_in_transaction(conn, user_id, language, curriculum)
    )


async def get_review_recommendations(user_id: int, language: str | None = None, limit: int = 5):
    """Return completed lessons worth reviewing, prioritizing weak mastery."""
    languages = [language] if language else ["cpp", "java"]
    results = []
    for lang in languages:
        curriculum = curriculum_for(lang)
        rows = await db.fetchall(
            "SELECT topic_id,best_score,last_score,attempts,passed,weak_categories,review_due_at,updated_at FROM lesson_mastery "
            "WHERE user_id=? AND language=? AND passed=1 "
            "ORDER BY CASE WHEN review_due_at IS NOT NULL AND review_due_at <= CURRENT_TIMESTAMP THEN 0 ELSE 1 END, best_score ASC, updated_at ASC",
            (user_id, lang),
        )
        by_id = {r["topic_id"]: r for r in rows}
        for topic in curriculum:
            row = by_id.get(topic["id"])
            if not row:
                continue
            score = int(row["best_score"])
            
            due_at = row["review_due_at"]
            if isinstance(due_at, str):
                due_at = datetime.fromisoformat(due_at)

            now = manila_timestamp()
            due = bool(due_at and now >= due_at)
            
            if score <= int(topic.get("review_threshold", 3)) or due:
                results.append({
                    "language": lang,
                    "topic": topic,
                    "best_score": score,
                    "attempts": int(row["attempts"]),
                    "last_score": int(row["last_score"] or 0),
                    "weak_categories": row["weak_categories"] or "",
                    "review_due_at": row["review_due_at"],
                    "updated_at": row["updated_at"],
                })
    results.sort(key=lambda item: (item["best_score"], str(item["updated_at"])))
    return results[:max(1, limit)]
