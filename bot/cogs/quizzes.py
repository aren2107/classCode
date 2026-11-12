"""Private, lesson-aware five-question practice quizzes."""
from __future__ import annotations

import logging
import random
import time
import asyncio
from datetime import date

from bot.timezone import manila_today

import discord
from discord.ext import commands
from discord import app_commands

from bot.database import db
from bot.learning.mastery import (
    _add_xp_in_transaction,
    _record_goal_in_transaction,
    award_badge,
    ensure_user_in_transaction,
)
from bot.learning.progress import sync_progress
from bot.ui.lesson import curriculum_for, lesson_questions
from bot.ui.embeds import UIEmbeds, ColorPalette

logger = logging.getLogger("ClassCodeBot.quizzes")
QUIZ_COOLDOWN_SECONDS = 20
PRACTICE_QUIZ_XP_REWARD = 50
_user_cooldowns: dict[tuple[int, str], float] = {}


def _lesson_for_status(curriculum: list[dict], statuses: dict[str, str]) -> dict | None:
    # Practice the earliest lesson that is available but not yet completed.
    return next((topic for topic in curriculum if statuses.get(topic["id"]) == "unlocked"), None)


def _save_practice_quiz_in_transaction(conn, user_id: int, username: str, language: str, topic_id: str, score: int, today: date):
    if isinstance(score, bool) or not isinstance(score, int) or not 0 <= score <= 5:
        raise ValueError("Practice quiz score must be between 0 and 5.")
    passed = score >= 4
    ensure_user_in_transaction(conn, user_id, username)
    conn.execute(
        "INSERT INTO quiz_attempts (user_id, language, topic_id, difficulty, score, total, passed) VALUES (?, ?, ?, ?, ?, 5, ?)",
        (user_id, language, topic_id, "lesson-practice", score, int(passed)),
    )
    _record_goal_in_transaction(conn, user_id, "quiz", today)
    if passed:
        claimed = conn.execute(
            "INSERT INTO practice_quiz_xp_rewards "
            "(user_id, language, topic_id, xp_awarded) VALUES (?, ?, ?, ?) "
            "ON CONFLICT(user_id, language, topic_id) DO NOTHING",
            (user_id, language, topic_id, PRACTICE_QUIZ_XP_REWARD),
        ).rowcount == 1
        if not claimed:
            return None
        return _add_xp_in_transaction(
            conn, user_id, username, PRACTICE_QUIZ_XP_REWARD,
            f"Passed {language.upper()} lesson practice quiz [{language}:{topic_id}]", today,
        )
    return None


def _answer_is_current(answer_index: int, current_index: int, finished: bool) -> bool:
    return not finished and answer_index == current_index


