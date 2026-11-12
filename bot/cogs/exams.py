import io
import logging
import re
from typing import Optional

import discord
from discord.ext import commands
from discord import app_commands

from bot.database import db
from bot.learning.mastery import ensure_user_in_transaction
from bot.ui.embeds import UIEmbeds, ColorPalette

logger = logging.getLogger("ClassCodeBot.exams")

LANGUAGE_CHOICES = [
    app_commands.Choice(name="C++", value="cpp"),
    app_commands.Choice(name="Java", value="java"),
]
DIFFICULTY_CHOICES = [
    app_commands.Choice(name="Beginner", value="beginner"),
    app_commands.Choice(name="Intermediate", value="intermediate"),
    app_commands.Choice(name="Advanced", value="advanced"),
]


def clean_code(content: str) -> str:
    content = content.strip()
    content = re.sub(r"^```(?:cpp|c\+\+|java)?\s*", "", content, flags=re.I)
    content = re.sub(r"\s*```$", "", content)
    return content.strip()



class ExamsCog(commands.Cog):
    """Practical programming exams posted inside an existing Discord Forum Channel.

    ClassCode NEVER creates categories, channels, or forums for exams. An admin
    selects an existing Forum Channel and ClassCode creates exactly one Forum
    Post in that channel. The problem file is attached to the post.
    """

    def __init__(self, bot):
        self.bot = bot
        self._active_exams: dict[int, dict] = {}

    async def cog_load(self):
        rows = await db.fetchall(
            "SELECT * FROM practical_exams WHERE active=1 AND thread_id IS NOT NULL"
        )
        self._active_exams = {int(row["thread_id"]): row for row in rows}

    @staticmethod
    def _is_admin(interaction: discord.Interaction) -> bool:
        member = interaction.user
        return isinstance(member, discord.Member) and (
            member.id == interaction.guild.owner_id
            or member.guild_permissions.administrator
        )

    @staticmethod
    def _admin_channel_ok(interaction: discord.Interaction) -> bool:
        return getattr(interaction.channel, "name", "") == "exam-admin"

    async def _read_attachment(self, attachment: discord.Attachment) -> bytes:
        if attachment.size > 8_000_000:
            raise ValueError("Attachment is too large. Keep the exam problem file under 8 MB.")
        return await attachment.read()

    @staticmethod
    def _decode_problem(data: bytes) -> str:
        try:
            return data.decode("utf-8-sig")
        except UnicodeDecodeError:
            return data.decode("cp1252", errors="replace")

    async def create_exam_post(
        self,
        forum: discord.ForumChannel,
        language: str,
        difficulty: str,
        title: str,
        problem: str,
        problem_bytes: bytes,
        problem_filename: str,
        created_by: int,
        topic: str = "",
        allowed_concepts: str = "",
        starter_code: str = "",
    ):
        """Create one post in an EXISTING forum. Never creates a channel."""
        if not isinstance(forum, discord.ForumChannel):
            raise ValueError("Select an existing Discord Forum Channel.")

        # The PDF is the post attachment. No large problem text is put into
        # Discord content, so the 2,000-character message limit is irrelevant.
        problem_file = discord.File(io.BytesIO(problem_bytes), filename=problem_filename)
        result = await forum.create_thread(
            name=title[:100],
            content=(
                f"**{title[:180]}**\n"
                f"Language: `{language.upper()}`\n"
                f"Difficulty: `{difficulty.title()}`\n\n"
                "📎 The complete exam problem is attached to this post.\n"
                "Submit your complete code in this exam post using `/exam-submit`."
            ),
            file=problem_file,
        )

        # discord.py returns ThreadWithMessage for ForumChannel.create_thread.
        thread = getattr(result, "thread", None)
        message = getattr(result, "message", None)
        if thread is None:
            # Defensive fallback for compatible discord.py versions/mocks.
            thread = result
        if message is None:
            message = getattr(thread, "starter_message", None)

        thread_id = thread.id
        message_id = getattr(message, "id", None)

        try:
            def save_exam(conn):
                ensure_user_in_transaction(conn, created_by, None)
                conn.execute(
                    "INSERT INTO practical_exams(title,language,difficulty,problem,topic,test_cases,allowed_concepts,starter_code,created_by,forum_channel_id,thread_id,exam_channel_id,message_id) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (
                        title, language, difficulty, problem, topic, "[]", allowed_concepts,
                        starter_code, created_by, forum.id, thread_id, forum.id, message_id,
                    ),
                )
            await db.run_transaction(save_exam)
            exam = await db.fetchone(
                "SELECT * FROM practical_exams WHERE thread_id=? AND active=1 ORDER BY exam_id DESC LIMIT 1",
                (thread_id,),
            )
            if exam:
                self._active_exams[thread_id] = exam
        except Exception:
            try:
                await thread.delete(reason="ClassCode could not register the practical exam")
            except discord.HTTPException:
                logger.exception(
                    "Could not remove unregistered exam thread actor_id=%s thread_id=%s",
                    created_by, thread_id,
                )
            raise
        return thread, message

    @app_commands.command(
        name="exam-create",
        description="Create a practical exam post inside an existing Forum Channel.",
    )
    @app_commands.describe(
        language="Exam programming language",
        difficulty="Exam difficulty",
        title="Short exam title",
        problem_file="PDF/TXT/MD file containing the full exam problem and restrictions",
        exam_forum="Existing Discord Forum Channel where the exam post should be created",
        topic="Roadmap topic or skill focus",
        allowed_concepts="Optional comma-separated allowed concepts",
    )
    @app_commands.choices(language=LANGUAGE_CHOICES, difficulty=DIFFICULTY_CHOICES)
    async def exam_create(
        self,
        interaction: discord.Interaction,
        language: app_commands.Choice[str],
        difficulty: app_commands.Choice[str],
        title: str,
        problem_file: discord.Attachment,
        exam_forum: discord.ForumChannel,
        topic: str = "",
        allowed_concepts: str = "",
    ):
        if not self._is_admin(interaction):
            await interaction.response.send_message("❌ Admin access required.", ephemeral=True)
            return
        if not self._admin_channel_ok(interaction):
            await interaction.response.send_message("🔒 Use this command only in `#exam-admin`.", ephemeral=True)
            return

        await interaction.response.defer(ephemeral=True)
        try:
            problem_bytes = await self._read_attachment(problem_file)
            problem = self._decode_problem(problem_bytes)
            thread, message = await self.create_exam_post(
                exam_forum,
                language.value,
                difficulty.value,
                title,
                problem,
                problem_bytes,
                problem_file.filename,
                interaction.user.id,
                topic,
                allowed_concepts,
            )
        except Exception:
            logger.exception("Could not create practical exam post for actor %s", interaction.user.id)
            await interaction.followup.send(
                "❌ Could not create the exam post. Check the bot logs or try again later.",
                ephemeral=True,
            )
            return

        jump_url = getattr(thread, "jump_url", None)
        if not jump_url and message is not None:
            jump_url = getattr(message, "jump_url", None)
        link = f"\n[Open exam post]({jump_url})" if jump_url else ""
        await interaction.followup.send(
            f"✅ Exam post created inside {exam_forum.mention}."
            f"{link}\n📎 The problem file is attached to the forum post.",
            ephemeral=True,
        )

    @app_commands.command(
        name="exam-submit",
        description="Submit exam code by pasting it or uploading a source file.",
    )
    @app_commands.checks.cooldown(1, 30.0, key=lambda interaction: interaction.user.id)
    @app_commands.choices(language=LANGUAGE_CHOICES)
    @app_commands.describe(
        language="The programming language used for this exam",
        code="Optional: paste your complete code here (up to Discord's 6,000-character limit)",
        file="Optional: upload one .cpp/.cc/.cxx or .java source file",
    )
    async def exam_submit(
        self,
        interaction: discord.Interaction,
        language: app_commands.Choice[str],
        code: Optional[str] = None,
        file: Optional[discord.Attachment] = None,
    ):
        channel = interaction.channel
        if not isinstance(channel, discord.Thread):
            await interaction.response.send_message(
                "❌ Use this command inside the ClassCode exam post.", ephemeral=True
            )
            return

        await interaction.response.defer(ephemeral=True, thinking=True)

        exam = await db.fetchone(
            "SELECT * FROM practical_exams WHERE thread_id=? AND active=1 ORDER BY exam_id DESC LIMIT 1",
            (channel.id,),
        )
        if not exam:
            await interaction.followup.send(
                "❌ This is not an active ClassCode practical exam post.", ephemeral=True
            )
            return

        if exam["language"] != language.value:
            await interaction.followup.send(
                f"❌ This exam requires **{exam['language'].upper()}**.", ephemeral=True
            )
            return

        # Students must provide exactly one submission source. Discord slash
        # commands cannot accept an unlimited pasted string, so large programs
        # should be uploaded as .cpp/.java files instead.
        has_code = bool(code and code.strip())
        has_file = file is not None
        if has_code and has_file:
            await interaction.followup.send(
                "❌ Please provide **either pasted code OR a source file**, not both.",
                ephemeral=True,
            )
            return
        if not has_code and not has_file:
            await interaction.followup.send(
                "❌ No code submitted. Paste your code in `code` or upload a `.cpp`/`.java` source file in `file`.",
                ephemeral=True,
            )
            return

        submitted_code = ""
        if has_code:
            submitted_code = clean_code(code or "")
            if not submitted_code:
                await interaction.followup.send(
                    "❌ The pasted code is empty.", ephemeral=True
                )
                return
        else:
            assert file is not None
            filename = file.filename.lower()
            allowed_extensions = (".cpp", ".cc", ".cxx") if language.value == "cpp" else (".java",)
            if not filename.endswith(allowed_extensions):
                allowed = ", ".join(allowed_extensions)
                await interaction.followup.send(
                    f"❌ Invalid source file. This **{language.value.upper()}** exam accepts: `{allowed}`.",
                    ephemeral=True,
                )
                return
            if file.size > 1_000_000:
                await interaction.followup.send(
                    "❌ Source file is too large. Keep it under 1 MB.", ephemeral=True
                )
                return
            try:
                data = await file.read()
                submitted_code = clean_code(self._decode_problem(data))
            except Exception:
                await interaction.followup.send(
                    "❌ I couldn't read that source file. Please upload a valid text-based source file.",
                    ephemeral=True,
                )
                return
            if not submitted_code:
                await interaction.followup.send(
                    "❌ The uploaded source file is empty.", ephemeral=True
                )
                return

        ok, response = await self.store_submission(
            interaction.user.id,
            interaction.user.display_name,
            interaction.guild,
            exam,
            submitted_code,
            channel.id,
        )
        await interaction.followup.send(response, ephemeral=True)

    async def store_submission(
        self, user_id: int, display_name: str, guild: discord.Guild, exam, code: str, thread_id: int
    ):
        if not code or len(code) > 8000:
            return False, "❌ Submit a complete program under 8000 characters."
        def save_submission(conn):
            active = conn.execute(
                "SELECT 1 FROM practical_exams WHERE exam_id=? AND active=1",
                (exam["exam_id"],),
            ).fetchone()
            if not active:
                return False
            ensure_user_in_transaction(conn, user_id, display_name)
            conn.execute(
                "INSERT INTO practical_exam_submissions(exam_id,user_id,thread_id,code,score,passed_tests,total_tests,status,feedback) VALUES(?,?,?,?,?,?,?,?,?)",
                (
                    exam["exam_id"], user_id, thread_id, code, 0, 0, 0,
                    "pending_review", "Awaiting administrator/teacher review.",
                ),
            )
            return True

        if not await db.run_transaction(save_submission):
            return False, "❌ This exam has closed; the submission was not saved."
        return True, "✅ Your code was submitted successfully and is now **pending administrator/teacher review**. No automatic tests are run."

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot or not isinstance(message.channel, discord.Thread):
            return

        # Only registered active exam threads are handled. The cog cache avoids
        # a database lookup for every ordinary message in a thread.
        exam = self._active_exams.get(message.channel.id)
        if not exam:
            return

        code = ""
        if message.attachments:
            attachment = message.attachments[0]
            if attachment.filename.lower().endswith((".cpp", ".cc", ".cxx", ".java", ".txt")) and attachment.size <= 1_000_000:
                try:
                    data = await attachment.read()
                    try:
                        decoded = data.decode("utf-8-sig")
                    except UnicodeDecodeError:
                        decoded = data.decode("cp1252", errors="replace")
                    code = clean_code(decoded)
                except Exception:
                    code = ""

        if not code:
            return
        ok, response = await self.store_submission(
            message.author.id,
            message.author.display_name,
            message.guild,
            exam,
            code,
            message.channel.id,
        )
        await message.channel.send(
            f"<@{message.author.id}> {response}",
            allowed_mentions=discord.AllowedMentions.none(),
        )

    @app_commands.command(name="exam-grade", description="Manually override the latest practical exam score for a student.")
    async def exam_grade(self, interaction: discord.Interaction, student: discord.Member, score: int, feedback: str = ""):
        if not self._is_admin(interaction):
            await interaction.response.send_message("❌ Admin access required.", ephemeral=True)
            return
        if not self._admin_channel_ok(interaction):
            await interaction.response.send_message("🔒 Use this command only in `#exam-admin`.", ephemeral=True)
            return
        score = max(0, min(100, score))
        await interaction.response.defer(ephemeral=True, thinking=True)
        def grade_latest(conn):
            row = conn.execute(
                "SELECT submission_id FROM practical_exam_submissions WHERE user_id=? ORDER BY submission_id DESC LIMIT 1",
                (student.id,),
            ).fetchone()
            if not row:
                return None
            updated = conn.execute(
                "UPDATE practical_exam_submissions SET score=?, status=?, feedback=? WHERE submission_id=? AND user_id=?",
                (score, "manual", feedback, row["submission_id"], student.id),
            )
            return row["submission_id"] if updated.rowcount == 1 else None

        submission_id = await db.run_transaction(grade_latest)
        if submission_id is None:
            await interaction.followup.send("❌ No submission found for that student.", ephemeral=True)
            return
        logger.info(
            "Administrative exam score override actor_id=%s target_id=%s submission_id=%s score=%s",
            interaction.user.id, student.id, submission_id, score,
        )
        await interaction.followup.send(f"✅ Latest exam score for {student.mention} updated to **{score}/100**.", ephemeral=True)

    @app_commands.command(name="exam-results", description="View practical exam submissions.")
    async def exam_results(self, interaction: discord.Interaction):
        if not self._is_admin(interaction):
            await interaction.response.send_message("❌ Admin access required.", ephemeral=True)
            return
        if not self._admin_channel_ok(interaction):
            await interaction.response.send_message("🔒 Use this command only in `#exam-admin`.", ephemeral=True)
            return
        await interaction.response.defer(ephemeral=True, thinking=True)
        rows = await db.fetchall("SELECT s.user_id,s.score,s.status,s.feedback,s.submitted_at,e.title FROM practical_exam_submissions s JOIN practical_exams e ON e.exam_id=s.exam_id ORDER BY s.submission_id DESC LIMIT 20")
        if not rows:
            await interaction.followup.send("No practical exam submissions yet.", ephemeral=True)
            return
        text = "\n".join(f"<@{r['user_id']}> — **{r['title']}** — `{r['score']}/100` — {r['status']}" for r in rows)
        await interaction.followup.send(embed=UIEmbeds.standard("📊 PRACTICAL EXAM RESULTS", text[:3900]), ephemeral=True)

    @app_commands.command(name="exam-close", description="Close an exam forum post so new submissions are not accepted.")
    async def exam_close(self, interaction: discord.Interaction):
        if not self._is_admin(interaction):
            await interaction.response.send_message("❌ Admin access required.", ephemeral=True)
            return
        if not isinstance(interaction.channel, discord.Thread):
            await interaction.response.send_message("❌ Use this inside the ClassCode exam post.", ephemeral=True)
            return
        await interaction.response.defer(ephemeral=False, thinking=True)
        exam = await db.fetchone("SELECT exam_id FROM practical_exams WHERE thread_id=? AND active=1 ORDER BY exam_id DESC LIMIT 1", (interaction.channel.id,))
        if not exam:
            await interaction.followup.send("❌ This is not a ClassCode exam post.", ephemeral=True)
            return
        await db.execute("UPDATE practical_exams SET active=0 WHERE exam_id=?", (exam["exam_id"],))
        self._active_exams.pop(interaction.channel.id, None)
        await interaction.followup.send("🔒 Exam closed. No more submissions will be accepted in this post.")


async def setup(bot):
    await bot.add_cog(ExamsCog(bot))
