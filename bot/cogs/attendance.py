
"""Daily attendance check-ins for ClassCode."""
from datetime import datetime, timedelta

import discord
from discord import app_commands
from discord.ext import commands

from bot.database import db
from bot.timezone import manila_now
from bot.learning.mastery import ensure_user_in_transaction
from bot.ui.embeds import UIEmbeds, ColorPalette


def _format_date(value: str) -> str:
    return datetime.strptime(value, "%Y-%m-%d").strftime("%B %d, %Y")


def _streak_from_dates(dates: list[str], today: str) -> int:
    """Count consecutive attendance dates backwards from today."""
    date_set = set(dates)
    cursor = datetime.strptime(today, "%Y-%m-%d").date()
    streak = 0
    while cursor.isoformat() in date_set:
        streak += 1
        cursor -= timedelta(days=1)
    return streak


def _best_streak(dates: list[str]) -> int:
    best = current = 0
    previous = None
    for value in sorted(set(dates)):
        current_date = datetime.strptime(value, "%Y-%m-%d").date()
        if previous is not None and current_date == previous + timedelta(days=1):
            current += 1
        else:
            current = 1
        best = max(best, current)
        previous = current_date
    return best


def _record_attendance_in_transaction(
    conn,
    user_id: int,
    username: str,
    today: str,
    checked_in_at: str,
) -> bool:
    ensure_user_in_transaction(conn, user_id, username)
    cursor = conn.execute(
        "INSERT OR IGNORE INTO attendance_records "
        "(user_id, attendance_date, checked_in_at) VALUES (?, ?, ?)",
        (user_id, today, checked_in_at),
    )
    return cursor.rowcount == 0


class AttendanceCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="attendance",
        description="Check in for today and view your ClassCode attendance streak.",
    )
    async def attendance(self, interaction: discord.Interaction):
        if interaction.guild is None:
            await interaction.response.send_message(
                "Use `/attendance` inside your ClassCode server's `#attendance` channel.",
                ephemeral=True,
            )
            return

        if (
            not isinstance(interaction.channel, discord.TextChannel)
            or interaction.channel.name != "attendance"
        ):
            await interaction.response.send_message(
                "📌 Please use `/attendance` in **#attendance** "
                "so daily check-ins stay together.",
                ephemeral=True,
            )
            return

        # Acknowledge before database reads/writes so Discord does not expire
        # the interaction while attendance data is being calculated.
        await interaction.response.defer(thinking=True)

        # Daily attendance follows the Philippines local calendar dates.
        now = manila_now()
        today = now.date().isoformat()
        user_id = interaction.user.id

        already_checked_in = await db.run_transaction(
            lambda conn: _record_attendance_in_transaction(
                conn,
                user_id,
                interaction.user.display_name,
                today,
                now.isoformat(timespec="seconds"),
            )
        )

        rows = await db.fetchall(
            "SELECT attendance_date FROM attendance_records "
            "WHERE user_id = ? ORDER BY attendance_date ASC",
            (user_id,),
        )
        dates = [row["attendance_date"] for row in rows]
        started = dates[0] if dates else today
        streak = _streak_from_dates(dates, today)
        total_days = len(dates)
        best = _best_streak(dates)

        if already_checked_in:
            heading = "✅ You're already checked in today!"
            color = ColorPalette.PRIMARY
            extra = "Your attendance is saved. You can check in again tomorrow."
        elif (
            streak == 1
            and total_days > 1
            and (now.date() - timedelta(days=1)).isoformat() not in set(dates)
        ):
            heading = "🔄 Attendance recorded — your streak starts at 1"
            color = ColorPalette.WARNING
            extra = (
                "A missed calendar day reset your previous streak. "
                "You're back on track today!"
            )
        else:
            heading = "🎉 Attendance recorded!"
            color = ColorPalette.SUCCESS
            extra = (
                "Keep showing up one day at a time. "
                "Consistency beats perfection."
            )

        embed = UIEmbeds.standard(
            f"📌 ClassCode Attendance • {interaction.user.display_name}",
            f"{heading}\n\n"
            f"**You started:** {_format_date(started)}\n"
            f"**Streak days:** {streak}\n"
            f"**Total days attended:** {total_days}\n"
            f"**Longest streak:** {best} day(s)\n"
            f"**Today's check-in:** {now.strftime('%I:%M %p')} "
            f"(Philippines time)\n\n"
            f"{extra}",
            color,
        )
        embed.set_footer(
            text="One check-in per day • Missing a day resets your current streak"
        )
        await interaction.followup.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(AttendanceCog(bot))
