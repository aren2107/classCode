import asyncio
import hashlib
import secrets
import logging
from datetime import date
from bot.timezone import manila_today
import discord
from discord.ext import commands
from discord import app_commands
from bot.database import db
from bot.learning.mastery import (
    _add_xp_in_transaction,
    _publish_xp_result,
    _submit_assignment_in_transaction,
    ensure_user_in_transaction,
    award_badge,
)
from bot.services.invite_codes import new_invite_code, normalize_invite_code
from bot.learning.cpp import CPP_CURRICULUM
from bot.learning.java import JAVA_CURRICULUM
from bot.ui.embeds import UIEmbeds, ColorPalette

LANGS = {"cpp": CPP_CURRICULUM, "java": JAVA_CURRICULUM}
logger = logging.getLogger(__name__)


def is_reserved_system_note_title(title: str) -> bool:
    return title.strip().casefold().startswith("classcode ")


PLACEMENT_QUESTIONS = {
    "cpp": [
        ("What does `int x = 5;` do?", ["Declares x and stores 5", "Prints 5", "Reads x", "Deletes x"], 0),
        ("Which loop is commonly used when the iteration count is known?", ["for", "class", "switch", "catch"], 0),
        ("What is the first valid index of a normal C++ array?", ["0", "1", "-1", "Depends on the array"], 0),
        ("What does a function return type describe?", ["The type of result it returns", "Its variable count", "Its class name", "Its loop count"], 0),
        ("What does `vector` provide compared with a fixed raw array?", ["A resizable sequence", "Automatic sorting", "No memory use", "Only strings"], 0),
        ("What does a private class member support?", ["Encapsulation", "Infinite loops", "Input parsing", "Sorting"], 0),
        ("What does a virtual function enable in a polymorphic hierarchy?", ["Dynamic dispatch", "File persistence", "Array indexing", "Compilation without headers"], 0),
        ("What does O(n) describe?", ["A growth pattern where work is proportional to input size", "A syntax error", "A data type", "A compiler option"], 0),
        ("Which structure is FIFO?", ["Queue", "Stack", "Set", "Tree only"], 0),
        ("What should you do before coding a long specification?", ["Break it into inputs, rules, processing, and outputs", "Start writing random code", "Skip validation", "Only design the final output"], 0),
    ],
    "java": [
        ("Which method is the normal Java program entry point?", ["public static void main", "startProgram", "run", "begin"], 0),
        ("Which type stores a whole number such as 18?", ["int", "double", "boolean", "char[] only"], 0),
        ("Which collection is a resizable ordered list?", ["ArrayList", "HashSet", "HashMap", "Thread"], 0),
        ("What does a method return type describe?", ["The type of result it returns", "Its class name", "Its loop count", "Its package"], 0),
        ("What is encapsulation mainly about?", ["Controlling access to object state", "Removing all methods", "Avoiding classes", "Making fields global"], 0),
        ("Which keyword declares class inheritance?", ["extends", "inherits", "parent", "base"], 0),
        ("What does an interface primarily define?", ["A contract/capability", "A database file", "A loop", "A compiler flag"], 0),
        ("What is a common benefit of generics?", ["Type-safe reusable code", "No compilation", "Automatic databases", "Fewer classes always"], 0),
        ("Which collection is FIFO?", ["Queue", "Stack", "Set", "Map"], 0),
        ("What should you do before implementing a large requirement?", ["Break it into inputs, rules, processing, and outputs", "Skip the specification", "Only write UI", "Ignore edge cases"], 0),
    ],
}