class LessonPracticeView(discord.ui.View):
    """Five questions sourced from the learner's current curriculum lesson.

    Quiz messages are ephemeral, and the owner guard also protects component
    callbacks against copied/stale interactions.
    """
    def __init__(self, owner_id: int, language: str, topic: dict, questions=None):
        super().__init__(timeout=600)
        self.owner_id = owner_id
        self.language = language
        self.topic = topic
        self.questions = questions if questions is not None else lesson_questions(topic, language)
        self.questions = [dict(q, options=list(q["options"])) for q in self.questions[:5]]
        self._shuffle_options()
        self.index = 0
        self.score = 0
        self.finished = False
        self._answer_lock = asyncio.Lock()
        self._render()

    def _shuffle_options(self):
        rng = random.SystemRandom()
        for q in self.questions:
            correct_text = q["options"][q["answer"]]
            rng.shuffle(q["options"])
            q["answer"] = q["options"].index(correct_text)

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id != self.owner_id:
            await interaction.response.send_message(
                "🔒 This is another student's private quiz. Start `/cpp-quiz` or `/java-quiz` to get your own.",
                ephemeral=True,
            )
            return False
        if self.finished:
            await interaction.response.send_message("This quiz has already finished. Start a new quiz when you're ready.", ephemeral=True)
            return False
        return True

    def _render(self):
        self.clear_items()
        q = self.questions[self.index]
        question_index = self.index
        for i, label in enumerate("ABCD"):
            button = discord.ui.Button(label=label, style=discord.ButtonStyle.secondary, row=0)
            async def callback(interaction: discord.Interaction, selected=i):
                await self._answer(interaction, selected, question_index)
            button.callback = callback
            self.add_item(button)

    def _embed(self, feedback: str = ""):
        q = self.questions[self.index]
        description = f"**Question {self.index + 1}/5**\n{q['question']}\n\n" + "\n".join(
            f"**{'ABCD'[i]}.** {option}" for i, option in enumerate(q["options"])
        )
        if feedback:
            description = feedback + "\n\n" + description
        return UIEmbeds.standard(f"🧠 {self.language.upper()} • {self.topic['title']}", description, ColorPalette.PRIMARY)

    async def _answer(self, interaction: discord.Interaction, selected: int, question_index: int):
        await interaction.response.defer()
        async with self._answer_lock:
            if not _answer_is_current(question_index, self.index, self.finished):
                await interaction.followup.send(
                    "That answer was already recorded or the quiz moved to its next question.",
                    ephemeral=True,
                )
                return

            q = self.questions[self.index]
            correct = selected == q["answer"]
            if correct:
                self.score += 1
                feedback = f"✅ Correct. {q.get('explanation', 'Good work — keep applying the lesson concept.')}"
            else:
                feedback = f"❌ Not quite. Correct answer: **{'ABCD'[q['answer']]}. {q['options'][q['answer']]}**. {q.get('explanation', 'Review this concept in the lesson before trying again.')}"

            self.index += 1
            if self.index < len(self.questions):
                self._render()
                await interaction.edit_original_response(embed=self._embed(feedback), view=self)
                return

            self.finished = True
            self.clear_items()
            passed = self.score >= 4
            saved = False
            reward_result = None
            try:
                today = manila_today()

                reward_result = await db.run_transaction(
                    lambda conn: _save_practice_quiz_in_transaction(
                        conn, interaction.user.id, interaction.user.display_name,
                        self.language, self.topic["id"], self.score, today,
                    )
                )
                saved = True
            except Exception as exc:
                logger.warning(
                    "Could not save quiz result for user %s (%s)",
                    interaction.user.id, type(exc).__name__,
                )

            if saved and passed:
                try:
                    await award_badge(interaction.user.id, "first_steps", interaction.guild)
                except Exception:
                    logger.exception("Could not award quiz badge for user %s", interaction.user.id)

        if not saved:
            message = (
                f"**Score: {self.score}/5**\n\n"
                "I couldn't save this quiz result, so it is not recorded and no XP reward is confirmed. "
                "Please try again later."
            )
            embed = UIEmbeds.standard("⚠️ Quiz result not saved", message, ColorPalette.WARNING)
            await interaction.edit_original_response(embed=embed, view=self)
            return

        if passed:
            reward_note = (
                "You earned the one-time 50 XP practice reward for this topic. "
                if reward_result is not None
                else "The one-time practice XP reward for this topic was already claimed; this attempt is still recorded. "
            )
            message = (f"**Score: {self.score}/5 (passed)**\n\nGreat work! You passed this quiz on **{self.topic['title']}**. "
                       f"{reward_note}"
                       "A new attempt will draw a different mix of questions from this same roadmap lesson. "
                       "Quiz results do not automatically complete the lesson; use the lesson's Mastery Check for that.")
            retry = discord.ui.Button(label="Try another quiz on this lesson", style=discord.ButtonStyle.success)
            async def retry_callback(retry_interaction: discord.Interaction):
                if retry_interaction.user.id != self.owner_id:
                    await retry_interaction.response.send_message("🔒 This quiz belongs to another student.", ephemeral=True)
                    return
                retry_view = LessonPracticeView(self.owner_id, self.language, self.topic)
                await retry_interaction.response.edit_message(embed=retry_view._embed(), view=retry_view)
            retry.callback = retry_callback
            self.add_item(retry)
            embed = UIEmbeds.standard("🏆 Quiz complete", message, ColorPalette.SUCCESS)
        else:
            message = (f"**Score: {self.score}/5** — you need **4/5** to pass.\n\n"
                       f"Review **{self.topic['title']}**, especially the questions you missed, then try another quiz on this same lesson.")
            retry = discord.ui.Button(label="Retry this lesson", style=discord.ButtonStyle.primary)
            async def retry_callback(retry_interaction: discord.Interaction):
                if retry_interaction.user.id != self.owner_id:
                    await retry_interaction.response.send_message("🔒 This quiz belongs to another student.", ephemeral=True)
                    return
                retry_view = LessonPracticeView(self.owner_id, self.language, self.topic)
                await retry_interaction.response.edit_message(embed=retry_view._embed(), view=retry_view)
            retry.callback = retry_callback
            self.add_item(retry)
            embed = UIEmbeds.standard("🔁 Keep practicing", message, ColorPalette.WARNING)
        await interaction.edit_original_response(embed=embed, view=self)

    async def on_timeout(self):
        for item in self.children:
            item.disabled = True


class QuizzesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def start_quiz(self, interaction: discord.Interaction, language: str):
        now = time.monotonic()
        key = (interaction.user.id, language)
        remaining = QUIZ_COOLDOWN_SECONDS - (now - _user_cooldowns.get(key, 0.0))
        if remaining > 0:
            await interaction.response.send_message(
                f"⏳ Please wait **{int(remaining) + 1} seconds** before starting another {language.upper()} quiz.",
                ephemeral=True,
            )
            return
        _user_cooldowns[key] = now
        # Acknowledge immediately; progress/database reads can exceed Discord's
        # initial interaction-response window on a busy or cold server.
        await interaction.response.defer(ephemeral=True, thinking=True)
        try:
            curriculum = curriculum_for(language)
            statuses = await sync_progress(interaction.user.id, language)
            assignment = await db.fetchone(
                "SELECT body FROM personal_notes WHERE user_id=? AND title=? ORDER BY note_id DESC LIMIT 1",
                (interaction.user.id, f"ClassCode Assigned Lesson {language.upper()}"),
            )
            assigned_id = (assignment["body"] or "").strip() if assignment else ""
            topic = next((t for t in curriculum if t["id"] == assigned_id), None)
            if topic is None:
                topic = _lesson_for_status(curriculum, statuses)
            if topic is None:
                topic = next((t for t in curriculum if statuses.get(t["id"]) != "completed"), curriculum[-1])
            questions = lesson_questions(topic, language)
            view = LessonPracticeView(interaction.user.id, language, topic, questions)
            await interaction.followup.send(embed=view._embed(), view=view, ephemeral=True)
        except Exception:
            logger.exception("Failed to start %s quiz for user %s", language, interaction.user.id)
            try:
                await interaction.followup.send(
                    "⚠️ I couldn't start your quiz just now. Please try again shortly. If it keeps happening, let an admin know.",
                    ephemeral=True,
                )
            except discord.HTTPException:
                logger.warning("Could not send quiz-start error response for user %s", interaction.user.id, exc_info=True)

    @app_commands.command(name="cpp-quiz", description="Take a private, lesson-aware C++ quiz.")
    async def cpp_quiz(self, interaction: discord.Interaction):
        await self.start_quiz(interaction, "cpp")

    @app_commands.command(name="java-quiz", description="Take a private, lesson-aware Java quiz.")
    async def java_quiz(self, interaction: discord.Interaction):
        await self.start_quiz(interaction, "java")

    


async def setup(bot):
    await bot.add_cog(QuizzesCog(bot))
