import hashlib
from datetime import datetime
import discord
from discord.ext import commands
from discord import app_commands
from bot.database import db
from bot.learning.cpp import CPP_CURRICULUM
from bot.learning.java import JAVA_CURRICULUM
from bot.learning.mastery import get_level_title, xp_for_next_level, BADGES, ensure_user
from bot.ui.embeds import UIEmbeds, ColorPalette


def can_view_profile(actor_id: int, target_id: int, actor_is_admin: bool) -> bool:
    return actor_id == target_id or actor_is_admin


async def language_progress(user_id: int, language: str, curriculum: list[dict]):
    rows = await db.fetchall("SELECT topic_id, status FROM user_progress WHERE user_id = ? AND language = ?", (user_id, language))
    completed = sum(1 for r in rows if r["status"] == "completed")
    total = len(curriculum)
    return completed, total, round((completed / total) * 100) if total else 0


class ProgressCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="profile", description="View your ClassCode profile, mastery, XP, badges, and streak.")
    async def profile(self, interaction: discord.Interaction, user: discord.User = None):
        target = user or interaction.user
        actor_is_admin = (
            isinstance(interaction.user, discord.Member)
            and interaction.user.guild_permissions.administrator
        )
        if not can_view_profile(interaction.user.id, target.id, actor_is_admin):
            await interaction.response.send_message(
                "🔒 You can view your own learning profile only.", ephemeral=True
            )
            return
        await interaction.response.defer(ephemeral=True, thinking=True)
        await ensure_user(target.id, target.display_name)
        row = await db.fetchone("SELECT xp, level, streak_count FROM users WHERE user_id = ?", (target.id,))
        xp, level, streak = row["xp"], row["level"], row["streak_count"]
        next_xp = xp_for_next_level(level)
        cpp_done, cpp_total, cpp_pct = await language_progress(target.id, "cpp", CPP_CURRICULUM)
        java_done, java_total, java_pct = await language_progress(target.id, "java", JAVA_CURRICULUM)
        badge_rows = await db.fetchall("SELECT badge_id FROM user_badges WHERE user_id = ? ORDER BY unlocked_at", (target.id,))
        badges = [BADGES.get(r["badge_id"], r["badge_id"]) for r in badge_rows]

        embed = UIEmbeds.profile(target.display_name, level, get_level_title(level), xp, next_xp, cpp_pct, java_pct, badges)
        embed.add_field(name="\U0001f525 Streak", value=f"**{streak} day(s)**", inline=True)
        embed.add_field(name="\U0001f7e6 C++", value=f"{cpp_done}/{cpp_total} topics", inline=True)
        embed.add_field(name="\u2615 Java", value=f"{java_done}/{java_total} topics", inline=True)
        await interaction.followup.send(embed=embed, ephemeral=True)

    @app_commands.command(name="progress", description="See your detailed roadmap progress.")
    @app_commands.choices(language=[app_commands.Choice(name="C++", value="cpp"), app_commands.Choice(name="Java", value="java")])
    async def progress(self, interaction: discord.Interaction, language: app_commands.Choice[str]):
        await interaction.response.defer(ephemeral=True, thinking=True)
        curriculum = CPP_CURRICULUM if language.value == "cpp" else JAVA_CURRICULUM
        rows = await db.fetchall("SELECT topic_id, status FROM user_progress WHERE user_id = ? AND language = ?", (interaction.user.id, language.value))
        statuses = {r["topic_id"]: r["status"] for r in rows}
        lines = []
        for topic in curriculum:
            icon = "\u2705" if statuses.get(topic["id"]) == "completed" else "\U0001f7e2" if statuses.get(topic["id"]) == "unlocked" else "\U0001f512"
            lines.append(f"{icon} {topic['title']}")
        done = sum(status == "completed" for status in statuses.values())
        embed = UIEmbeds.standard(f"\U0001f4da {language.name} Progress", f"**{done}/{len(curriculum)} topics complete**\n\n" + "\n".join(lines))
        await interaction.followup.send(embed=embed, ephemeral=True)

    @app_commands.command(name="certificate", description="Generate a certificate after completing an entire language track.")
    @app_commands.choices(language=[app_commands.Choice(name="C++ Mastery Track", value="cpp"), app_commands.Choice(name="Java Mastery Track", value="java")])
    async def certificate(self, interaction: discord.Interaction, language: app_commands.Choice[str]):
        await interaction.response.defer(ephemeral=False, thinking=True)
        curriculum = CPP_CURRICULUM if language.value == "cpp" else JAVA_CURRICULUM
        row = await db.fetchone("SELECT COUNT(*) AS count FROM user_progress WHERE user_id = ? AND language = ? AND status = 'completed'", (interaction.user.id, language.value))
        if row["count"] < len(curriculum):
            await interaction.followup.send(f"\U0001f512 Complete all **{len(curriculum)}** {language.name} topics first. You have completed **{row['count']}**.", ephemeral=True)
            return

        cert_hash = hashlib.sha256(f"{interaction.user.id}-{language.value}".encode()).hexdigest()[:12].upper()
        cert_id = f"CC-CERT-{cert_hash}"
        await db.execute("INSERT OR IGNORE INTO certificates (certificate_id, user_id, language) VALUES (?, ?, ?)", (cert_id, interaction.user.id, language.value))
        certificate = await db.fetchone(
            "SELECT issued_at FROM certificates WHERE certificate_id = ?",
            (cert_id,),
        )
        issued_at = certificate["issued_at"]
        if isinstance(issued_at, str):
            issued_at = datetime.fromisoformat(issued_at)
        embed = discord.Embed(title="\U0001f4dc CERTIFICATE OF PRACTICAL MASTERY", description=f"This certifies that\n\n### \U0001f393 **{interaction.user.display_name}**\n\nhas completed the **{language.name.upper()}** ClassCode learning track.", color=discord.Color.gold())
        embed.add_field(
            name="\U0001f4c5 Issue Date",
            value=issued_at.strftime("%B %d, %Y") if issued_at else "Unavailable",
            inline=True,
        )
        embed.add_field(name="\U0001f511 Verification ID", value=f"`{cert_id}`", inline=True)
        embed.set_footer(text="ClassCode Educational Platform")
        await interaction.followup.send(embed=embed)

async def setup(bot):
    await bot.add_cog(ProgressCog(bot))
