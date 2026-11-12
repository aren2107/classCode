import discord
from discord.ext import commands
from discord import app_commands
import logging
from bot.ui.embeds import UIEmbeds, ColorPalette
from bot.ui.views import TopicSelectView
from bot.database import db

ROLE_NAMES = {"unverified": "Unverified", "student": "Student", "admin": "Admin"}
logger = logging.getLogger(__name__)


def is_server_admin(member: discord.Member) -> bool:
    """Use Discord's authoritative guild permissions for privileged actions."""
    return member.id == member.guild.owner_id or member.guild_permissions.administrator


def bot_channel_overwrite(guild: discord.Guild) -> discord.PermissionOverwrite:
    """Give the ClassCode bot explicit access even when @everyone is denied."""
    return discord.PermissionOverwrite(
        view_channel=True,
        send_messages=True,
        read_message_history=True,
        embed_links=True,
        attach_files=True,
        add_reactions=True,
        manage_messages=True,
        manage_threads=True,
        create_public_threads=True,
        send_messages_in_threads=True,
    )

CHANNEL_GUIDES = {
    "welcome": ("\U0001f44b Welcome to ClassCode!", "ClassCode is your beginner-friendly Discord classroom for learning C++ and Java step by step.", "**Start here:** `#rules` \u2192 `#verify` \u2192 `#questionnaire` \u2192 `#how-to-start` \u2192 use `/start`.\n\n**If you are completely new to programming:** choose **Beginner** in the questionnaire. You do not need prior coding experience."),
    "rules": ("\U0001f4dc Server Rules", "Keep ClassCode safe, respectful, and focused on learning.", "1. Be respectful.\n2. Do not spam or disrupt lessons.\n3. Use the channel that matches your question.\n4. Do not share passwords, tokens, or private information.\n5. Do not use ClassCode to cheat on real exams or assignments.\n6. Follow Discord's Terms of Service."),
    "verify": ("\U0001f512 Verification", "Click the button below to become a verified Student and unlock the learning areas.", "**New member:** click **Verify & Become a Student**.\n\nIf verification fails, tell an admin. Do not repeatedly click the button."),
    "questionnaire": ("\U0001f4dd Your Learning Profile", "Answer the three short questions so ClassCode can guide you to the right starting point.", "Choose your **language**, **experience**, and **goal**.\n\n**Beginner?** Pick Beginner even if you have only watched tutorials. You can change your path later."),
    "announcements": ("\U0001f4e2 ClassCode Announcements", "Official updates about lessons, maintenance, events, practical exams, deadlines, and new features are posted here.", "**Students:** read this channel regularly. No commands are normally needed here.\n\n**Admins:** use the admin tools to manage announcements."),
    "how-to-start": ("\U0001f680 Your First 10 Minutes", "Follow this simple path. You do not need to understand every ClassCode command.", "**1.** Verify in `#verify`\n**2.** Finish `#questionnaire`\n**3.** Type `/start`\n**4.** Pick C++ or Java\n**5.** Open the first roadmap lesson\n**6.** Read the example and complete the exercise\n**7.** Use **Review My Code** in a lesson to get feedback on your implementation\n**8.** When ready, try the quiz\n\n**Stuck?** Use `/hint` or `/explain` in the matching help channel."),
    "tickets": ("\U0001f3ab Help & Support", "Use this channel when you need help with the ClassCode server itself, verification, permissions, or a broken bot feature.", "For programming questions, use `#cpp-help` or `#java-help` instead.\n\n**Server issue:** describe what happened and include the command you used. Never post passwords or API keys."),
    "general": ("\U0001f4ac General", "A friendly place to talk about programming, school, technology, and your learning journey.", "**Commands:** `/study-groups` to browse groups, `/study-group-create` to start one, `/study-group-join` to join one.\n\nFor code questions, move to the language help channel."),
    "memes": ("\U0001f602 Programming Memes", "Share coding memes and jokes without burying important learning conversations.", "**Commands:** none required. Keep memes appropriate and avoid spam."),
    "gaming": ("\U0001f3ae Gaming", "Talk about games and relax with other students.", "**Commands:** none required. Keep programming help in the appropriate learning channel."),
    "ideas-and-suggestions": ("\U0001f4a1 Ideas & Suggestions", "Suggest improvements for ClassCode, new lessons, challenges, channels, or features.", "**Commands:** none required. Explain the idea and why it would help students."),
    "projects-showcase": ("\U0001f3c6 Projects Showcase", "Show classmates what you built and celebrate progress.", "**Commands:** `/portfolio` to view your portfolio. You can also share screenshots, demos, and project links."),
    "bot-commands": ("\U0001f916 ClassCode Command Center", "This is the main place to use slash commands. Beginners should start with `/start` instead of trying to learn every command at once.", "**Start:** `/start`\n**Learning:** `/cpp-roadmap`, `/java-roadmap`\n**Practice:** `/cpp-quiz`, `/java-quiz`, `/daily-challenge`\n**Code:** `/hint`, `/explain`, `/code-review`, `/explain-error`\n**Progress:** `/dashboard`, `/profile`, `/progress`, `/mastery`, `/skill-tree`\n**Projects:** `/projects`, `/project`\n**Notes:** `/save-snippet`, `/my-snippets`, `/note`, `/notes`\n**Help:** `/help`"),
    "cpp": ("\U0001f7e6 C++ Classroom", "Learn and discuss C++ concepts, syntax, logic, and programming problems.", "**Main commands:** `/cpp-roadmap` to learn \u2022 `/cpp-quiz` to check understanding \u2022 **Review My Code** for feedback.\n\nFor mistakes or questions, use `#cpp-help`. For feedback on your code, use `#cpp-code-review`."),
    "cpp-help": ("\U0001f198 C++ Help", "Ask beginner-friendly C++ questions and get guidance without immediately receiving the full solution.", "**Use:** `/hint` for a small clue \u2022 `/explain` for a simple concept explanation \u2022 `/explain-error` for compiler/runtime errors.\n\nInclude the error message and the small part of code causing the problem when possible."),
    "cpp-code-review": ("\U0001f50e C++ Code Review", "Get constructive feedback on your C++ code: readability, logic, bugs, and possible improvements.", "**Use:** `/code-review` with `language: cpp` and your code.\n\nYour code is sent to the configured AI service for feedback. Never include passwords, API keys, tokens, or private information."),
    "java": ("\u2615 Java Classroom", "Learn Java step by step, from variables and conditions to methods, classes, collections, and larger programs.", "**Main commands:** `/java-roadmap` to learn \u2022 `/java-quiz` to check understanding \u2022 **Review My Code** for feedback.\n\nFor mistakes or questions, use `#java-help`. For feedback, use `#java-code-review`."),
    "java-help": ("\U0001f198 Java Help", "Ask beginner-friendly Java questions and get guidance while you learn to debug your own code.", "**Use:** `/hint` for a clue \u2022 `/explain` for concepts \u2022 `/explain-error` for compiler/runtime errors.\n\nPaste the exact error and the smallest useful code section."),
    "java-code-review": ("\U0001f50e Java Code Review", "Get constructive feedback on your Java code without having the whole program rewritten for you.", "**Use:** `/code-review` with `language: java` and your code.\n\nYour code is sent to the configured AI service for feedback. Never include passwords, API keys, tokens, or private information."),
    "playground": ("\U0001f4bb Coding Playground", "A safe place to experiment with small C++ and Java programs.", "**This area is for coding discussion and experimentation.\n\nUse your own IDE/compiler to run programs, then bring your code here for feedback with **Review My Code**. **Never paste passwords, API keys, tokens, or private data.**"),
    "daily-challenge": ("\U0001f525 Daily Challenge", "One small coding challenge to practice what you have learned.", "**Use:** `/daily-challenge` to read the task, then `/submit-challenge` to submit your code.\n\nIf you are stuck, practice the related roadmap topic first."),
    "cpp-roadmap": ("\U0001f5fa\ufe0f C++ Roadmap", "Your C++ lessons are ordered from beginner fundamentals to more advanced programming skills.", "**Use:** `/cpp-roadmap`\n\nStart with the first unlocked topic. Read the explanation, study the syntax example, then complete the exercise before moving on."),
    "java-roadmap": ("\U0001f5fa\ufe0f Java Roadmap", "Your Java lessons are ordered so a complete beginner can build knowledge one topic at a time.", "**Use:** `/java-roadmap`\n\nStart with the first unlocked topic. Do not worry about advanced topics until the basics are comfortable."),
    "cpp-quiz": ("\U0001f4dd C++ Quiz", "Check your understanding after studying C++ lessons.", "**Use:** `/cpp-quiz`\n\nTry the quiz after completing some roadmap topics. A wrong answer is practice, not failure."),
    "java-quiz": ("\U0001f4dd Java Quiz", "Check your understanding after studying Java lessons.", "**Use:** `/java-quiz`\n\nReview the related roadmap lesson whenever a question feels unfamiliar."),
    "leaderboard": ("\U0001f3c6 Leaderboard", "See XP rankings and celebrate progress without treating the leaderboard as a requirement.", "**Use:** `/leaderboard`\n\nYour goal is to learn, not just to collect XP."),
    "achievements": ("\U0001f389 Achievements", "Badges and milestones earned while learning are celebrated here.", "**Useful commands:** `/profile`, `/titles`, `/xp-history`."),
    "certificates": ("\U0001f4dc Certificates", "Certificates are available after completing an entire language track.", "**Use:** `/certificate` when you meet the completion requirement.\n**Verify a certificate:** `/certificate-verify`."),
    "attendance": ("\U0001f4c5 ClassCode Daily Attendance", "Check in once each day to track your attendance streak and consistency.", "**Use:** `/attendance` in this channel once per day. Missing a calendar day resets your current streak; your next check-in starts a new streak at 1. Your first attendance date and total check-ins are saved."),
    "project-ideas": ("\U0001f4a1 Project Ideas", "Find practical projects that help turn lessons into real programs.", "**Use:** `/projects` to browse projects and `/project` to open a project blueprint."),
    "project-help": ("\U0001f3d7\ufe0f Project Help", "Ask for help planning or debugging larger projects.", "**Useful commands:** `/project`, `/hint`, `/code-review`.\n\nShare your goal, what you tried, and where you are stuck."),
    "music": ("\U0001f3b5 Music", "A relaxed space for music while you study or code.", "**Commands:** none required."),
    "bot-spam": ("\U0001f916 Bot Playground", "Use this channel for harmless bot experiments that would otherwise clutter normal channels.", "**Commands:** most general ClassCode commands are fine here. For a beginner learning path, use `/start`."),
    "mod-logs": ("\U0001f6e1\ufe0f Moderator Logs", "Restricted moderation and access-control logs.", "**Admins only.** Students do not need to use commands here."),
    "bot-logs": ("\u2699\ufe0f Bot Logs", "Restricted ClassCode system and bot logs.", "**Admins only.** Students do not need to use commands here."),
    "exam-admin": ("\U0001f9d1\u200d\U0001f3eb Practical Exam Admin", "Restricted area for teachers/admins to create, grade, close, and review practical examinations.", "**Admin commands:** `/exam-create` \u2022 `/exam-grade` \u2022 `/exam-results` \u2022 `/exam-close`\n\nStudents should never need to use commands in this channel."),
}


