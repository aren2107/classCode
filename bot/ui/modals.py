import discord

class CodeSubmissionModal(discord.ui.Modal, title="Code Submission"):
    code_input = discord.ui.TextInput(
        label="Paste your code below:",
        style=discord.TextStyle.paragraph,
        placeholder="// Write your C++ or Java implementation here...",
        required=True,
        max_length=2000
    )

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "\u23f3 Code received! Analysing feedback...", ephemeral=True
        )