class PlacementView(discord.ui.View):
    """Ten-question placement check using the same private embed/ABCD flow as lesson quizzes."""

    def __init__(self, owner_id: int, language: str):
        super().__init__(timeout=600)
        self.owner_id = owner_id
        self.language = language
        self.questions = []
        for question, options, answer in PLACEMENT_QUESTIONS[language]:
            copied_options = list(options)
            correct_text = copied_options[answer]
            secrets.SystemRandom().shuffle(copied_options)
            self.questions.append({
                "question": question,
                "options": copied_options,
                "answer": copied_options.index(correct_text),
            })
        self.index = 0
        self.score = 0
        self.finished = False
        self._render()

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id != self.owner_id:
            await interaction.response.send_message(
                "ðŸ”’ This is another student's private placement check. Run `/placement` to start your own.",
                ephemeral=True,
            )
            return False
        if self.finished:
            await interaction.response.send_message(
                "This placement check has already finished. Run `/placement` again when you're ready.",
                ephemeral=True,
            )
            return False
        return True

    def _render(self):
        self.clear_items()
        for selected, label in enumerate("ABCD"):
            button = discord.ui.Button(label=label, style=discord.ButtonStyle.secondary, row=0)

            async def callback(interaction: discord.Interaction, choice=selected):
                await self._answer(interaction, choice)

            button.callback = callback
            self.add_item(button)

    def _embed(self, feedback: str = ""):
        question = self.questions[self.index]
        description = (
            f"**Question {self.index + 1}/{len(self.questions)}**\n"
            f"{question['question']}\n\n"
            + "\n".join(
                f"**{'ABCD'[i]}.** {option}"
                for i, option in enumerate(question["options"])
            )
        )
        if feedback:
            description = feedback + "\n\n" + description
        return UIEmbeds.standard(
            f"ðŸ§­ {self.language.upper()} â€¢ Placement Check",
            description,
            ColorPalette.PRIMARY,
        )

    async def _answer(self, interaction: discord.Interaction, selected: int):
        # Acknowledge the component interaction immediately, then edit the private quiz message.
        await interaction.response.defer()
        question = self.questions[self.index]
        correct = selected == question["answer"]
        if correct:
            self.score += 1
            feedback = "âœ… Correct."
        else:
            correct_index = question["answer"]
            feedback = (
                f"âŒ Not quite. Correct answer: **{'ABCD'[correct_index]}. "
                f"{question['options'][correct_index]}**."
            )

        self.index += 1
        if self.index < len(self.questions):
            self._render()
            await interaction.edit_original_response(embed=self._embed(feedback), view=self)
            return

        self.finished = True
        self.clear_items()
        if self.score <= 4:
            start_index, stage = 0, "Foundation"
        elif self.score <= 7:
            start_index, stage = 7, "Core Problem Solving"
        elif self.score <= 9:
            start_index, stage = 21, "Advanced Language Skills"
        else:
            start_index, stage = 28, "Algorithms & Engineering"

        title = f"ClassCode Placement {self.language.upper()}"
        body = f"SCORE: {self.score}/10\nSTAGE: {stage}\nSTART_INDEX: {start_index}"
        saved = False
        try:
            def save_placement(conn):
                existing = conn.execute(
                    "SELECT note_id FROM personal_notes WHERE user_id=? AND title=? "
                    "ORDER BY note_id DESC LIMIT 1",
                    (interaction.user.id, title),
                ).fetchone()
                ensure_user_in_transaction(conn, interaction.user.id, interaction.user.display_name)
                if existing:
                    conn.execute(
                        "UPDATE personal_notes SET body=?, updated_at=CURRENT_TIMESTAMP WHERE note_id=? AND user_id=?",
                        (body, existing["note_id"], interaction.user.id),
                    )
                else:
                    conn.execute(
                        "INSERT INTO personal_notes(user_id,title,body) VALUES(?,?,?)",
                        (interaction.user.id, title, body),
                    )

            await db.run_transaction(save_placement)
            saved = True
        except Exception as exc:
            logger.warning(
                "Placement recommendation could not be saved for user %s (%s)",
                interaction.user.id,
                type(exc).__name__,
            )

        result = (
            f"**Score: {self.score}/10**\n"
            f"**Recommended starting stage:** {stage}\n\n"
            "This is a starting-point recommendation, not a label of your ability. "
            "Earlier lessons remain available for review. Use `/start` or `/next-lesson` "
            "to begin your recommended path."
        )
        if not saved:
            result += "\n\nâš ï¸ I could not save this recommendation. Your answers were not recorded; please try `/placement` again later."
        embed = UIEmbeds.standard("ðŸŽ¯ Placement complete", result, ColorPalette.SUCCESS)
        await interaction.edit_original_response(embed=embed, view=None)

    async def on_timeout(self):
        for item in self.children:
            item.disabled = True

TITLES = {
    "rookie": "\U0001f423 Code Rookie", "solver": "\U0001f9e0 Problem Solver", "debugger": "\U0001f41b Debugger",
    "builder": "\U0001f3d7\ufe0f Project Builder", "architect": "\U0001f48e Code Architect", "streak": "\U0001f525 Streak Master"
}
BUGS = [
    ("loop-off-by-one","cpp","Off-by-one loop","int sum=0;\nfor(int i=0;i<=5;i++) sum += i;\ncout << sum;","i<5","The loop includes 5. If the intended range is 0 through 4, use i<5.","Beginner"),
    ("java-null","java","Null reference","String name=null;\nSystem.out.println(name.length());","name != null","Calling length() on null causes a NullPointerException. Check the value before using it.","Beginner"),
    ("cpp-divzero","cpp","Division by zero","int a=10, b=0;\ncout << a/b;","b != 0","The denominator is zero. Validate it before dividing.","Beginner"),
]

async def seed_bugs():
    for row in BUGS:
        await db.execute("INSERT OR IGNORE INTO bug_puzzles(puzzle_id,language,title,code,answer,explanation,difficulty) VALUES(?,?,?,?,?,?,?)", row)

class QuestionnaireView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.answers = {}
        lang = discord.ui.Select(placeholder="1\ufe0f\u20e3 Choose your language", custom_id="classcode_questionnaire_language", options=[
            discord.SelectOption(label="C++", value="cpp"), discord.SelectOption(label="Java", value="java"), discord.SelectOption(label="Both", value="both")])
        level = discord.ui.Select(placeholder="2\ufe0f\u20e3 Choose your experience", custom_id="classcode_questionnaire_level", options=[
            discord.SelectOption(label="Beginner", value="beginner"), discord.SelectOption(label="Intermediate", value="intermediate"), discord.SelectOption(label="Advanced", value="advanced")])
        goal = discord.ui.Select(placeholder="3\ufe0f\u20e3 Choose your goal", custom_id="classcode_questionnaire_goal", options=[
            discord.SelectOption(label="Learn programming basics", value="basics"), discord.SelectOption(label="Pass practical exams", value="exams"), discord.SelectOption(label="Build projects", value="projects"), discord.SelectOption(label="Prepare for a career", value="career")])
        lang.callback = self.language_callback
        level.callback = self.level_callback
        goal.callback = self.goal_callback
        self.add_item(lang); self.add_item(level); self.add_item(goal)

    async def save(self, interaction):
        answer = self.answers.get(interaction.user.id, {})
        if not all((answer.get("language"), answer.get("level"), answer.get("goal"))):
            await interaction.response.send_message("Choose all three questionnaire answers first.", ephemeral=True)
            return
        await interaction.response.defer(ephemeral=True, thinking=True)
        body = f"Language: {answer['language']}\nExperience: {answer['level']}\nGoal: {answer['goal']}"

        def operation(conn):
            existing = conn.execute(
                "SELECT note_id FROM personal_notes WHERE user_id=? AND title=? ORDER BY note_id DESC LIMIT 1",
                (interaction.user.id, "ClassCode Questionnaire"),
            ).fetchone()
            ensure_user_in_transaction(conn, interaction.user.id, interaction.user.display_name)
            if existing:
                conn.execute(
                    "UPDATE personal_notes SET body=?, updated_at=CURRENT_TIMESTAMP WHERE note_id=? AND user_id=?",
                    (body, existing["note_id"], interaction.user.id),
                )
            else:
                conn.execute(
                    "INSERT INTO personal_notes(user_id,title,body) VALUES(?,?,?)",
                    (interaction.user.id, "ClassCode Questionnaire", body),
                )

        await db.run_transaction(operation)
        self.answers.pop(interaction.user.id, None)
        await interaction.followup.send(
            f"âœ… Profile saved.\n**Language:** {answer['language']}\n**Experience:** {answer['level']}\n**Goal:** {answer['goal']}\n\nYou can now start the roadmap.",
            ephemeral=True,
        )

    async def language_callback(self, interaction):
        self.answers.setdefault(interaction.user.id, {})["language"] = interaction.data["values"][0]
        value = interaction.data["values"][0]
        await interaction.response.send_message(f"Saved language: **{value}**. Choose your experience and goal next.", ephemeral=True)
    async def level_callback(self, interaction):
        self.answers.setdefault(interaction.user.id, {})["level"] = interaction.data["values"][0]
        value = interaction.data["values"][0]
        await interaction.response.send_message(f"Saved experience: **{value}**. Choose your goal next.", ephemeral=True)
    async def goal_callback(self, interaction):
        self.answers.setdefault(interaction.user.id, {})["goal"] = interaction.data["values"][0]
        await self.save(interaction)

