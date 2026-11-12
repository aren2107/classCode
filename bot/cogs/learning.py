import discord
from discord.ext import commands
from discord import app_commands
from bot.learning.cpp import CPP_CURRICULUM
from bot.learning.progress import get_review_recommendations
from bot.learning.java import JAVA_CURRICULUM
from bot.ui.views import TopicSelectView
from bot.ui.lesson import open_lesson, curriculum_for, sync_progress
from bot.ui.embeds import UIEmbeds


class LearningCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="cpp-roadmap", description="View the C++ learning progression roadmap.")
    async def cpp_roadmap(self, interaction: discord.Interaction):
        embed = UIEmbeds.standard(
            "\U0001f7e6 C++ Practical Mastery Roadmap",
            "Choose a lesson to open the full **6-step lesson experience**: Overview \u2192 Learn \u2192 Example \u2192 Practice \u2192 Mastery Check \u2192 Complete.\n\n"
            "Step 1: choose the unlocked lesson. Step 2: follow the **🧭 Step-by-step** message inside the lesson; it tells you exactly which button to click next."
        )
        await interaction.response.send_message(embed=embed, view=TopicSelectView("cpp"))

    @app_commands.command(name="java-roadmap", description="View the Java learning progression roadmap.")
    async def java_roadmap(self, interaction: discord.Interaction):
        embed = UIEmbeds.standard(
            "\u2615 Java Practical Mastery Roadmap",
            "Choose a lesson to open the full **6-step lesson experience**: Overview \u2192 Learn \u2192 Example \u2192 Practice \u2192 Mastery Check \u2192 Complete.\n\n"
            "Step 1: choose the unlocked lesson. Step 2: follow the **🧭 Step-by-step** message inside the lesson; it tells you exactly which button to click next."
        )
        await interaction.response.send_message(embed=embed, view=TopicSelectView("java"))


    @app_commands.command(name="review", description="Show lessons you should review based on your mastery scores.")
    @app_commands.choices(language=[
        app_commands.Choice(name="All", value="all"),
        app_commands.Choice(name="C++", value="cpp"),
        app_commands.Choice(name="Java", value="java"),
    ])
    async def review(self, interaction: discord.Interaction, language: app_commands.Choice[str]):
        lang = None if language.value == "all" else language.value
        recommendations = await get_review_recommendations(interaction.user.id, lang, limit=5)
        if not recommendations:
            await interaction.response.send_message(
                "📚 **No review lessons yet.** Finish a few lessons first; ClassCode will recommend topics where your mastery score was 3/5 or lower.",
                ephemeral=True,
            )
            return
        lines = ["**Start with the first item, then work downward.**"]
        for idx, item in enumerate(recommendations, 1):
            topic = item["topic"]
            label = "C++" if item["language"] == "cpp" else "Java"
            lines.append(f"**{idx}. {label} — Lesson {topic['title']}**\n   🧠 Best: **{item['best_score']}/5** • Last: **{item.get('last_score', item['best_score'])}/5** • Attempts: {item['attempts']}\n   🔎 Weak skills: **{item.get('weak_categories') or 'none recorded'}**\n   🔄 Review due: **{item.get('review_due_at') or 'scheduled later'}**\n   ➡️ Run `/{'cpp-roadmap' if item['language']=='cpp' else 'java-roadmap'}` and open this lesson.")
        await interaction.response.send_message(
            embed=UIEmbeds.standard("🔄 CLASSCODE REVIEW PLAN", "\n\n".join(lines)),
            ephemeral=True,
        )

    @app_commands.command(name="next-lesson", description="Open your next unlocked lesson.")
    @app_commands.choices(language=[
        app_commands.Choice(name="C++", value="cpp"),
        app_commands.Choice(name="Java", value="java")
    ])
    async def next_lesson(self, interaction: discord.Interaction, language: app_commands.Choice[str]):
        await interaction.response.defer(ephemeral=True, thinking=True)
        curriculum = curriculum_for(language.value)
        statuses = await sync_progress(interaction.user.id, language.value)
        topic = next((t for t in curriculum if statuses.get(t["id"]) == "unlocked"), None)
        if topic:
            await open_lesson(interaction, language.value, topic["id"])
            return
        if all(statuses.get(t["id"]) == "completed" for t in curriculum):
            await interaction.edit_original_response(
                content=f"\U0001f3c6 You completed the entire {language.name} track! Use `/certificate` when you are ready.",
                embed=None,
                view=None,
            )
            return
        await interaction.edit_original_response(
            content="\U0001f512 Your next lesson is still locked. Complete the earlier lesson first.",
            embed=None,
            view=None,
        )


async def setup(bot):
    await bot.add_cog(LearningCog(bot))
