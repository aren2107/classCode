import discord
from bot.database import db
from bot.learning.cpp import CPP_CURRICULUM
from bot.learning.java import JAVA_CURRICULUM
from bot.learning.mastery import add_xp, award_badge, record_goal
from bot.ui.lesson import LessonView, lesson_embed, open_lesson, curriculum_for, sync_progress


class TopicSelectView(discord.ui.View):
    PAGE_SIZE = 20

    def __init__(self, language: str, page: int = 0):
        super().__init__(timeout=None)
        self.language = language.lower()
        self.page = max(0, page)
        self._build()

    def _build(self):
        curriculum = curriculum_for(self.language)
        total_pages = max(1, (len(curriculum) + self.PAGE_SIZE - 1) // self.PAGE_SIZE)
        self.page = min(self.page, total_pages - 1)
        start = self.page * self.PAGE_SIZE
        topics = curriculum[start:start + self.PAGE_SIZE]
        options = [
            discord.SelectOption(
                label=t["title"][:100],
                value=t["id"],
                description=("\U0001f4d6 " + t["description"][:92]).replace("\n", " ")
            ) for t in topics
        ]
        select = discord.ui.Select(
            custom_id=f"roadmap_select_{self.language}_{self.page}",
            placeholder=f"Choose a {self.language.upper()} lesson... (page {self.page + 1}/{total_pages})",
            min_values=1,
            max_values=1,
            options=options,
            row=0,
        )
        select.callback = self.select_callback
        self.add_item(select)
        if total_pages > 1:
            prev = discord.ui.Button(label="\u25c0 Previous", style=discord.ButtonStyle.secondary, custom_id=f"roadmap_prev_{self.language}_{self.page}", disabled=self.page == 0, row=1)
            nxt = discord.ui.Button(label="Next \u25b6", style=discord.ButtonStyle.secondary, custom_id=f"roadmap_next_{self.language}_{self.page}", disabled=self.page >= total_pages - 1, row=1)
            prev.callback = self.previous_page
            nxt.callback = self.next_page
            self.add_item(prev)
            self.add_item(nxt)

    async def previous_page(self, interaction: discord.Interaction):
        await interaction.response.edit_message(view=TopicSelectView(self.language, self.page - 1))

    async def next_page(self, interaction: discord.Interaction):
        await interaction.response.edit_message(view=TopicSelectView(self.language, self.page + 1))

    async def select_callback(self, interaction: discord.Interaction):
        # open_lesson acknowledges immediately before database work.
        selected_id = interaction.data["values"][0]
        await open_lesson(interaction, self.language, selected_id)
