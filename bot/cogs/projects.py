import discord
from discord.ext import commands
from discord import app_commands
from bot.database import db
from datetime import date
from bot.timezone import manila_today
from bot.learning.mastery import _complete_project_in_transaction, _publish_xp_result, award_badge
from bot.ui.embeds import UIEmbeds, ColorPalette

PROJECTS=[
{"id":"cpp-cli-calculator","title":"C++ CLI Calculator","language":"cpp","difficulty":"\U0001f7e2 Beginner","description":"Build a calculator that validates input and handles division by zero.","requirements":["Read two numbers","Read an operator","Validate the operator","Handle division by zero","Repeat until exit"],"xp":150},
{"id":"java-guessing-game","title":"Java Number Guessing Game","language":"java","difficulty":"\U0001f7e2 Beginner","description":"Build a console game using loops, conditions, random numbers, and counters.","requirements":["Generate a secret number","Loop until correct","Count attempts","Validate guesses","Show a final result"],"xp":150},
{"id":"cpp-grade-analyzer","title":"C++ Grade Analyzer","language":"cpp","difficulty":"\U0001f7e2 Beginner","description":"Analyze a collection of student scores and report statistics.","requirements":["Read scores","Calculate average","Find minimum and maximum","Count passing scores","Validate score range"],"xp":200},
{"id":"java-task-list","title":"Java Task List","language":"java","difficulty":"\U0001f7e2 Beginner","description":"Build a menu-driven task list using ArrayList and methods.","requirements":["Add tasks","Complete tasks","Remove tasks","List tasks","Validate menu choices"],"xp":200},
{"id":"cpp-student-system","title":"C++ Student Management System","language":"cpp","difficulty":"\U0001f7e1 Intermediate","description":"Create a menu-driven record system using structs/classes, vectors, searching, and validation.","requirements":["Add students","List students","Search students","Update students","Delete students","Validate grades"],"xp":350},
{"id":"java-inventory-system","title":"Java Inventory System","language":"java","difficulty":"\U0001f7e1 Intermediate","description":"Build an inventory manager using classes, collections, validation, and file persistence.","requirements":["Add products","Search products","Update stock","Sell products","Persist data","Handle invalid input"],"xp":400},
{"id":"cpp-file-database","title":"C++ File-Based Database","language":"cpp","difficulty":"\U0001f7e1 Intermediate","description":"Build a small record database using classes, vectors, searching, sorting, and files.","requirements":["CRUD records","Search","Sort","Save","Load","Validate records"],"xp":450},
{"id":"java-oop-library","title":"Java OOP Library System","language":"java","difficulty":"\U0001f7e1 Intermediate","description":"Use encapsulation, inheritance, interfaces, collections, and exceptions in a library application.","requirements":["Book/member classes","Borrow and return","Late validation","Search","Exception handling","Reports"],"xp":500},
{"id":"cpp-algorithm-lab","title":"C++ Algorithm Lab","language":"cpp","difficulty":"\U0001f534 Advanced","description":"Compare searching and sorting algorithms and report correctness and complexity.","requirements":["Implement multiple algorithms","Test identical inputs","Measure operations","Explain complexity","Compare results"],"xp":600},
{"id":"java-concurrent-worker","title":"Java Concurrent Worker","language":"java","difficulty":"\U0001f534 Advanced","description":"Process independent jobs with ExecutorService while keeping shared state safe.","requirements":["Create jobs","Use ExecutorService","Collect results","Handle failures","Avoid unsafe shared state","Shutdown cleanly"],"xp":650},
{"id":"cpp-graph-explorer","title":"C++ Graph Explorer","language":"cpp","difficulty":"\U0001f534 Advanced","description":"Represent a graph and implement BFS/DFS with a clear traversal report.","requirements":["Build graph","Add edges","BFS","DFS","Visited tracking","Explain complexity"],"xp":700},
{"id":"java-capstone","title":"Java Full Console Capstone","language":"java","difficulty":"\U0001f534 Advanced","description":"Design a complete application from a written specification using OOP, collections, persistence, validation, testing, and documentation.","requirements":["Requirements breakdown","OOP design","Collections","Persistence","Validation","Tests","Error handling","Final documentation"],"xp":1000},
]

