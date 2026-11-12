from __future__ import annotations

from datetime import date

from bot.timezone import manila_today

try:
    import discord
except ImportError:  # Allows pure progression tests without optional Discord dependencies.
    discord = None

from bot.database import db

LEVEL_TITLES = {
    1: "Beginner", 2: "Learner", 3: "Coder", 4: "Developer", 5: "Builder",
    6: "Problem Solver", 7: "Programmer", 8: "Architect", 9: "Master", 10: "Legend",
}
BADGES = {
    "first_steps": "First Steps", "cpp_beginner": "C++ Starter", "java_beginner": "Java Starter",
    "perfect_quiz": "Perfect Score", "streak_7": "On Fire", "bug_hunter": "Bug Hunter",
    "problem_solver": "Problem Solver", "cpp_master": "C++ Master", "java_master": "Java Master",
    "project_builder": "Project Builder", "speed_learner": "Speed Learner", "challenge_10": "Challenge Veteran",
}


def calculate_level(xp: int) -> int:
    level = 1
    while xp >= level * level * 100:
        level += 1
    return level


def xp_for_next_level(level: int) -> int:
    return level * level * 100


def get_level_title(level: int) -> str:
    return LEVEL_TITLES.get(level, "Master Coder")


def ensure_user_in_transaction(conn, user_id: int, username: str | None):
    conn.execute(
        "INSERT OR IGNORE INTO users(user_id, username) VALUES(?, ?)",
        (user_id, username or f"Discord user {user_id}"),
    )
    if username is not None:
        conn.execute("UPDATE users SET username = ? WHERE user_id = ?", (username, user_id))


async def ensure_user(user_id: int, username: str):
    def operation(conn):
        ensure_user_in_transaction(conn, user_id, username)

    await db.run_transaction(operation)


def _update_streak_in_transaction(conn, user_id: int, today: date):
    today_str = today.isoformat()
    row = conn.execute(
        "SELECT streak_count, last_active_date FROM users WHERE user_id = ?",
        (user_id,),
    ).fetchone()
    if not row or not row["last_active_date"]:
        conn.execute(
            "UPDATE users SET streak_count = 1, last_active_date = ? WHERE user_id = ?",
            (today_str, user_id),
        )
        return 1, 0

    try:
        diff = (today - date.fromisoformat(row["last_active_date"])).days
    except (ValueError, TypeError):
        diff = 0

    if diff == 1:
        streak = (row["streak_count"] or 0) + 1
        bonus = 25 if streak >= 3 else 0
        conn.execute(
            "UPDATE users SET streak_count = ?, last_active_date = ? WHERE user_id = ?",
            (streak, today_str, user_id),
        )
        return streak, bonus
    if diff > 1:
        conn.execute(
            "UPDATE users SET streak_count = 1, last_active_date = ? WHERE user_id = ?",
            (today_str, user_id),
        )
        return 1, 0
    return row["streak_count"] or 1, 0


async def update_streak(user_id: int):
    today = manila_today()

    def operation(conn):
        return _update_streak_in_transaction(conn, user_id, today)

    return await db.run_transaction(operation)


def _add_xp_in_transaction(conn, user_id: int, username: str, amount: int, reason: str, today: date):
    """Apply an XP award using the caller's transaction and return its result."""
    if not isinstance(amount, int) or isinstance(amount, bool) or amount < 0:
        raise ValueError("XP awards must be non-negative integers.")

    ensure_user_in_transaction(conn, user_id, username)

    streak, bonus = _update_streak_in_transaction(conn, user_id, today)
    earned = amount + bonus
    row = conn.execute("SELECT xp, level FROM users WHERE user_id = ?", (user_id,)).fetchone()
    old_level = row["level"] if row else 1
    current_xp = (row["xp"] if row else 0) + earned
    new_level = calculate_level(current_xp)
    conn.execute(
        "UPDATE users SET xp = ?, level = ? WHERE user_id = ?",
        (current_xp, new_level, user_id),
    )
    conn.execute(
        "INSERT INTO xp_history(user_id, amount, reason) VALUES(?, ?, ?)",
        (user_id, earned, reason),
    )
    today_str = today.isoformat()
    conn.execute("INSERT OR IGNORE INTO daily_goals(user_id, goal_date) VALUES(?, ?)", (user_id, today_str))
    conn.execute(
        "UPDATE daily_goals SET xp_earned = xp_earned + ? WHERE user_id = ? AND goal_date = ?",
        (earned, user_id, today_str),
    )
    return current_xp, new_level > old_level, new_level, streak


def _complete_lesson_in_transaction(conn, user_id: int, username: str, language: str, topic_id: str, today: date):
    changed = conn.execute(
        "UPDATE user_progress SET status='completed',completed_at=CURRENT_TIMESTAMP "
        "WHERE user_id=? AND language=? AND topic_id=? AND status='unlocked'",
        (user_id, language, topic_id),
    ).rowcount == 1
    if not changed:
        return None
    result = _add_xp_in_transaction(
        conn, user_id, username, 20, f"Completed {language.upper()} lesson", today,
    )
    today_str = today.isoformat()
    conn.execute("INSERT OR IGNORE INTO daily_goals(user_id,goal_date) VALUES(?,?)", (user_id, today_str))
    conn.execute("UPDATE daily_goals SET lessons=lessons+1 WHERE user_id=? AND goal_date=?", (user_id, today_str))
    return result