STRUCTURE = {
    "\U0001f4e2 START HERE": ["welcome", "rules", "verify", "questionnaire", "announcements", "how-to-start", "tickets"],
    "\U0001f4ac COMMUNITY": ["general", "memes", "gaming", "ideas-and-suggestions", "projects-showcase", "bot-commands"],
    "\U0001f7e6 C++ PROGRAMMING": ["cpp", "cpp-help", "cpp-code-review", "cpp-roadmap", "cpp-quiz"],
    "\u2615 JAVA PROGRAMMING": ["java", "java-help", "java-code-review", "java-roadmap", "java-quiz"],
    "\U0001f4bb PROGRAMMING LAB": ["playground", "daily-challenge"],
    "\U0001f3c6 PROGRESS": ["leaderboard", "achievements", "certificates", "attendance"],
    "\U0001f3d7\ufe0f PROJECTS": ["project-ideas", "project-help"],
    "\U0001f3b5 ENTERTAINMENT": ["music", "bot-spam"],
    "\U0001f6e1\ufe0f ADMIN LOGS": ["mod-logs", "bot-logs", "exam-admin"],
}

# Older ClassCode releases used these combined categories. During `/setup`,
# their managed channels are moved into the new language-specific categories.
LEGACY_CATEGORIES = {"\U0001f4bb PROGRAMMING", "\U0001f5fa\ufe0f LEARNING"}


