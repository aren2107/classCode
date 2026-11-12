import discord
from discord.ext import commands
from discord import app_commands
from bot.database import db
from bot.learning.mastery import ensure_user_in_transaction
from bot.services.invite_codes import new_invite_code, normalize_invite_code
from bot.ui.embeds import UIEmbeds, ColorPalette

class ClassesCog(commands.Cog):
    def __init__(self,bot): self.bot=bot

    @app_commands.command(name='class-create',description='Create a ClassCode class as a teacher/admin.')
    @app_commands.checks.has_permissions(manage_guild=True)
    async def class_create(self,interaction:discord.Interaction,name:str):
        await interaction.response.defer(ephemeral=True, thinking=True)
        class_id=new_invite_code()
        def operation(conn):
            ensure_user_in_transaction(conn, interaction.user.id, interaction.user.display_name)
            conn.execute('INSERT INTO classes(class_id,name,teacher_id) VALUES(?,?,?)',(class_id,name,interaction.user.id))
            conn.execute("INSERT INTO class_members(class_id,user_id,role) VALUES(?,?,?)",(class_id,interaction.user.id,'teacher'))
        await db.run_transaction(operation)
        await interaction.followup.send(embed=UIEmbeds.standard('\U0001f4da CLASS CREATED',f"**{name}**\n\nClass code: `{class_id}`\n\nShare this code with students so they can use `/class-join`."),ephemeral=True)

    @app_commands.command(name='class-join',description='Join a class with its class code.')
    @app_commands.checks.cooldown(3, 60.0, key=lambda interaction: interaction.user.id)
    async def class_join(self,interaction:discord.Interaction,class_code:str):
        await interaction.response.defer(ephemeral=True, thinking=True)
        normalized_code=normalize_invite_code(class_code)
        if not normalized_code:
            await interaction.followup.send('❌ Class code is invalid.',ephemeral=True)
            return
        def operation(conn):
            r=conn.execute('SELECT * FROM classes WHERE class_id=?',(normalized_code,)).fetchone()
            if not r:
                return None
            ensure_user_in_transaction(conn, interaction.user.id, interaction.user.display_name)
            conn.execute("INSERT OR IGNORE INTO class_members(class_id,user_id,role) VALUES(?,?,?)",(r['class_id'],interaction.user.id,'student'))
            return r
        r=await db.run_transaction(operation)
        if not r: await interaction.followup.send('\u274c Class code not found.',ephemeral=True); return
        await interaction.followup.send(f"\U0001f393 You joined **{r['name']}**.",ephemeral=True)

    @app_commands.command(name='my-classes',description='View your classes.')
    async def my_classes(self,interaction:discord.Interaction):
        await interaction.response.defer(ephemeral=True, thinking=True)
        rows=await db.fetchall('SELECT c.name,c.class_id,cm.role FROM classes c JOIN class_members cm ON c.class_id=cm.class_id WHERE cm.user_id=? ORDER BY c.created_at DESC',(interaction.user.id,))
        if not rows: await interaction.followup.send('You are not in a class yet. Use `/class-join` with a class code.',ephemeral=True); return
        desc='\n'.join(f"**{r['name']}** \u2014 `{r['class_id']}` \u2022 {r['role']}" for r in rows)
        await interaction.followup.send(embed=UIEmbeds.standard('\U0001f393 MY CLASSES',desc),ephemeral=True)

    @app_commands.command(name='class-dashboard',description='View class-level aggregate progress.')
    async def class_dashboard(self,interaction:discord.Interaction,class_code:str):
        await interaction.response.defer(ephemeral=True, thinking=True)
        c=await db.fetchone('SELECT * FROM classes WHERE class_id=?',(class_code.upper(),))
        if not c: await interaction.followup.send('\u274c Class not found.',ephemeral=True); return
        member=await db.fetchone('SELECT role FROM class_members WHERE class_id=? AND user_id=?',(c['class_id'],interaction.user.id))
        if not member or member['role'] not in ('teacher','student'):
            await interaction.followup.send('\u274c You are not a member of this class.',ephemeral=True); return
        count=await db.fetchone('SELECT COUNT(*) c FROM class_members WHERE class_id=?',(c['class_id'],))
        students=await db.fetchone("SELECT COUNT(*) c FROM class_members WHERE class_id=? AND role='student'",(c['class_id'],))
        avg=await db.fetchone("SELECT COALESCE(AVG(u.xp),0) avg FROM users u JOIN class_members cm ON u.user_id=cm.user_id WHERE cm.class_id=? AND cm.role='student'",(c['class_id'],))
        await interaction.followup.send(embed=UIEmbeds.standard(f"\U0001f4ca {c['name']}",f"Students: **{students['c']}**\nMembers: **{count['c']}**\nAverage student XP: **{round(avg['avg'])}**\n\nUse `/class-assign` to create an assignment."),ephemeral=True)

    @app_commands.command(name='class-assign',description='Create a class assignment.')
    @app_commands.checks.has_permissions(manage_guild=True)
    @app_commands.choices(language=[app_commands.Choice(name='C++',value='cpp'),app_commands.Choice(name='Java',value='java')])
    async def class_assign(self,interaction:discord.Interaction,class_code:str,title:str,language:app_commands.Choice[str],topic_id:str=None,due_date:str=None):
        await interaction.response.defer(ephemeral=True, thinking=True)
        c=await db.fetchone('SELECT * FROM classes WHERE class_id=?',(class_code.upper(),))
        if not c: await interaction.followup.send('\u274c Class not found.',ephemeral=True); return
        if c['teacher_id']!=interaction.user.id and not interaction.user.guild_permissions.manage_guild:
            await interaction.followup.send('\u274c Only the class teacher/admin can create assignments.',ephemeral=True); return
        await db.execute('INSERT INTO assignments(class_id,title,language,topic_id,due_date) VALUES(?,?,?,?,?)',(c['class_id'],title,language.value,topic_id,due_date))
        await interaction.followup.send(embed=UIEmbeds.standard('\U0001f4dd ASSIGNMENT CREATED',f"**{title}**\nClass: {c['name']}\nLanguage: {language.name}\nTopic: `{topic_id or 'General'}`\nDue: `{due_date or 'No due date'}`",ColorPalette.SUCCESS),ephemeral=True)

async def setup(bot): await bot.add_cog(ClassesCog(bot))