class AcademyCog(commands.Cog):
    def __init__(self, bot): self.bot=bot

    @app_commands.command(name="placement", description="Take a short placement check to choose a recommended starting stage.")
    @app_commands.choices(language=[app_commands.Choice(name="C++", value="cpp"), app_commands.Choice(name="Java", value="java")])
    async def placement(self, interaction: discord.Interaction, language: str):
        # Receive the selected choice value directly instead of relying on the
        # Choice object. This keeps the selected language unambiguous even
        # when Discord is showing a cached slash-command UI.
        lang = str(language).strip().lower()
        if lang not in PLACEMENT_QUESTIONS:
            await interaction.response.send_message("\u274c Choose either C++ or Java.", ephemeral=True)
            return
        display_language = "C++" if lang == "cpp" else "Java"
        view = PlacementView(interaction.user.id, lang)
        first_question = view.questions[0]
        embed = UIEmbeds.standard(
            f"ðŸ§­ {display_language} â€¢ Placement Check",
            "Answer 10 questions. This does not label you as an expert; it recommends a starting point so you can avoid repeating material you already know.\n\n"
            + f"**Question 1/{len(view.questions)}**\n{first_question['question']}\n\n"
            + "\n".join(
                f"**{'ABCD'[i]}.** {option}"
                for i, option in enumerate(first_question['options'])
            ),
            ColorPalette.PRIMARY,
        )
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

    @app_commands.command(name="questionnaire", description="Open or update your ClassCode learning profile.")
    async def questionnaire(self, interaction: discord.Interaction):
        embed = UIEmbeds.standard(
            "\U0001f4dd YOUR CLASSCODE LEARNING PROFILE",
            "Answer three quick questions. ClassCode uses them to recommend your starting language and learning path.\n\n"
            "You can run `/questionnaire` again anytime if your goals change."
        )
        embed.add_field(name="1\ufe0f\u20e3 Language", value="Choose C++, Java, or Both.", inline=True)
        embed.add_field(name="2\ufe0f\u20e3 Experience", value="Choose the level that honestly matches you.", inline=True)
        embed.add_field(name="3\ufe0f\u20e3 Goal", value="Choose what you want ClassCode to help you accomplish.", inline=True)
        await interaction.response.send_message(embed=embed, view=QuestionnaireView(), ephemeral=True)

    @app_commands.command(name="explain-code", description="Explain a code snippet line by line in beginner-friendly language.")
    @app_commands.describe(language="C++ or Java", code="Code to explain")
    @app_commands.choices(language=[app_commands.Choice(name="C++",value="cpp"),app_commands.Choice(name="Java",value="java")])
    async def explain_code(self, interaction, language: app_commands.Choice[str], code: str):
        lines=code.strip().splitlines()
        if len(lines)>40 or len(code)>6000:
            await interaction.response.send_message("\u274c Keep the snippet under 40 lines and 6000 characters.",ephemeral=True); return
        explanation=[]
        for i,line in enumerate(lines,1):
            stripped=line.strip()
            if not stripped: continue
            if "for" in stripped: tip="loop/repetition control"
            elif "if" in stripped: tip="conditional decision"
            elif "cout" in stripped or "System.out" in stripped or "print" in stripped: tip="prints output"
            elif "=" in stripped and not "==" in stripped: tip="assigns a value"
            elif "class" in stripped: tip="declares a class"
            elif "return" in stripped: tip="returns a value from a function/method"
            else: tip="program statement"
            explanation.append(f"**{i}.** `{stripped[:180]}` \u2014 {tip}.")
        embed=UIEmbeds.standard("\U0001f9e0 EXPLAIN MY CODE", "\n".join(explanation)[:3900] or "No code provided.")
        await interaction.response.send_message(embed=embed,ephemeral=True)

    @app_commands.command(name="code-health", description="Get a lightweight code-quality report.")
    async def code_health(self, interaction, code: str):
        lines=code.splitlines(); chars=len(code); comments=sum(1 for x in lines if x.strip().startswith(("//","#","/*","*")))
        long_lines=sum(1 for x in lines if len(x)>100); score=max(0,min(100,100-long_lines*5-(0 if comments else 10)))
        embed=UIEmbeds.standard("\U0001fa7a CODE HEALTH",f"Readability **{score}%**\nComments **{comments}**\nLines **{len(lines)}**\nCharacters **{chars}**\n\n\U0001f4a1 Suggestions\n\u2022 Keep lines short and focused.\n\u2022 Use descriptive variable names.\n\u2022 Add comments for non-obvious logic.\n\u2022 Break large functions into smaller functions.")
        await interaction.response.send_message(embed=embed,ephemeral=True)

    @app_commands.command(name="debug", description="Enter guided debugging mode without revealing the answer immediately.")
    async def debug(self, interaction, error: str):
        hints=["What is the first error message, not the last one?","Which variable or value does the error mention?","Can you reproduce the problem with the smallest possible input?","Now inspect the line where that value is created or changed."]
        await interaction.response.send_message(embed=UIEmbeds.standard("\U0001f41b GUIDED DEBUGGER",f"**Your error:** `{error[:700]}`\n\n**Hint 1:** {hints[0]}\n\nUse `/explain-error` for a direct beginner explanation, or ask again with the exact compiler message for another debugging hint."),ephemeral=True)

    @app_commands.command(name="bug-puzzle", description="Solve a small debugging puzzle.")
    async def bug_puzzle(self, interaction):
        await interaction.response.defer(ephemeral=True, thinking=True)
        await seed_bugs()
        rows=await db.fetchall("SELECT * FROM bug_puzzles ORDER BY puzzle_id")
        idx=(interaction.user.id + manila_today().day)%len(rows)
        r=rows[idx]
        await db.execute("INSERT OR IGNORE INTO bug_attempts(user_id,puzzle_id) VALUES(?,?)",(interaction.user.id,r['puzzle_id']))
        view=BugAnswerView(r['puzzle_id'])
        embed=UIEmbeds.standard(f"\U0001f41b {r['title']}",f"**Language:** {r['language'].upper()}\n**Difficulty:** {r['difficulty']}\n\n```text\n{r['code']}\n```\n\nWhat condition or fix would prevent the bug? Use the buttons for a guided attempt.")
        await interaction.followup.send(embed=embed,view=view,ephemeral=True)

    @app_commands.command(name="skill-tree", description="View your programming skill tree.")
    async def skill_tree(self, interaction):
        await interaction.response.defer(ephemeral=False, thinking=True)
        parts=[]
        for lang,curr in LANGS.items():
            rows=await db.fetchall("SELECT topic_id,status FROM user_progress WHERE user_id=? AND language=?",(interaction.user.id,lang))
            status={x['topic_id']:x['status'] for x in rows}
            parts.append(f"**{'\U0001f7e6 C++' if lang=='cpp' else '\u2615 Java'}**")
            for t in curr:
                icon='\u2705' if status.get(t['id'])=='completed' else ('\U0001f7e2' if status.get(t['id'])=='unlocked' else '\U0001f512')
                parts.append(f"{icon} {t['title']}")
        await interaction.followup.send(embed=UIEmbeds.standard("\U0001f333 CLASSCODE SKILL TREE","\n".join(parts)[:3900]))

    @app_commands.command(name="mastery", description="See mastery levels and weak areas.")
    async def mastery(self, interaction):
        await interaction.response.defer(ephemeral=True, thinking=True)
        blocks=[]
        for lang,curr in LANGS.items():
            rows=await db.fetchall("SELECT topic_id,status FROM user_progress WHERE user_id=? AND language=?",(interaction.user.id,lang))
            done=sum(r['status']=='completed' for r in rows); pct=round(done/len(curr)*100) if curr else 0
            blocks.append(f"**{lang.upper()}** \u2014 {pct}% mastery ({done}/{len(curr)})")
        attempts=await db.fetchall("SELECT language,topic_id,AVG(score*1.0/NULLIF(total,0)) avg FROM quiz_attempts WHERE user_id=? GROUP BY language,topic_id ORDER BY avg ASC LIMIT 3",(interaction.user.id,))
        weak="\n".join(f"\u2022 {r['language'].upper()} `{r['topic_id']}` \u2014 {round(r['avg']*100)}% quiz average" for r in attempts) or "\u2022 Not enough quiz data yet."
        await interaction.followup.send(embed=UIEmbeds.standard("\U0001f9e0 MASTERY REPORT","\n".join(blocks)+f"\n\n**Needs Practice**\n{weak}"),ephemeral=True)

    @app_commands.command(name="missions", description="View personalized daily coding missions.")
    async def missions(self, interaction):
        await interaction.response.defer(ephemeral=True, thinking=True)
        today=manila_today().isoformat(); await ensure_missions(interaction.user.id,today,interaction.user.display_name)
        rows=await db.fetchall("SELECT kind,target,progress,reward FROM daily_missions WHERE user_id=? AND mission_date=?",(interaction.user.id,today))
        desc="\n".join(f"{'\u2705' if r['progress']>=r['target'] else '\u2b1c'} **{r['kind'].title()}** `{min(r['progress'],r['target'])}/{r['target']}` \u2014 +{r['reward']} XP" for r in rows)
        await interaction.followup.send(embed=UIEmbeds.standard("\U0001f3af PERSONAL MISSIONS",desc),ephemeral=True)

    @app_commands.command(name="save-snippet", description="Save a useful code snippet to your notebook.")
    async def save_snippet(self, interaction, title:str, language:str, code:str, note:str=""):
        await interaction.response.defer(ephemeral=True, thinking=True)
        if len(code)>10000: await interaction.followup.send("\u274c Snippet is too large.",ephemeral=True); return
        def operation(conn):
            ensure_user_in_transaction(conn, interaction.user.id, interaction.user.display_name)
            conn.execute("INSERT INTO code_snippets(user_id,title,language,code,note) VALUES(?,?,?,?,?)",(interaction.user.id,title,language.lower(),code,note))
        await db.run_transaction(operation)
        await interaction.followup.send("\U0001f4cc Snippet saved to your Code Notebook.",ephemeral=True)

    @app_commands.command(name="my-snippets", description="Browse your saved code snippets.")
    async def my_snippets(self, interaction):
        await interaction.response.defer(ephemeral=True, thinking=True)
        rows=await db.fetchall("SELECT snippet_id,title,language,note FROM code_snippets WHERE user_id=? ORDER BY snippet_id DESC LIMIT 15",(interaction.user.id,))
        desc="\n".join(f"`#{r['snippet_id']}` **{r['title']}** \u2014 {r['language'].upper()}\n{r['note'][:120]}" for r in rows) or "No snippets yet. Use `/save-snippet`."
        await interaction.followup.send(embed=UIEmbeds.standard("\U0001f4d3 CODE NOTEBOOK",desc),ephemeral=True)

    @app_commands.command(name="note", description="Save a personal learning note.")
    async def note(self, interaction, title:str, body:str):
        if is_reserved_system_note_title(title):
            await interaction.response.send_message(
                "That title is reserved for ClassCode system records. Choose another title.",
                ephemeral=True,
            )
            return
        await interaction.response.defer(ephemeral=True, thinking=True)
        def operation(conn):
            ensure_user_in_transaction(conn, interaction.user.id, interaction.user.display_name)
            conn.execute("INSERT INTO personal_notes(user_id,title,body) VALUES(?,?,?)",(interaction.user.id,title,body))
        await db.run_transaction(operation)
        await interaction.followup.send("\U0001f4dd Note saved.",ephemeral=True)

    @app_commands.command(name="notes", description="View your recent learning notes.")
    async def notes(self, interaction):
        await interaction.response.defer(ephemeral=True, thinking=True)
        rows=await db.fetchall("SELECT title,body FROM personal_notes WHERE user_id=? ORDER BY note_id DESC LIMIT 10",(interaction.user.id,))
        desc="\n\n".join(f"**{r['title']}**\n{r['body'][:300]}" for r in rows) or "No notes yet."
        await interaction.followup.send(embed=UIEmbeds.standard("\U0001f4dd MY NOTES",desc),ephemeral=True)

    @app_commands.command(name="portfolio", description="Show your ClassCode portfolio summary.")
    async def portfolio(self, interaction):
        await interaction.response.defer(ephemeral=False, thinking=True)
        rows=await db.fetchall("SELECT p.title,p.language,p.difficulty,pp.completed_at FROM project_progress pp JOIN projects p ON p.project_id=pp.project_id WHERE pp.user_id=? AND pp.status='completed' ORDER BY pp.completed_at DESC",(interaction.user.id,))
        user=await db.fetchone("SELECT xp,level,streak_count FROM users WHERE user_id=?",(interaction.user.id,))
        desc=f"**Level:** {user['level'] if user else 1}\n**XP:** {user['xp'] if user else 0}\n**Streak:** {user['streak_count'] if user else 0}\n\n**Projects**\n"+("\n".join(f"\u2022 {r['title']} \u2014 {r['language'].upper()} {r['difficulty']}" for r in rows) if rows else "No completed projects yet.")
        await interaction.followup.send(embed=UIEmbeds.standard(f"\U0001f4bc {interaction.user.display_name}'S PORTFOLIO",desc))

    @app_commands.command(name="study-group-create", description="Create a study group.")
    async def group_create(self, interaction, name:str, topic:str):
        await interaction.response.defer(ephemeral=True, thinking=True)
        gid=new_invite_code()
        def operation(conn):
            ensure_user_in_transaction(conn, interaction.user.id, interaction.user.display_name)
            conn.execute("INSERT INTO study_groups(group_id,name,owner_id,topic) VALUES(?,?,?,?)",(gid,name,interaction.user.id,topic))
            conn.execute("INSERT INTO study_group_members(group_id,user_id,role) VALUES(?,?,?)",(gid,interaction.user.id,'owner'))
        await db.run_transaction(operation)
        await interaction.followup.send(embed=UIEmbeds.standard("\U0001f465 STUDY GROUP CREATED",f"**{name}**\nTopic: {topic}\nJoin code: `{gid}`"),ephemeral=True)

    @app_commands.command(name="study-group-join", description="Join a study group.")
    @app_commands.checks.cooldown(3, 60.0, key=lambda interaction: interaction.user.id)
    async def group_join(self, interaction, group_code:str):
        await interaction.response.defer(ephemeral=True, thinking=True)
        normalized_code=normalize_invite_code(group_code)
        if not normalized_code:
            await interaction.followup.send("âŒ Study group code is invalid.",ephemeral=True)
            return
        def operation(conn):
            g=conn.execute("SELECT * FROM study_groups WHERE group_id=?",(normalized_code,)).fetchone()
            if not g:
                return None
            ensure_user_in_transaction(conn, interaction.user.id, interaction.user.display_name)
            conn.execute("INSERT OR IGNORE INTO study_group_members(group_id,user_id) VALUES(?,?)",(g['group_id'],interaction.user.id))
            return g
        g=await db.run_transaction(operation)
        if not g: await interaction.followup.send("\u274c Group not found.",ephemeral=True); return
        await interaction.followup.send(f"\U0001f465 Joined **{g['name']}**.",ephemeral=True)

    @app_commands.command(name="study-groups", description="Browse active study groups.")
    async def groups(self, interaction):
        await interaction.response.defer(ephemeral=False, thinking=True)
        rows=await db.fetchall("SELECT g.group_id,g.name,g.topic,COUNT(m.user_id) members FROM study_groups g LEFT JOIN study_group_members m ON g.group_id=m.group_id GROUP BY g.group_id ORDER BY g.created_at DESC LIMIT 15")
        desc="\n".join(f"`{r['group_id']}` **{r['name']}** \u2014 {r['topic']} \u2022 {r['members']} members" for r in rows) or "No study groups yet."
        await interaction.followup.send(embed=UIEmbeds.standard("\U0001f465 STUDY GROUPS",desc))

    @app_commands.command(name="titles", description="View your unlocked ClassCode titles.")
    async def titles(self, interaction):
        await interaction.response.defer(ephemeral=True, thinking=True)
        rows=await db.fetchall("SELECT title_id FROM user_titles WHERE user_id=?",(interaction.user.id,))
        desc="\n".join(f"\u2022 {TITLES.get(r['title_id'],r['title_id'])}" for r in rows) or "No titles unlocked yet. Keep learning!"
        await interaction.followup.send(embed=UIEmbeds.standard("\U0001f3c5 YOUR TITLES",desc),ephemeral=True)


    @app_commands.command(name="assignment-list", description="View assignments for your ClassCode classes.")
    async def assignment_list(self, interaction):
        await interaction.response.defer(ephemeral=True, thinking=True)
        rows=await db.fetchall("""SELECT a.title,a.language,a.due_date,c.name,cm.role,
            CASE WHEN s.user_id IS NULL THEN 0 ELSE 1 END submitted
            FROM assignments a JOIN classes c ON a.class_id=c.class_id
            JOIN class_members cm ON cm.class_id=c.class_id
            LEFT JOIN assignment_submissions s ON s.assignment_id=a.assignment_id AND s.user_id=?
            WHERE cm.user_id=? ORDER BY a.created_at DESC LIMIT 20""",(interaction.user.id,interaction.user.id))
        desc="\n".join(f"{'\u2705' if r['submitted'] else '\u2b1c'} **{r['title']}** \u2014 {r['language'].upper()} \u2022 {r['name']} \u2022 Due: `{r['due_date'] or 'None'}`" for r in rows) or "No assignments yet."
        await interaction.followup.send(embed=UIEmbeds.standard("\U0001f4dd MY ASSIGNMENTS",desc),ephemeral=True)

    @app_commands.command(name="assignment-submit", description="Mark a class assignment as submitted.")
    async def assignment_submit(self, interaction, assignment_id:int):
        await interaction.response.defer(ephemeral=True, thinking=True)
        result = await db.run_transaction(
            lambda conn: _submit_assignment_in_transaction(
                conn, interaction.user.id, interaction.user.display_name,
                assignment_id, manila_today(),
            )
        )
        if result is None:
            await interaction.followup.send(
                "❌ Assignment not found, or you are no longer a member of its class.",
                ephemeral=True,
            )
            return
        if result is False:
            await interaction.followup.send(
                "Already submitted. No additional XP was awarded.",
                ephemeral=True,
            )
            return
        xp_result = result
        await _publish_xp_result(interaction.user.id, interaction.guild, xp_result)
        await interaction.followup.send("\U0001f4e4 Assignment marked as submitted. XP awarded!", ephemeral=True)

    @app_commands.command(name="class-analytics", description="Teacher/admin analytics for a class.")
    async def class_analytics(self, interaction, class_code:str):
        await interaction.response.defer(ephemeral=True, thinking=True)
        c=await db.fetchone("SELECT * FROM classes WHERE class_id=?",(class_code.upper(),))
        if not c: await interaction.followup.send("\u274c Class not found.",ephemeral=True); return
        member=await db.fetchone("SELECT role FROM class_members WHERE class_id=? AND user_id=?",(c['class_id'],interaction.user.id))
        if not member or member['role']!='teacher': await interaction.followup.send("\u274c Teacher access required.",ephemeral=True); return
        total=(await db.fetchone("SELECT COUNT(*) c FROM class_members WHERE class_id=? AND role='student'",(c['class_id'],)))['c']
        submitted=(await db.fetchone("SELECT COUNT(DISTINCT s.user_id) c FROM assignment_submissions s JOIN assignments a ON a.assignment_id=s.assignment_id WHERE a.class_id=?",(c['class_id'],)))['c']
        avg=(await db.fetchone("SELECT COALESCE(AVG(u.xp),0) avg FROM users u JOIN class_members cm ON cm.user_id=u.user_id WHERE cm.class_id=? AND cm.role='student'",(c['class_id'],)))['avg']
        await interaction.followup.send(embed=UIEmbeds.standard("\U0001f4ca TEACHER ANALYTICS",f"Class: **{c['name']}**\nStudents: **{total}**\nStudents with submissions: **{submitted}**\nAverage XP: **{round(avg)}**"),ephemeral=True)

    @app_commands.command(name="weekly-report", description="View a weekly learning summary.")
    async def weekly_report(self, interaction):
        await interaction.response.defer(ephemeral=True, thinking=True)
        xp=(await db.fetchone("SELECT COALESCE(SUM(amount),0) total FROM xp_history WHERE user_id=? AND created_at >= datetime('now','-7 day')",(interaction.user.id,)))['total']
        quizzes=(await db.fetchone("SELECT COUNT(*) c FROM quiz_attempts WHERE user_id=? AND attempted_at >= datetime('now','-7 day')",(interaction.user.id,)))['c']
        bugs=(await db.fetchone("SELECT COUNT(*) c FROM bug_attempts WHERE user_id=? AND solved=1",(interaction.user.id,)))['c']
        projects=(await db.fetchone("SELECT COUNT(*) c FROM project_progress WHERE user_id=? AND status='completed' AND completed_at >= datetime('now','-7 day')",(interaction.user.id,)))['c']
        await interaction.followup.send(embed=UIEmbeds.standard("\U0001f4ca YOUR WEEK IN CLASSCODE",f"\u2b50 XP earned: **{xp}**\n\U0001f9e9 Quiz attempts: **{quizzes}**\n\U0001f41b Bugs solved: **{bugs}**\n\U0001f3d7\ufe0f Projects completed: **{projects}**\n\nKeep the next session small and consistent: one lesson, one problem, one reflection."),ephemeral=True)

    @app_commands.command(name="pair-up", description="Join or leave the coding partner queue.")
    @app_commands.choices(language=[app_commands.Choice(name="C++",value="cpp"),app_commands.Choice(name="Java",value="java")])
    async def pair_up(self, interaction, language:app_commands.Choice[str], leave:bool=False):
        await interaction.response.defer(ephemeral=False, thinking=True)
        if leave:
            await db.execute("DELETE FROM pair_queue WHERE user_id=?",(interaction.user.id,)); await interaction.followup.send("\U0001f44b You left the pairing queue.",ephemeral=True); return
        def match_or_enqueue(conn):
            ensure_user_in_transaction(conn, interaction.user.id, interaction.user.display_name)
            other=conn.execute("SELECT user_id FROM pair_queue WHERE language=? AND user_id<>? ORDER BY joined_at LIMIT 1",(language.value,interaction.user.id)).fetchone()
            if other:
                conn.execute("DELETE FROM pair_queue WHERE user_id IN (?,?)",(other['user_id'],interaction.user.id))
                return other['user_id']
            conn.execute("INSERT INTO pair_queue(user_id,language) VALUES(?,?) ON CONFLICT(user_id) DO UPDATE SET language=excluded.language, joined_at=CURRENT_TIMESTAMP",(interaction.user.id,language.value))
            return None
        other_user_id=await db.run_transaction(match_or_enqueue)
        if other_user_id:
            await interaction.followup.send(f"\U0001f91d Pair found! You can collaborate with <@{other_user_id}> on **{language.name}**.",ephemeral=False)
        else:
            await interaction.followup.send(f"\U0001f91d You're in the **{language.name}** pairing queue. I'll match you with the next learner who joins.",ephemeral=True)

    @app_commands.command(name="seasonal-event", description="View the current ClassCode coding event.")
    async def seasonal_event(self, interaction):
        await interaction.response.defer(ephemeral=False, thinking=True)
        month=manila_today().month
        names={1:"New Year Code Quest",2:"Algorithm Love Lab",3:"Spring Debug Sprint",4:"April Code Challenge",5:"Build Month",6:"Summer Coding Quest",7:"Midyear Debug Derby",8:"Back-to-Code Challenge",9:"School Starter Sprint",10:"Spooky Bug Hunt",11:"Project Builder Cup",12:"Winter Code Quest"}
        eid=f"event-{manila_today().year}-{month}"
        r=await db.fetchone("SELECT points FROM event_progress WHERE user_id=? AND event_id=?",(interaction.user.id,eid)); points=r['points'] if r else 0
        await interaction.followup.send(embed=UIEmbeds.standard(f"\U0001f3c6 {names[month]}",f"Event ID: `{eid}`\nYour event points: **{points}**\n\nEarn points by completing lessons, debugging puzzles, quizzes, and projects during the month."))

    @app_commands.command(name="event-points", description="Record event points for a completed ClassCode activity.")
    @app_commands.checks.has_permissions(manage_guild=True)
    @app_commands.describe(user="Student receiving the points", points="Points to award", reason="Why the points were awarded")
    async def event_points(self, interaction, user:discord.Member, points:int=10, reason:str="ClassCode event activity"):
        await interaction.response.defer(ephemeral=True, thinking=True)
        points=max(1,min(points,100)); month=manila_today().month; eid=f"event-{manila_today().year}-{month}"
        safe_reason = reason[:180]

        def operation(conn):
            conn.execute("INSERT OR IGNORE INTO event_progress(user_id,event_id,points) VALUES(?,?,0)",(user.id,eid))
            conn.execute("UPDATE event_progress SET points=points+? WHERE user_id=? AND event_id=?",(points,user.id,eid))
            return _add_xp_in_transaction(
                conn, user.id, user.display_name, points,
                f"Event points: {safe_reason}", manila_today(),
            )

        xp_result = await db.run_transaction(operation)
        logger.info(
            "Administrative event-points award actor_id=%s target_id=%s points=%s event_id=%s",
            interaction.user.id, user.id, points, eid,
        )
        await _publish_xp_result(user.id, interaction.guild, xp_result)
        await interaction.followup.send(f"\U0001f3c6 Awarded **+{points} event points** and **+{points} XP** to {user.mention}.\nReason: {reason[:200]}",ephemeral=True)

    @app_commands.command(name="sandbox", description="Open a no-grading coding mode reminder.")
    async def sandbox(self, interaction):
        await interaction.response.send_message(embed=UIEmbeds.standard("\U0001f9ea SANDBOX MODE","Experiment freely. Sandbox work should not affect grades or assignments. Run code in your own IDE/compiler, then use **Review My Code** in lessons or `/code-review` to get feedback. Use `/save-snippet` when you want to keep something."),ephemeral=True)

    @app_commands.command(name="tutor-mode", description="Choose how ClassCode's AI help should teach you.")
    @app_commands.choices(mode=[
        app_commands.Choice(name="Beginner \u2014 simple explanations",value="beginner"),
        app_commands.Choice(name="Socratic \u2014 questions first",value="socratic"),
        app_commands.Choice(name="Debugger \u2014 focus on bugs",value="debugger"),
        app_commands.Choice(name="Senior Developer \u2014 practical advice",value="senior")])
    async def tutor_mode(self, interaction, mode:app_commands.Choice[str]):
        await interaction.response.defer(ephemeral=True, thinking=True)
        def operation(conn):
            ensure_user_in_transaction(conn, interaction.user.id, interaction.user.display_name)
            conn.execute("INSERT OR IGNORE INTO personal_notes(user_id,title,body) VALUES(?,?,?)",(interaction.user.id,"AI Tutor Mode",mode.value))
        await db.run_transaction(operation)
        await interaction.followup.send(f"\U0001f916 Tutor mode set to **{mode.name}**. Your AI-help prompts can use this preference going forward.",ephemeral=True)

    @app_commands.command(name="certificate-verify", description="Verify a ClassCode certificate ID.")
    async def certificate_verify(self, interaction, certificate_id:str):
        await interaction.response.defer(ephemeral=True, thinking=True)
        r=await db.fetchone("SELECT c.certificate_id,c.language,c.issued_at,u.username FROM certificates c JOIN users u ON u.user_id=c.user_id WHERE c.certificate_id=?",(certificate_id.upper(),))
        if not r: await interaction.followup.send("\u274c Certificate ID not found.",ephemeral=True); return
        await interaction.followup.send(embed=UIEmbeds.standard("\u2705 CERTIFICATE VERIFIED",f"Certificate: `{r['certificate_id']}`\nStudent: **{r['username']}**\nTrack: **{r['language'].upper()}**\nIssued: **{r['issued_at']}**"),ephemeral=True)

    @app_commands.command(name="portfolio-add", description="Add a custom project entry to your portfolio.")
    async def portfolio_add(self, interaction, project_id:str, description:str="", url:str=""):
        await interaction.response.defer(ephemeral=True, thinking=True)
        p=await db.fetchone("SELECT project_id FROM projects WHERE project_id=?",(project_id,))
        if not p: await interaction.followup.send("\u274c Project ID not found. Use `/projects`.",ephemeral=True); return
        def operation(conn):
            ensure_user_in_transaction(conn, interaction.user.id, interaction.user.display_name)
            conn.execute("INSERT INTO portfolio_projects(user_id,project_id,description,url) VALUES(?,?,?,?)",(interaction.user.id,project_id,description,url))
        await db.run_transaction(operation)
        await interaction.followup.send("\U0001f4bc Portfolio entry added.",ephemeral=True)