async def ensure_roles(guild: discord.Guild):
    roles = {}
    for key, name in ROLE_NAMES.items():
        role = discord.utils.get(guild.roles, name=name)
        if role is None:
            permissions = discord.Permissions.none()
            role = await guild.create_role(name=name, permissions=permissions, reason="ClassCode role setup")
        roles[key] = role
    return roles


async def assign_join_role(member: discord.Member):
    try:
        roles = await ensure_roles(member.guild)
        # Existing server administrators also receive the named Admin role.
        if is_server_admin(member):
            await member.add_roles(roles["admin"], reason="ClassCode administrator role sync")
            if roles["unverified"] in member.roles:
                await member.remove_roles(roles["unverified"], reason="ClassCode admin role sync")
        elif roles["student"] not in member.roles:
            await member.add_roles(roles["unverified"], reason="ClassCode new member verification")
    except discord.Forbidden:
        # The bot must have Manage Roles and its bot role must be above these roles.
        pass


class VerifyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Verify & Become a Student", style=discord.ButtonStyle.success, custom_id="classcode_verify_button", emoji="\u2705")
    async def verify_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        if not guild:
            await interaction.response.send_message("This button can only be used inside a server.", ephemeral=True)
            return
        await interaction.response.defer(ephemeral=True, thinking=True)
        try:
            roles = await ensure_roles(guild)
            member = interaction.user
            if not isinstance(member, discord.Member):
                await interaction.followup.send("❌ Unable to verify your server membership. Please try again.", ephemeral=True)
                return
            if is_server_admin(member):
                await interaction.followup.send("\U0001f6e1\ufe0f You already have administrator access.", ephemeral=True)
                return
            if roles["student"] in member.roles:
                await interaction.followup.send("\u2139\ufe0f You are already verified as a Student.", ephemeral=True)
                return
            await member.add_roles(roles["student"], reason="ClassCode verification")
            if roles["unverified"] in member.roles:
                await member.remove_roles(roles["unverified"], reason="ClassCode verification")
            await interaction.followup.send("\U0001f389 **Verification successful!** You are now a **Student** and can access the learning channels.", ephemeral=True)
        except discord.Forbidden:
            await interaction.followup.send("\u274c I cannot manage the roles. Make sure the bot has **Manage Roles** and its role is above Unverified/Student/Admin.", ephemeral=True)
        except discord.HTTPException:
            logger.exception("Discord API failure while verifying member %s in guild %s", interaction.user.id, guild.id)
            await interaction.followup.send("❌ Discord could not complete verification. Please try again later.", ephemeral=True)