async def seed():
    for p in PROJECTS:
        await db.execute(
            "INSERT INTO projects(project_id,title,language,difficulty,description,requirements,xp) VALUES(?,?,?,?,?,?,?) "
            "ON CONFLICT(project_id) DO UPDATE SET title=excluded.title,language=excluded.language,difficulty=excluded.difficulty,description=excluded.description,requirements=excluded.requirements,xp=excluded.xp",
            (p['id'],p['title'],p['language'],p['difficulty'],p['description'],'\n'.join(p['requirements']),p['xp'])
        )

class ProjectsCog(commands.Cog):
    def __init__(self,bot): self.bot=bot
    @app_commands.command(name='projects',description='Browse ClassCode coding projects.')
    async def projects(self,interaction:discord.Interaction):
        await interaction.response.defer(ephemeral=False, thinking=True)
        await seed(); rows=await db.fetchall('SELECT * FROM projects')
        order={p['id']: i+1 for i,p in enumerate(PROJECTS)}
        rows=sorted(rows, key=lambda r: order.get(r['project_id'], 999))
        desc='\n\n'.join(
            f"**ID: {order[r['project_id']]}**\n**Name:** {r['title']}\n"
            f"{r['language'].upper()} {r['difficulty']} \u2022 `{r['xp']} XP`\n"
            f"{r['description']}"
            for r in rows
        )
        await interaction.followup.send(embed=UIEmbeds.standard('\U0001f3d7\ufe0f PROJECT LAB',desc))

    @app_commands.command(name='project',description='Open a coding project by its numeric ID.')
    @app_commands.describe(id='Project ID from /projects (1-12)')
    async def project(self,interaction:discord.Interaction,id:int):
        await interaction.response.defer(ephemeral=False, thinking=True)
        await seed()
        if id < 1 or id > len(PROJECTS):
            await interaction.followup.send(f'\u274c Invalid project ID. Use a number from 1 to {len(PROJECTS)}.',ephemeral=True)
            return
        project_id=PROJECTS[id-1]['id']
        r=await db.fetchone('SELECT * FROM projects WHERE project_id=?',(project_id,))
        if not r: await interaction.followup.send('\u274c Project not found. Use `/projects` first.',ephemeral=True); return
        embed=UIEmbeds.standard(f"\U0001f3d7\ufe0f {r['title']}",f"**ID:** `{id}`\n**Language:** {r['language'].upper()}\n**Difficulty:** {r['difficulty']}\n**Reward:** `{r['xp']} XP`\n\n{r['description']}\n\n**Requirements**\n{r['requirements']}")
        await interaction.followup.send(embed=embed)
    @app_commands.command(name='project-complete',description='Mark a project complete after finishing it.')
    async def project_complete(self,interaction:discord.Interaction,project_id:str):
        await interaction.response.defer(ephemeral=False, thinking=True)
        await seed(); r=await db.fetchone('SELECT * FROM projects WHERE project_id=?',(project_id,))
        if not r: await interaction.followup.send('\u274c Project not found.',ephemeral=True); return

        today = manila_today()

        def operation(conn):
            xp_result = _complete_project_in_transaction(
                conn, interaction.user.id, interaction.user.display_name,
                project_id, r['xp'], r['title'], today,
            )
            return xp_result is not None, xp_result

        claimed, xp_result = await db.run_transaction(operation)
        if not claimed:
            await interaction.followup.send('\u2139\ufe0f Project already completed; no additional XP was awarded.',ephemeral=True)
            return
        await _publish_xp_result(interaction.user.id,interaction.guild,xp_result)
        await award_badge(interaction.user.id,'project_builder',interaction.guild)
        await interaction.followup.send(embed=UIEmbeds.standard('\U0001f389 PROJECT COMPLETED',f"**{r['title']}** completed!\n\n\U0001f3c6 **+{r['xp']} XP**",ColorPalette.SUCCESS))


async def setup(bot): await bot.add_cog(ProjectsCog(bot))