def _complete_project_in_transaction(conn, user_id: int, username: str, project_id: str, xp: int, title: str, today: date):
    changed = conn.execute(
        "INSERT INTO project_progress(user_id,project_id,status,completed_at) VALUES(?,?,'completed',CURRENT_TIMESTAMP) "
        "ON CONFLICT(user_id,project_id) DO UPDATE SET status='completed',completed_at=CURRENT_TIMESTAMP "
        "WHERE project_progress.status <> 'completed'",
        (user_id, project_id),
    ).rowcount == 1
    if not changed:
        return None
    return _add_xp_in_transaction(conn, user_id, username, xp, f"Completed project: {title}", today)


def _submit_assignment_in_transaction(
    conn, user_id: int, username: str, assignment_id: int, today: date,
):
    """Submit an assignment only while the student is a current class member."""
    assignment = conn.execute(
        "SELECT a.title FROM assignments a "
        "JOIN class_members cm ON cm.class_id = a.class_id "
        "WHERE a.assignment_id = ? AND cm.user_id = ? "
        "FOR UPDATE OF a, cm",
        (assignment_id, user_id),
    ).fetchone()
    if not assignment:
        return None

    inserted = conn.execute(
        "INSERT INTO assignment_submissions"
        "(assignment_id,user_id,status,submitted_at) "
        "VALUES(?,?,'submitted',CURRENT_TIMESTAMP) "
        "ON CONFLICT(assignment_id,user_id) DO NOTHING",
        (assignment_id, user_id),
    ).rowcount == 1
    if not inserted:
        return False

    return _add_xp_in_transaction(
        conn, user_id, username, 25,
        f"Submitted assignment: {assignment['title']}", today,
    )


async def _publish_xp_result(user_id: int, guild: discord.Guild | None, result):
    current_xp, leveled_up, new_level, streak = result
    if streak >= 7:
        await award_badge(user_id, "streak_7", guild)
    if guild and leveled_up:
        embed = discord.Embed(
            title="🎉 LEVEL UP!",
            description=f"<@{user_id}> reached **Level {new_level} — {get_level_title(new_level)}**!",
            color=discord.Color.gold(),
        )
        await broadcast_achievement(guild, embed)
    return current_xp, leveled_up, new_level, streak


def _record_goal_in_transaction(conn, user_id: int, kind: str, today: date, xp: int = 0):
    today_str = today.isoformat()
    ensure_user_in_transaction(conn, user_id, None)
    field = {"lesson": "lessons", "quiz": "quizzes", "challenge": "challenges"}.get(kind)
    conn.execute(
        "INSERT OR IGNORE INTO daily_goals(user_id, goal_date) VALUES(?, ?)",
        (user_id, today_str),
    )
    if field:
        conn.execute(
            f"UPDATE daily_goals SET {field} = {field} + ?, xp_earned = xp_earned + ? "
            "WHERE user_id = ? AND goal_date = ?",
            (1, xp, user_id, today_str),
        )
    elif xp:
        conn.execute(
            "UPDATE daily_goals SET xp_earned = xp_earned + ? WHERE user_id = ? AND goal_date = ?",
            (xp, user_id, today_str),
        )


async def record_goal(user_id: int, kind: str, xp: int = 0):
    today = manila_today()

    def operation(conn):
        _record_goal_in_transaction(conn, user_id, kind, today, xp)

    await db.run_transaction(operation)


async def add_xp(
    user_id: int,
    username: str,
    amount: int,
    guild: discord.Guild | None = None,
    reason: str = "Activity",
):
    """Atomically award XP so simultaneous events cannot overwrite one another."""
    today = manila_today()
    result = await db.run_transaction(
        lambda conn: _add_xp_in_transaction(conn, user_id, username, amount, reason, today)
    )
    return await _publish_xp_result(user_id, guild, result)


async def award_badge(
    user_id: int,
    badge_id: str,
    guild: discord.Guild | None = None,
) -> bool:
    """Award a badge once, even when multiple events race to award it."""
    def operation(conn):
        cursor = conn.execute(
            "INSERT OR IGNORE INTO user_badges(user_id, badge_id) VALUES(?, ?)",
            (user_id, badge_id),
        )
        return cursor.rowcount == 1

    awarded = await db.run_transaction(operation)
    if awarded and guild:
        embed = discord.Embed(
            title="🏅 BADGE UNLOCKED!",
            description=f"<@{user_id}> unlocked **{BADGES.get(badge_id, badge_id)}**!",
            color=discord.Color.blue(),
        )
        await broadcast_achievement(guild, embed)
    return awarded


async def broadcast_achievement(guild: discord.Guild, embed: discord.Embed):
    if discord is None:
        return
    channel = discord.utils.get(guild.text_channels, name="achievements")
    if channel:
        try:
            await channel.send(embed=embed)
        except discord.Forbidden:
            pass