class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        await assign_join_role(member)

    async def configure_category_permissions(self, guild: discord.Guild, category: discord.CategoryChannel, roles: dict, admin_only=False, start_here=False):
        everyone = guild.default_role
        overwrites = {everyone: discord.PermissionOverwrite(view_channel=False)}
        if guild.me:
            overwrites[guild.me] = bot_channel_overwrite(guild)
        if not admin_only:
            allow = discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True)
            overwrites[roles["student"]] = allow
            # Unverified members are intentionally blocked at category level.
            # The #verify channel gets a specific exception below.
        try:
            await category.edit(overwrites=overwrites, reason="ClassCode access control")
        except discord.Forbidden:
            pass

    async def configure_channel_permissions(self, guild: discord.Guild, channel: discord.TextChannel, roles: dict, *, verify_only=False, admin_only=False):
        """Apply the final per-channel visibility rules.

        Unverified members can see only #verify. Student members can see
        normal learning/community channels; Discord administrators bypass the
        channel deny. The bot always keeps explicit access.
        """
        everyone = guild.default_role
        overwrites = {everyone: discord.PermissionOverwrite(view_channel=False)}
        if guild.me:
            overwrites[guild.me] = bot_channel_overwrite(guild)

        if not admin_only:
            member_allow = discord.PermissionOverwrite(
                view_channel=True, send_messages=True, read_message_history=True
            )
            overwrites[roles["student"]] = member_allow
            if verify_only:
                overwrites[roles["unverified"]] = member_allow

        try:
            await channel.edit(overwrites=overwrites, reason="ClassCode verification access control")
        except discord.Forbidden:
            pass

    async def post_questionnaire_panel(self, guild: discord.Guild):
        channel = discord.utils.get(guild.text_channels, name="questionnaire")
        if not channel:
            return False
        embed = UIEmbeds.standard("\U0001f4dd START HERE \u2014 QUESTIONNAIRE", "Complete your learner profile before starting the roadmap. Your answers help ClassCode personalize your practice.")
        embed.add_field(name="Questions", value="1. Which language are you learning?\n2. What is your current experience level?\n3. What is your main learning goal?", inline=False)
        from bot.cogs.academy import QuestionnaireView
        if self.bot.user:
            async for message in channel.history(limit=50):
                if message.author.id == self.bot.user.id and message.embeds and message.embeds[0].title == "\U0001f4dd START HERE \u2014 QUESTIONNAIRE":
                    await message.edit(embed=embed, view=QuestionnaireView())
                    return True
        await channel.send(embed=embed, view=QuestionnaireView())
        return True

    async def post_channel_guides(self, guild: discord.Guild, only_empty: bool = True):
        """Post the beginner-friendly guide in each configured channel."""
        posted = 0
        for category_name, channels in STRUCTURE.items():
            category = discord.utils.get(guild.categories, name=category_name)
            if not category:
                continue
            for ch_name in channels:
                channel = discord.utils.get(category.text_channels, name=ch_name)
                guide = CHANNEL_GUIDES.get(ch_name)
                if not channel or not guide:
                    continue
                title, desc, *extra = guide
                embed = UIEmbeds.standard(title, desc)
                if extra:
                    embed.add_field(name="\U0001f4a1 How to use this channel", value=extra[0].replace("\\n", "\n"), inline=False)
                try:
                    # On an existing ClassCode server, refresh the bot's previous guide
                    # instead of leaving outdated instructions behind.
                    refreshed = False
                    if only_empty and self.bot.user:
                        async for message in channel.history(limit=25):
                            if message.author.id == self.bot.user.id and message.embeds and message.embeds[0].title == title:
                                await message.edit(embed=embed)
                                refreshed = True
                                posted += 1
                                break
                    if refreshed:
                        continue
                    if only_empty:
                        has_message = False
                        async for _ in channel.history(limit=1):
                            has_message = True
                            break
                        if has_message:
                            continue
                    await channel.send(embed=embed)
                    posted += 1
                except discord.Forbidden:
                    continue
        return posted

    @app_commands.command(name="setup", description="Create ClassCode roles, channels, permissions, guides, and roadmaps.")
    @app_commands.checks.has_permissions(manage_channels=True, manage_roles=True)
    async def setup_server(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        guild = interaction.guild
        roles = await ensure_roles(guild)
        # Sync existing admins into the named Admin role.
        for member in guild.members:
            if is_server_admin(member):
                try:
                    await member.add_roles(roles["admin"], reason="ClassCode admin role sync")
                except discord.Forbidden:
                    pass

        created_count = 0
        moved_count = 0
        for category_name, channels in STRUCTURE.items():
            category = discord.utils.get(guild.categories, name=category_name)
            if not category:
                category = await guild.create_category(category_name, reason="ClassCode server setup")
                created_count += 1
            is_admin = category_name == "\U0001f6e1\ufe0f ADMIN LOGS"
            is_start = category_name == "\U0001f4e2 START HERE"
            await self.configure_category_permissions(guild, category, roles, admin_only=is_admin, start_here=is_start)
            for ch_name in channels:
                # Find an existing ClassCode channel anywhere in the server so
                # `/setup` migrates the old layout instead of creating duplicates.
                channel = discord.utils.get(guild.text_channels, name=ch_name)
                if channel is None:
                    channel = await guild.create_text_channel(
                        ch_name, category=category, reason="ClassCode server setup"
                    )
                    created_count += 1
                elif channel.category_id != category.id:
                    try:
                        await channel.edit(category=category, reason="ClassCode language category migration")
                        moved_count += 1
                    except discord.Forbidden:
                        pass

                # Verification is the only ClassCode channel visible to an
                # unverified member. Once verified, Student access unlocks the
                # rest of the server.
                await self.configure_channel_permissions(
                    guild,
                    channel,
                    roles,
                    verify_only=(ch_name == "verify"),
                    admin_only=is_admin,
                )

        # Remove only the two old ClassCode categories when they became empty.
        # Never delete a category containing another channel.
        for legacy_name in LEGACY_CATEGORIES:
            legacy = discord.utils.get(guild.categories, name=legacy_name)
            if legacy and not legacy.channels:
                try:
                    await legacy.delete(reason="Remove obsolete ClassCode category after language migration")
                except discord.Forbidden:
                    pass
        await self.post_channel_guides(guild, only_empty=True)
        await self.post_roadmaps(guild)
        await self.post_verify_panel(guild)
        await self.post_questionnaire_panel(guild)
        tickets_cog = self.bot.get_cog("Tickets")
        if tickets_cog:
            await tickets_cog.post_ticket_panel(guild)
        embed = UIEmbeds.standard("\u2705 ClassCode Setup Complete", f"Created/updated **{created_count}** server elements and moved **{moved_count}** existing channels into the new category structure.\n\n**Roles:** `Unverified` \u2192 `Student` | `Admin`\n\nNew members automatically receive **Unverified**. Clicking Verify removes Unverified and adds **Student**.", ColorPalette.SUCCESS)
        await interaction.followup.send(embed=embed, ephemeral=True)

    async def post_roadmaps(self, guild: discord.Guild):
        for name, language in (("cpp-roadmap", "cpp"), ("java-roadmap", "java")):
            channel = discord.utils.get(guild.text_channels, name=name)
            if not channel:
                continue
            title = f"{'\U0001f7e6 C++' if language == 'cpp' else '\u2615 Java'} Learning Roadmap"
            embed = UIEmbeds.standard(title, "Select a topic to study it. Complete topics in order to unlock the next lesson and earn XP.")
            existing = None
            if self.bot.user:
                async for message in channel.history(limit=25):
                    if message.author.id == self.bot.user.id and message.embeds and message.embeds[0].title == title:
                        existing = message
                        break
            if existing:
                await existing.edit(embed=embed, view=TopicSelectView(language, 0))
            else:
                await channel.send(embed=embed, view=TopicSelectView(language, 0))

    async def post_verify_panel(self, guild: discord.Guild):
        channel = discord.utils.get(guild.text_channels, name="verify")
        if not channel:
            return False
        embed = UIEmbeds.standard("\U0001f512 CLASSCODE VERIFICATION", "New members start with the **Unverified** role and can see only this channel.\n\nClick **Verify & Become a Student** to remove `Unverified` and receive `Student` access to the rest of ClassCode.", ColorPalette.PRIMARY)
        if self.bot.user:
            async for message in channel.history(limit=50):
                if message.author.id == self.bot.user.id and message.embeds and message.embeds[0].title == "\U0001f512 CLASSCODE VERIFICATION":
                    await message.edit(embed=embed, view=VerifyView())
                    return True
        await channel.send(embed=embed, view=VerifyView())
        return True

    @app_commands.command(name="setup-content", description="Post missing beginner-friendly channel guides.")
    @app_commands.checks.has_permissions(manage_channels=True)
    async def setup_content(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        guild = interaction.guild
        posted = await self.post_channel_guides(guild, only_empty=True)
        questionnaire = discord.utils.get(guild.text_channels, name="questionnaire")
        questionnaire_posted = 0
        if questionnaire:
            # Refresh the ClassCode questionnaire panel without duplicating it.
            async for message in questionnaire.history(limit=25):
                if message.author == self.bot.user and message.embeds and message.embeds[0].title == "\U0001f4dd START HERE \u2014 QUESTIONNAIRE":
                    from bot.cogs.academy import QuestionnaireView
                    await message.edit(view=QuestionnaireView())
                    questionnaire_posted = 1
                    break
            else:
                await self.post_questionnaire_panel(guild)
                questionnaire_posted = 1

        # Also create/refresh the real ticket button panel. The channel guide above
        # only explains support; the Tickets cog owns the interactive buttons.
        ticket_panel = 0
        tickets_cog = self.bot.get_cog("Tickets")
        if tickets_cog:
            ticket_panel = int(await tickets_cog.post_ticket_panel(guild))

        await interaction.followup.send(
            f"\u2705 Beginner content checked. Updated **{posted}** guide panel(s), **{questionnaire_posted}** questionnaire panel, and **{ticket_panel}** ticket panel.",
            ephemeral=True,
        )

    @app_commands.command(name="setup-verify", description="Post the verification panel and ensure ClassCode roles exist.")
    @app_commands.checks.has_permissions(manage_roles=True)
    async def setup_verify(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        await ensure_roles(interaction.guild)
        channel = discord.utils.get(interaction.guild.text_channels, name="verify") or interaction.channel
        embed = UIEmbeds.standard("\U0001f512 CLASSCODE VERIFICATION", "Click **Verify & Become a Student** to replace your `Unverified` role with `Student` access.", ColorPalette.PRIMARY)
        await channel.send(embed=embed, view=VerifyView())
        await interaction.followup.send(f"\u2705 Verification panel posted in {channel.mention}.", ephemeral=True)

    @app_commands.command(name="setup-roadmaps", description="Post fresh C++ and Java roadmap panels.")
    @app_commands.checks.has_permissions(manage_channels=True)
    async def setup_roadmaps_cmd(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        await self.post_roadmaps(interaction.guild)
        await interaction.followup.send("\u2705 Roadmap panels posted.", ephemeral=True)

    @app_commands.command(name="sync-roles", description="Create ClassCode roles and sync existing members.")
    @app_commands.checks.has_permissions(manage_roles=True)
    async def sync_roles(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        roles = await ensure_roles(interaction.guild)
        added = 0
        for member in interaction.guild.members:
            try:
                if is_server_admin(member):
                    if roles["admin"] not in member.roles:
                        await member.add_roles(roles["admin"], reason="ClassCode role sync")
                        added += 1
                elif roles["student"] not in member.roles and roles["unverified"] not in member.roles:
                    await member.add_roles(roles["unverified"], reason="ClassCode role sync")
                    added += 1
            except discord.Forbidden:
                continue
        await interaction.followup.send(f"\u2705 Roles ready. Updated **{added}** members.", ephemeral=True)

    @staticmethod
    def _can_assign_lesson(interaction: discord.Interaction) -> bool:
        member = interaction.user
        return (
            interaction.guild is not None
            and isinstance(member, discord.Member)
            and is_server_admin(member)
        )

    async def _lesson_autocomplete(self, interaction: discord.Interaction, current: str):
        language = "java" if interaction.command and interaction.command.name == "student-set-java" else "cpp"
        from bot.ui.lesson import curriculum_for
        query = current.casefold().strip()
        matches = [
            app_commands.Choice(name=f"{topic['title']} ({topic['id']})"[:100], value=topic["id"])
            for topic in curriculum_for(language)
            if query in topic["title"].casefold() or query in topic["id"].casefold()
        ]
        return matches[:25]

    @app_commands.command(name="student-set-java", description="Assign a student's current Java lesson without erasing progress.")
    @app_commands.describe(student="Student whose Java lesson you want to assign", lesson="Choose a Java roadmap lesson")
    @app_commands.autocomplete(lesson=_lesson_autocomplete)
    async def student_set_java(self, interaction: discord.Interaction, student: discord.Member, lesson: str):
        await self._assign_student_lesson(interaction, student, "java", lesson)

    @app_commands.command(name="student-set-cpp", description="Assign a student's current C++ lesson without erasing progress.")
    @app_commands.describe(student="Student whose C++ lesson you want to assign", lesson="Choose a C++ roadmap lesson")
    @app_commands.autocomplete(lesson=_lesson_autocomplete)
    async def student_set_cpp(self, interaction: discord.Interaction, student: discord.Member, lesson: str):
        await self._assign_student_lesson(interaction, student, "cpp", lesson)

    async def _assign_student_lesson(self, interaction: discord.Interaction, student: discord.Member, language: str, lesson_id: str):
        # Acknowledge the interaction immediately so Discord does not expire it
        # while database/progress work is running.
        await interaction.response.defer(ephemeral=True, thinking=True)

        if not self._can_assign_lesson(interaction):
            await interaction.followup.send("⛔ Only server administrators can assign lessons.", ephemeral=True)
            return
        from bot.ui.lesson import curriculum_for
        from bot.learning.progress import sync_progress
        topic = next((item for item in curriculum_for(language) if item["id"] == lesson_id), None)
        if topic is None:
            await interaction.followup.send("❌ I couldn't find that lesson. Choose one from the autocomplete list.", ephemeral=True)
            return
        await db.execute(
            "INSERT INTO users (user_id, username) VALUES (%s, %s) ON CONFLICT(user_id) DO NOTHING",
            (student.id, student.display_name),
        )
        title = f"ClassCode Assigned Lesson {language.upper()}"
        await db.execute(
            "INSERT INTO personal_notes(user_id,title,body) VALUES(%s,%s,%s)",
            (student.id, title, topic["id"]),
        )
        statuses = await sync_progress(student.id, language)
        # Earlier lessons become accessible, but none are automatically completed.
        earlier_topics = [
            item["title"] for item in curriculum_for(language)
            if item["id"] != topic["id"]
            and statuses.get(item["id"]) == "unlocked"
            and curriculum_for(language).index(item) < curriculum_for(language).index(topic)
        ]
        if statuses.get(topic["id"]) == "completed":
            message = (f"✅ Assigned **{student.display_name}** to review **{language.upper()} — {topic['title']}**. "
                       "Their completion record remains unchanged.")
        else:
            message = (f"✅ Assigned **{student.display_name}** to **{language.upper()} — {topic['title']}**.\n"
                       f"Earlier lessons are now unlocked ({len(earlier_topics)} earlier lesson(s)); they have not been marked completed.\n"
                       f"They can use `/{language}-roadmap`; `/{language}-quiz` will focus on the assigned lesson.")

        # Notify the student directly. If DMs are disabled, tell the admin so
        # they can relay the assignment manually.
        notification = (
            f"📚 **Your ClassCode learning path has been updated!**\n\n"
            f"Your current assigned lesson is **{language.upper()} — {topic['title']}**.\n"
            f"Your earlier {language.upper()} lessons are now unlocked so you can study them too. "
            "They are not automatically marked completed—you can work through them at your own pace.\n\n"
            f"**Start here:** use `/{language}-roadmap` to open the roadmap. "
            f"Use `/{language}-quiz` to practice questions for **{topic['title']}**. "
            "Passing a quiz does not automatically complete a lesson; use its Mastery Check."
        )
        try:
            await student.send(notification)
            message += "\n📩 The student was notified by DM."
        except (discord.Forbidden, discord.HTTPException):
            message += "\n⚠️ I couldn't DM the student (their DMs may be disabled). Please notify them manually."
        logger.info(
            "Administrative lesson assignment actor_id=%s target_id=%s language=%s lesson_id=%s",
            interaction.user.id, student.id, language, topic["id"],
        )
        await interaction.followup.send(message, ephemeral=True)

    @app_commands.command(name="admin-stats", description="View ClassCode learning statistics for this server.")
    @app_commands.checks.has_permissions(manage_guild=True)
    async def admin_stats(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True, thinking=True)
        member_ids = [m.id for m in interaction.guild.members if not m.bot]
        if member_ids:
            marks = ",".join("%s" for _ in member_ids)
            users = await db.fetchone(f"SELECT COUNT(*) AS count FROM users WHERE user_id IN ({marks})", tuple(member_ids))
            completed = await db.fetchone(f"SELECT COUNT(*) AS count FROM user_progress WHERE user_id IN ({marks}) AND status = 'completed'", tuple(member_ids))
            challenges = await db.fetchone(f"SELECT COUNT(*) AS count FROM daily_submissions WHERE user_id IN ({marks}) AND status = 'passed'", tuple(member_ids))
            projects = await db.fetchone(f"SELECT COUNT(*) AS count FROM project_progress WHERE user_id IN ({marks}) AND status = 'completed'", tuple(member_ids))
        else:
            users = completed = challenges = projects = {"count": 0}
        student_count = sum(1 for m in interaction.guild.members if any(r.name == 'Student' for r in m.roles))
        embed = UIEmbeds.standard("\U0001f4ca CLASSCODE ADMIN STATS", f"**Tracked learners:** {users['count']}\n**Completed lessons:** {completed['count']}\n**Passed challenges:** {challenges['count']}\n**Completed projects:** {projects['count']}\n**Students role:** {student_count}")
        await interaction.followup.send(embed=embed, ephemeral=True)


async def setup(bot):
    await bot.add_cog(AdminCog(bot))
