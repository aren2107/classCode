import discord
from discord.ext import commands
from discord import app_commands

from bot.database import db
from bot.ui.embeds import UIEmbeds


class CommunityCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="xp-history", description="View your recent XP activity.")
    async def xp_history(self, interaction: discord.Interaction):
        # Acknowledge before querying the database; Discord's initial response
        # window is short, especially on a cold or slow database connection.
        await interaction.response.defer(ephemeral=True, thinking=True)
        rows = await db.fetchall(
            "SELECT amount, reason, created_at FROM xp_history WHERE user_id = ? ORDER BY id DESC LIMIT 10",
            (interaction.user.id,),
        )
        desc = "\\n".join(
            f"`+{r['amount']} XP` — {r['reason']}" for r in rows
        ) or "No XP activity yet."
        await interaction.followup.send(
            embed=UIEmbeds.standard("📜 XP HISTORY", desc),
            ephemeral=True,
        )

    @app_commands.command(name="leaderboard", description="Display the ClassCode XP leaderboard.")
    async def leaderboard(self, interaction: discord.Interaction):
        # Defer before the Supabase query so the interaction token stays valid.
        await interaction.response.defer(thinking=True)
        top_users = await db.fetchall(
            "SELECT username, xp, level, streak_count FROM users ORDER BY xp DESC LIMIT 10"
        )
        if not top_users:
            desc = "No students have earned XP yet. Start a lesson or quiz!"
        else:
            desc = "\\n".join(
                f"**{i}. {u['username']}** — Level {u['level']} • `{u['xp']} XP` • 🔥 {u['streak_count']}"
                for i, u in enumerate(top_users, 1)
            )
        await interaction.followup.send(
            embed=UIEmbeds.standard("🏆 CLASSCODE LEADERBOARD", desc)
        )


async def setup(bot):
    await bot.add_cog(CommunityCog(bot))
