
import discord
from discord.ext import commands
from discord import app_commands
import logging
import time
from bot.config import Config

logger = logging.getLogger("ClassCodeBot")


class ClassCodeCommandTree(app_commands.CommandTree):
    """Apply channel routing before a slash command's callback runs."""
    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        checker = getattr(self.client, "check_command_channel", None)
        if checker is None:
            return True
        return await checker(interaction)


class ClassCodeBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True

        super().__init__(
            command_prefix="!",
            intents=intents,
            help_command=None,
            tree_cls=ClassCodeCommandTree,
        )
        self.started_at = time.monotonic()

        self.tree.error(self.handle_app_command_error)

    async def check_command_channel(self, interaction: discord.Interaction) -> bool:
        """Keep commands in their intended channels and give a clear private hint."""
        command = interaction.command
        channel = interaction.channel
        if command is None or interaction.guild is None or channel is None:
            return True

        name = command.name.lower()
        namespace = getattr(interaction, "namespace", None)
        language_value = getattr(namespace, "language", "") or ""
        language = str(getattr(language_value, "value", language_value)).lower()

        # Commands that must run in the context of a practical-exam thread are
        # intentionally not forced into #bot-commands.
        context_commands = {"exam-submit", "exam-grade", "exam-results", "exam-close"}
        if name in context_commands:
            return True

        exact_channels = {
            "start": "how-to-start",
            "questionnaire": "questionnaire",
            "cpp-quiz": "cpp-quiz",
            "java-quiz": "java-quiz",
            "attendance": "attendance",
            "cpp-roadmap": "cpp-roadmap",
            "java-roadmap": "java-roadmap",
            "daily-challenge": "daily-challenge",
            "submit-challenge": "daily-challenge",
            "leaderboard": "leaderboard",
            "xp-history": "leaderboard",
            "projects": "project-ideas",
            "project": "project-ideas",
            "project-complete": "project-ideas",
            "portfolio": "projects-showcase",
            "portfolio-add": "projects-showcase",
            "study-group-create": "general",
            "study-group-join": "general",
            "study-groups": "general",
        }
        expected = exact_channels.get(name)
        expected_channels = None

        # Commands with a language option go to the matching help/review area.
        if name == "code-review":
            expected = f"{language}-code-review" if language in {"cpp", "java"} else "bot-commands"
        elif name in {"explain", "explain-code"}:
            expected = f"{language}-help" if language in {"cpp", "java"} else "bot-commands"
        elif name in {"hint", "explain-error", "debug"}:
            # These commands do not all ask for a language, so accept either
            # language's help channel rather than forcing students into one.
            expected_channels = {"cpp-help", "java-help"}
        elif name == "review" or name == "next-lesson":
            expected = f"{language}-roadmap" if language in {"cpp", "java"} else "bot-commands"
        elif name == "save-snippet":
            expected = f"{language}-help" if language in {"cpp", "java"} else "bot-commands"

        # The main command center is the safe default for general, progress,
        # placement, admin, class-management, and other unassigned commands.
        if expected_channels is None:
            expected_channels = {expected or "bot-commands"}

        current_name = getattr(channel, "name", "")
        # For forum/thread contexts, allow a command in a thread whose parent
        # forum is the intended destination.
        parent = getattr(channel, "parent", None)
        allowed = current_name in expected_channels or getattr(parent, "name", None) in expected_channels
        if allowed:
            return True

        command_text = f"/{command.qualified_name}"
        if len(expected_channels) == 1:
            expected_text = f"**#{next(iter(expected_channels))}**"
        else:
            expected_text = " or ".join(f"**#{name}**" for name in sorted(expected_channels))
        await interaction.response.send_message(
            f"📍 Please use `{command_text}` in {expected_text} to run this command.",
            ephemeral=True,
        )
        return False

    async def handle_app_command_error(
        self,
        interaction: discord.Interaction,
        error: app_commands.AppCommandError,
    ):
        command_name = (
            interaction.command.qualified_name
            if interaction.command
            else "unknown"
        )

        if isinstance(error, app_commands.CommandOnCooldown):
            logger.info(
                "Slash command cooldown command=%s user_id=%s retry_after=%.1f",
                command_name, interaction.user.id, error.retry_after,
            )
            message = f"Please wait {error.retry_after:.0f} seconds before using this command again."
        elif isinstance(error, app_commands.MissingPermissions):
            logger.warning(
                "Slash command permission denied command=%s user_id=%s guild_id=%s",
                command_name, interaction.user.id,
                interaction.guild.id if interaction.guild else None,
            )
            message = "⛔ You do not have permission to use this command."
        else:
            logger.error(
                "Slash command '%s' failed for user %s",
                command_name,
                interaction.user.id,
                exc_info=(type(error), error, error.__traceback__),
            )
            message = "⚠️ Something went wrong. Please try again shortly."

        try:
            if interaction.response.is_done():
                await interaction.followup.send(
                    message,
                    ephemeral=True
                )
            else:
                await interaction.response.send_message(
                    message,
                    ephemeral=True
                )
        except discord.NotFound:
            # Discord returns 10062 when the interaction token has expired.
            # At that point there is no valid response/follow-up to send.
            logger.warning(
                "Interaction expired before an error response could be sent for '%s'",
                command_name,
            )
        except discord.HTTPException:
            logger.warning(
                "Could not send error response for slash command '%s'",
                command_name,
                exc_info=True,
            )

    async def setup_hook(self):
        from bot.cogs.admin import VerifyView
        from bot.ui.views import TopicSelectView
        from bot.learning.cpp import CPP_CURRICULUM
        from bot.learning.java import JAVA_CURRICULUM
        from bot.cogs.academy import QuestionnaireView
        from bot.cogs.tickets import TicketPanelView, TicketControlsView

        self.add_view(VerifyView())

        for language, curriculum in (
            ("cpp", CPP_CURRICULUM),
            ("java", JAVA_CURRICULUM),
        ):
            pages = max(
                1,
                (
                    len(curriculum) + TopicSelectView.PAGE_SIZE - 1
                ) // TopicSelectView.PAGE_SIZE
            )

            for page in range(pages):
                self.add_view(TopicSelectView(language, page))

        self.add_view(QuestionnaireView())
        self.add_view(TicketPanelView())
        self.add_view(TicketControlsView())

        initial_extensions = [
            "bot.cogs.admin",
            "bot.cogs.learning",
            "bot.cogs.quizzes",
            "bot.cogs.progress",
            "bot.cogs.attendance",
            "bot.cogs.code_review",
            "bot.cogs.challenges",
            "bot.cogs.community",
            "bot.cogs.dashboard",
            "bot.cogs.projects",
            "bot.cogs.classes",
            "bot.cogs.academy",
            "bot.cogs.exams",
            "bot.cogs.tickets",
        ]

        for ext in initial_extensions:
            try:
                await self.load_extension(ext)
                logger.info("Loaded extension: %s", ext)
            except Exception:
                logger.exception(
                    "Failed to load required extension: %s",
                    ext
                )
                raise

        if Config.GUILD_ID:
            guild = discord.Object(id=Config.GUILD_ID)
            self.tree.copy_global_to(guild=guild)
            await self.tree.sync(guild=guild)
            logger.info(
                "Synced commands to guild %s",
                Config.GUILD_ID
            )
        else:
            await self.tree.sync()
            logger.info("Synced global commands.")

    async def on_ready(self):
        uptime_seconds = int(time.monotonic() - self.started_at)
        logger.info(
            "Bot ready user=%s user_id=%s uptime_seconds=%s",
            self.user,
            self.user.id,
            uptime_seconds,
        )

        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name="students master C++ & Java 💻"
            )
        )

    async def close(self):
        logger.info("ClassCode bot shutdown requested")
        await super().close()