class BugAnswerView(discord.ui.View):
    def __init__(self,puzzle_id):
        super().__init__(timeout=180); self.puzzle_id=puzzle_id
    @discord.ui.button(label="\U0001f4a1 Hint",style=discord.ButtonStyle.secondary)
    async def hint(self,interaction,button):
        await interaction.response.defer(ephemeral=True, thinking=True)
        r=await db.fetchone("SELECT answer FROM bug_puzzles WHERE puzzle_id=?",(self.puzzle_id,))
        if not r:
            await interaction.followup.send("This puzzle is no longer available.",ephemeral=True)
            return
        await interaction.followup.send(f"\U0001f4a1 Think about this condition/value: `{r['answer']}`",ephemeral=True)
    @discord.ui.button(label="\u2705 Mark Solved",style=discord.ButtonStyle.success)
    async def solved(self,interaction,button):
        await interaction.response.defer(ephemeral=True, thinking=True)
        r=await db.fetchone("SELECT explanation FROM bug_puzzles WHERE puzzle_id=?",(self.puzzle_id,))
        if not r:
            await interaction.followup.send("This puzzle is no longer available.",ephemeral=True)
            return

        def operation(conn):
            conn.execute("INSERT OR IGNORE INTO bug_attempts(user_id,puzzle_id) VALUES(?,?)",(interaction.user.id,self.puzzle_id))
            claimed = conn.execute(
                "UPDATE bug_attempts SET solved=1,attempts=attempts+1 WHERE user_id=? AND puzzle_id=? AND solved=0",
                (interaction.user.id,self.puzzle_id),
            ).rowcount == 1
            if not claimed:
                return False, None
            conn.execute("INSERT OR IGNORE INTO user_stats(user_id) VALUES(?)",(interaction.user.id,))
            conn.execute("UPDATE user_stats SET bugs_fixed=bugs_fixed+1 WHERE user_id=?",(interaction.user.id,))
            conn.execute("INSERT OR IGNORE INTO user_titles(user_id,title_id) VALUES(?,?)",(interaction.user.id,"debugger"))
            award = _add_xp_in_transaction(
                conn, interaction.user.id, interaction.user.display_name, 20,
                "Solved debugging puzzle", manila_today(),
            )
            return True, award

        claimed, xp_result = await db.run_transaction(operation)
        if not claimed:
            await interaction.followup.send("âœ… You already solved this puzzle. No extra XP was awarded.",ephemeral=True)
            return
        await _publish_xp_result(interaction.user.id, interaction.guild, xp_result)
        await award_badge(interaction.user.id,'bug_hunter',interaction.guild)
        await interaction.followup.send(f"\U0001f41b **Solved!**\n\n{r['explanation']}\n\n\U0001f3c6 +20 XP",ephemeral=True)

async def ensure_missions(user_id,today,username):
    missions=[('lessons',1,40),('quizzes',1,40),('bugs',1,50),('xp',100,60)]
    def operation(conn):
        ensure_user_in_transaction(conn, user_id, username)
        for kind,target,reward in missions:
            conn.execute("INSERT OR IGNORE INTO daily_missions(user_id,mission_date,kind,target,reward) VALUES(?,?,?,?,?)",(user_id,today,kind,target,reward))
    await db.run_transaction(operation)

async def setup(bot): await bot.add_cog(AcademyCog(bot))

