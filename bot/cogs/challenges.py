import json
import hashlib
from datetime import date

import discord
from discord.ext import commands
from discord import app_commands

from bot.timezone import manila_now, manila_timestamp
from bot.ui.embeds import UIEmbeds, ColorPalette
from bot.learning.mastery import (
    _add_xp_in_transaction,
    _publish_xp_result,
    award_badge,
    ensure_user_in_transaction,
)
from bot.database import db
from bot.services.code_runner import CodeRunnerError, runner


def _daily_submission_lock_key(user_id: int, challenge_id: str) -> int:
    """Generate a stable signed 64-bit PostgreSQL advisory-lock key."""
    lock_identity = f"{user_id}:{challenge_id}".encode("utf-8")
    digest = hashlib.blake2b(lock_identity, digest_size=8).digest()
    return int.from_bytes(digest, byteorder="big", signed=True)


CHALLENGES = [
    {
        "id": "student-average",
        "language": "cpp",
        "title": "Student Average",
        "description": "Read three integer grades and print their average as a number.",
        "requirements": [
            "Read three integers from stdin.",
            "Calculate the arithmetic average.",
            "Print the result.",
        ],
        "tests": [
            {"input": "80 90 100\n", "output": "90"},
            {"input": "50 60 70\n", "output": "60"},
            {"input": "75 75 75\n", "output": "75"},
        ],
    },
    {
        "id": "even-or-odd",
        "language": "java",
        "title": "Even or Odd",
        "description": "Read one integer and print `Even` when divisible by 2, otherwise print `Odd`.",
        "requirements": [
            "Read one integer.",
            "Use a condition to test divisibility by 2.",
            "Print exactly `Even` or `Odd`.",
        ],
        "tests": [
            {"input": "8\n", "output": "Even"},
            {"input": "13\n", "output": "Odd"},
            {"input": "0\n", "output": "Even"},
        ],
    },
    {
        "id": "largest-of-three",
        "language": "cpp",
        "title": "Largest of Three",
        "description": "Read three integers and print the largest value.",
        "requirements": [
            "Read three integers.",
            "Compare the values correctly.",
            "Print only the largest value.",
        ],
        "tests": [
            {"input": "4 9 2\n", "output": "9"},
            {"input": "12 3 7\n", "output": "12"},
            {"input": "5 5 2\n", "output": "5"},
        ],
    },
]


class ChallengesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def today_challenge(self, today: date | None = None):
        today = today or manila_now().date()
        return CHALLENGES[today.toordinal() % len(CHALLENGES)]

    @app_commands.command(
        name="daily-challenge",
        description="View today's coding challenge.",
    )
    async def daily_challenge(self, interaction: discord.Interaction):
        today = manila_now().date()
        c = self.today_challenge(today)

        tests = "\n".join(
            f"\u2022 `{t['input'].strip()}` \u2192 `{t['output']}`"
            for t in c["tests"]
        )

        embed = UIEmbeds.standard(
            f"\U0001f525 DAILY CHALLENGE \u2014 {c['title']}",
            f"**Language:** `{c['language'].upper()}`\n"
            f"**Difficulty:** \U0001f7e1 Intermediate\n\n"
            f"{c['description']}\n\n"
            f"**Requirements**\n"
            + "\n".join(f"\u2022 {x}" for x in c["requirements"])
            + f"\n\n**Sample tests**\n{tests}\n\n"
            "Use `/submit-challenge` to run your solution against "
            "hidden-style practice tests and earn XP.",
        )

        await interaction.response.send_message(embed=embed)

    @app_commands.command(
        name="submit-challenge",
        description="Submit code for today's coding challenge.",
    )
    @app_commands.checks.cooldown(
        1,
        30.0,
        key=lambda interaction: interaction.user.id,
    )
    @app_commands.choices(
        language=[
            app_commands.Choice(name="C++", value="cpp"),
            app_commands.Choice(name="Java", value="java"),
        ]
    )
    @app_commands.describe(
        language="Language of your solution",
        code="Complete program",
    )
    async def submit_challenge(
        self,
        interaction: discord.Interaction,
        language: app_commands.Choice[str],
        code: str,
    ):
        # A submission belongs to the Manila date when it starts,
        # even if code execution finishes after midnight.
        submission_now = manila_now()
        today = submission_now.date()
        submitted_at = manila_timestamp(submission_now)
        challenge = self.today_challenge(today)

        if language.value != challenge["language"]:
            await interaction.response.send_message(
                f"\u274c Today's challenge expects "
                f"**{challenge['language'].upper()}**.",
                ephemeral=True,
            )
            return

        await interaction.response.defer()

        # Prevent repeated XP rewards for the same challenge
        # on the same Manila calendar date.
        cleaned = (
            code.strip()
            .replace("```cpp", "")
            .replace("```java", "")
            .replace("```", "")
            .strip()
        )

        passed = 0
        details = []

        for test in challenge["tests"]:
            try:
                result = await runner.run(
                    language.value,
                    cleaned,
                    test["input"],
                )

                actual = (result.stdout or "").strip()
                expected = test["output"].strip()
                ok = result.successful and actual == expected

                passed += int(ok)

                displayed_output = (
                    actual[:500] + "\u2026"
                    if len(actual) > 500
                    else (actual or "no output")
                )

                details.append(
                    f"{'\u2705' if ok else '\u274c'} "
                    f"`{test['input'].strip()}` \u2192 "
                    f"`{displayed_output}`"
                )

                if not result.successful and (
                    result.stderr or result.compile_output
                ):
                    details.append(
                        f"\U0001f41b "
                        f"{(result.stderr or result.compile_output).strip()[:500]}"
                    )

            except CodeRunnerError as exc:
                details.append(
                    f"\u26a0\ufe0f Test runner unavailable: {exc}"
                )
                break

        total = len(challenge["tests"])
        status = "passed" if passed == total else "partial"

        def save_submission(conn):
            lock_key = _daily_submission_lock_key(
                interaction.user.id,
                challenge["id"],
            )
            conn.execute(
                "SELECT pg_advisory_xact_lock(?)",
                (lock_key,),
            )
        
            ensure_user_in_transaction(
                conn,
                interaction.user.id,
                interaction.user.display_name,
            )

            previous = conn.execute(
                "SELECT status,score FROM daily_submissions "
                "WHERE user_id=? AND challenge_id=? "
                "AND submitted_at::date=?",
                (interaction.user.id, challenge["id"], today),
            ).fetchone()

            already_credited_today = bool(
                previous and previous["status"] == "passed"
            )

            stored_status = (
                "passed" if already_credited_today else status
            )

            stored_score = (
                max(passed, int(previous["score"] or 0))
                if already_credited_today
                else passed
            )

            conn.execute(
                "INSERT INTO daily_submissions("
                "user_id,challenge_id,language,status,score,submitted_at"
                ") VALUES(?,?,?,?,?,?) "
                "ON CONFLICT(user_id,challenge_id) DO UPDATE SET "
                "language=excluded.language,"
                "status=excluded.status,"
                "score=excluded.score,"
                "submitted_at=excluded.submitted_at",
                (
                    interaction.user.id,
                    challenge["id"],
                    language.value,
                    stored_status,
                    stored_score,
                    submitted_at,
                ),
            )

            awarded = passed == total and not already_credited_today
            xp_result = None

            if awarded:
                xp_result = _add_xp_in_transaction(
                    conn,
                    interaction.user.id,
                    interaction.user.display_name,
                    75,
                    f"Passed daily challenge: {challenge['title']}",
                    today,
                )

                today_str = today.isoformat()

                conn.execute(
                    "INSERT OR IGNORE INTO daily_goals(user_id,goal_date) "
                    "VALUES(?,?)",
                    (interaction.user.id, today_str),
                )

                conn.execute(
                    "UPDATE daily_goals "
                    "SET challenges=challenges+1 "
                    "WHERE user_id=? AND goal_date=?",
                    (interaction.user.id, today_str),
                )

            return awarded, xp_result

        awarded_xp, xp_result = await db.run_transaction(save_submission)

        if awarded_xp:
            await _publish_xp_result(
                interaction.user.id,
                interaction.guild,
                xp_result,
            )
            await award_badge(
                interaction.user.id,
                "problem_solver",
                interaction.guild,
            )

        if passed == total:
            title = "\U0001f389 Challenge Passed!"
            color = ColorPalette.SUCCESS
        else:
            title = "\U0001f9ea Challenge Results"
            color = ColorPalette.WARNING

        if passed == total:
            outcome_note = (
                "\n\n\U0001f3c6 **+75 XP**"
                if awarded_xp
                else "\n\n\u2705 Already completed today \u2014 "
                "no additional XP for resubmitting the same challenge."
            )
        else:
            outcome_note = "\n\nKeep debugging and submit again!"

        embed = UIEmbeds.standard(
            title,
            f"**{challenge['title']}**\n\n"
            f"**Tests:** {passed}/{total}\n\n"
            + "\n".join(details)
            + outcome_note,
            color,
        )

        await interaction.followup.send(
            embed=embed,
            allowed_mentions=discord.AllowedMentions.none(),
        )


async def setup(bot):
    await bot.add_cog(ChallengesCog(bot))