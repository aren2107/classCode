import discord
from discord.ext import commands
from discord import app_commands
from bot.database import db
from bot.learning.cpp import CPP_CURRICULUM
from bot.learning.java import JAVA_CURRICULUM
from bot.learning.mastery import ensure_user, get_level_title, xp_for_next_level
from bot.ui.embeds import UIEmbeds
from bot.ui.lesson import open_lesson, curriculum_for, sync_progress

class DashboardView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=300)

    @discord.ui.button(label="\U0001f4da Learn", style=discord.ButtonStyle.primary)
    async def learn(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("\U0001f4da Use `/next-lesson` to open the next unlocked lesson, or `/cpp-roadmap` / `/java-roadmap` to browse the full track.", ephemeral=True)

    @discord.ui.button(label="\U0001f4bb Practice", style=discord.ButtonStyle.success)
    async def practice(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Practice with `/cpp-quiz`, `/java-quiz`, or `/daily-challenge`.", ephemeral=True)

    @discord.ui.button(label="\U0001f916 AI Tutor", style=discord.ButtonStyle.secondary)
    async def tutor(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Try `/hint`, `/explain`, or `/code-review` when you're stuck.", ephemeral=True)

    @discord.ui.button(label="\U0001f3c6 Profile", style=discord.ButtonStyle.secondary)
    async def profile(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Open `/profile` for your full stats and badges.", ephemeral=True)



class StartView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=600)

    async def _questionnaire(self, user_id: int):
        row = await db.fetchone("SELECT body FROM personal_notes WHERE user_id=? AND title='ClassCode Questionnaire' ORDER BY note_id DESC LIMIT 1", (user_id,))
        if not row:
            return {}
        result = {}
        for line in row["body"].splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                result[key.strip().lower()] = value.strip().lower()
        return result

    async def _recommended(self, interaction: discord.Interaction):
        # Acknowledge the component immediately; questionnaire/progress queries may take >3 seconds.
        if not interaction.response.is_done():
            await interaction.response.defer(ephemeral=True, thinking=True)
        answers = await self._questionnaire(interaction.user.id)
        language = answers.get("language", "cpp")
        if language == "both":
            language = "cpp"
        if language not in ("cpp", "java"):
            language = "cpp"
        experience = answers.get("experience", answers.get("level", "beginner"))
        if experience in ("intermediate", "advanced"):
            placement = await db.fetchone(
                "SELECT body FROM personal_notes WHERE user_id=? AND title=? ORDER BY note_id DESC LIMIT 1",
                (interaction.user.id, f"ClassCode Placement {language.upper()}"),
            )
            if not placement:
                await interaction.edit_original_response(
                    content=f"\U0001f9ed Your profile says **{experience.title()}**. Take `/placement` for {language.upper()} first so ClassCode can recommend the right starting stage instead of making you repeat beginner material.",
                    embed=None,
                    view=None,
                )
                return
        curriculum = curriculum_for(language)
        statuses = await sync_progress(interaction.user.id, language)
        topic = next((t for t in curriculum if statuses.get(t["id"]) == "unlocked"), curriculum[0])
        await open_lesson(interaction, language, topic["id"])

    @discord.ui.button(label="\U0001f680 Recommended Lesson", style=discord.ButtonStyle.primary, row=0)
    async def recommended(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self._recommended(interaction)

    @discord.ui.button(label="\U0001f7e6 C++", style=discord.ButtonStyle.primary, row=0)
    async def cpp(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True, thinking=True)
        statuses = await sync_progress(interaction.user.id, "cpp")
        topic = next((t for t in CPP_CURRICULUM if statuses.get(t["id"]) == "unlocked"), CPP_CURRICULUM[0])
        await open_lesson(interaction, "cpp", topic["id"])

    @discord.ui.button(label="\u2615 Java", style=discord.ButtonStyle.primary, row=0)
    async def java(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True, thinking=True)
        statuses = await sync_progress(interaction.user.id, "java")
        topic = next((t for t in JAVA_CURRICULUM if statuses.get(t["id"]) == "unlocked"), JAVA_CURRICULUM[0])
        await open_lesson(interaction, "java", topic["id"])

    @discord.ui.button(label="\U0001f9ea Practice", style=discord.ButtonStyle.success, row=1)
    async def practice(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("\U0001f9ea **Practice:** use `Review My Code` in your lesson, then try the matching quiz after your lesson.", ephemeral=True)

    @discord.ui.button(label="\U0001f198 I\u2019m stuck", style=discord.ButtonStyle.secondary, row=1)
    async def stuck(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("\U0001f198 That's normal. Use `/hint` for a clue, `/explain` for a simpler explanation, `/explain-error` for compiler errors, or open a support ticket when you need human help.", ephemeral=True)


class DashboardCog(commands.Cog):
    def __init__(self, bot): self.bot=bot

    async def build(self, user):
        await ensure_user(user.id,user.display_name)
        row=await db.fetchone("SELECT xp,level,streak_count FROM users WHERE user_id=?",(user.id,))
        xp,level,streak=row["xp"],row["level"],row["streak_count"]
        values={}
        for lang,curr in (("cpp",CPP_CURRICULUM),("java",JAVA_CURRICULUM)):
            r=await db.fetchone("SELECT COUNT(*) c FROM user_progress WHERE user_id=? AND language=? AND status='completed'",(user.id,lang))
            values[lang]=(r["c"],len(curr))
        goal=await db.fetchone("SELECT lessons,quizzes,challenges,xp_earned FROM daily_goals WHERE user_id=? AND goal_date=date('now')",(user.id,))
        g=goal or {"lessons":0,"quizzes":0,"challenges":0,"xp_earned":0}
        desc=(f"**Level {level} \u2014 {get_level_title(level)}**\n\u2b50 `{xp} XP` \u2022 \U0001f525 `{streak} day streak`\n\n"
              f"\U0001f7e6 **C++** `{values['cpp'][0]}/{values['cpp'][1]}`\n\u2615 **Java** `{values['java'][0]}/{values['java'][1]}`\n\n"
              f"\U0001f3af **Today's activity**\nLessons: `{g['lessons']}` \u2022 Quizzes: `{g['quizzes']}` \u2022 Challenges: `{g['challenges']}`\nXP today: `{g['xp_earned']}`")
        return UIEmbeds.standard(f"\U0001f393 CLASSCODE DASHBOARD \u2014 {user.display_name}",desc)


    @app_commands.command(name="start", description="Start your personalized ClassCode learning path.")
    async def start(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True, thinking=True)
        await ensure_user(interaction.user.id, interaction.user.display_name)
        row = await db.fetchone("SELECT body FROM personal_notes WHERE user_id=? AND title='ClassCode Questionnaire' ORDER BY note_id DESC LIMIT 1", (interaction.user.id,))
        answers = {}
        if row:
            for line in row["body"].splitlines():
                if ":" in line:
                    key, value = line.split(":", 1)
                    answers[key.strip().lower()] = value.strip()
        language = answers.get("language", "Not completed")
        experience = answers.get("experience", "Not completed")
        goal = answers.get("goal", "Not completed")
        lang_key = language.lower()
        goal_key = goal.lower()
        level_key = experience.lower()
        if lang_key == "both":
            track = "C++ first, then Java"
        elif lang_key in ("cpp", "java"):
            track = "C++" if lang_key == "cpp" else "Java"
        else:
            track = "your chosen language"
        if lang_key not in ("cpp", "java", "both"):
            recommendation = "Complete `#questionnaire` first so ClassCode can personalize your starting point."
        elif goal_key == "pass practical exams":
            recommendation = f"Follow the **{track}** foundation lessons carefully, then move into validation, problem solving, and practical-exam readiness."
        elif goal_key == "build projects":
            recommendation = f"Build your **{track}** fundamentals first, then use projects to combine multiple concepts."
        elif goal_key == "prepare for a career":
            recommendation = f"Start with the **{track}** fundamentals and focus on writing readable, testable code as you progress."
        elif level_key == "advanced":
            recommendation = f"Use the **{track}** roadmap to identify gaps, then spend extra time on practical problem solving and projects."
        elif level_key == "intermediate":
            recommendation = f"Use the **{track}** roadmap to review the foundations and continue into functions, collections, OOP, and problem solving."
        else:
            recommendation = f"Start with **{track} Lesson 1** and follow the lessons in order."
        embed = UIEmbeds.standard(
            "\U0001f680 YOUR CLASSCODE START",
            "A good learning session is simple: **learn \u2192 see an example \u2192 practice \u2192 prove mastery \u2192 complete the lesson.**\n\n"
            f"**\U0001f3af Your profile**\nLanguage: **{language}**\nExperience: **{experience}**\nGoal: **{goal}**\n\n"
            f"**\U0001f4cd Recommendation**\n{recommendation}\n\n"
            "You do not need to finish everything today. One lesson understood well is better than rushing through ten."
        )
        embed.add_field(name="\U0001f4da What you will do", value="1\ufe0f\u20e3 Open the recommended lesson\n2\ufe0f\u20e3 Read the explanation\n3\ufe0f\u20e3 Study the code example\n4\ufe0f\u20e3 Try the practice task\n5\ufe0f\u20e3 Complete the self-check\n6\ufe0f\u20e3 Mark the lesson complete to unlock the next one", inline=False)
        embed.add_field(name="\U0001f198 Need help?", value="`/hint` \u2022 `/explain` \u2022 `/explain-error` \u2022 \U0001f3ab Support Ticket", inline=False)
        await interaction.followup.send(embed=embed, view=StartView(), ephemeral=True)

    @app_commands.command(name="help", description="Show the ClassCode beginner command guide.")
    async def help_command(self, interaction: discord.Interaction):
        embed = UIEmbeds.standard(
            "\U0001f9ed CLASSCODE BEGINNER GUIDE",
            "You only need a few commands at first. Everything else can wait."
        )
        embed.add_field(name="\U0001f331 Start", value="`/start` \u2014 your beginner path\n`/dashboard` \u2014 your home screen", inline=False)
        embed.add_field(name="\U0001f4da Learn", value="`/cpp-roadmap` \u2014 C++ lessons\n`/java-roadmap` \u2014 Java lessons", inline=False)
        embed.add_field(name="\U0001f4bb Practice", value="`/cpp-quiz` / `/java-quiz` \u2014 check understanding\n`/daily-challenge` \u2014 daily coding task", inline=False)
        embed.add_field(name="\U0001f198 Get Help", value="`/hint` \u2014 small clue\n`/explain` \u2014 simple explanation\n`/explain-error` \u2014 understand an error\n`/code-review` \u2014 feedback on your code", inline=False)
        embed.add_field(name="\U0001f3c6 Track Progress", value="`/profile` \u2022 `/progress` \u2022 `/mastery` \u2022 `/skill-tree` \u2022 `/leaderboard`", inline=False)
        embed.set_footer(text="Tip: If you are new, use /start and ignore the advanced commands until you need them.")
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(name="dashboard",description="Open your ClassCode home dashboard.")
    async def dashboard(self,interaction:discord.Interaction):
        await interaction.response.defer(ephemeral=False, thinking=True)
        await interaction.followup.send(embed=await self.build(interaction.user),view=DashboardView())

    @app_commands.command(name="daily-goal",description="View today's learning goal and activity.")
    async def daily_goal(self,interaction:discord.Interaction):
        await interaction.response.defer(ephemeral=True, thinking=True)
        goal=await db.fetchone("SELECT lessons,quizzes,challenges,xp_earned FROM daily_goals WHERE user_id=? AND goal_date=date('now')",(interaction.user.id,))
        g=goal or {"lessons":0,"quizzes":0,"challenges":0,"xp_earned":0}
        complete=min(100,int(((g['lessons']>0)+(g['quizzes']>0)+(g['challenges']>0))*100/3))
        embed=UIEmbeds.standard("\U0001f3af TODAY'S GOAL",f"Complete at least one learning activity of each type.\n\nLessons: {'\u2705' if g['lessons'] else '\u2b1c'}\nQuizzes: {'\u2705' if g['quizzes'] else '\u2b1c'}\nChallenges: {'\u2705' if g['challenges'] else '\u2b1c'}\n\nProgress: **{complete}%**\nXP earned today: **{g['xp_earned']}**")
        await interaction.followup.send(embed=embed,ephemeral=True)

async def setup(bot): await bot.add_cog(DashboardCog(bot))
