import re
import logging

import discord
from discord.ext import commands


TICKET_CATEGORY = "🎫 SUPPORT TICKETS"
TICKET_PANEL_CHANNEL = "tickets"
TICKET_PANEL_TITLE = "🎫 CLASSCODE SUPPORT"
logger = logging.getLogger(__name__)


def safe_ticket_name(user: discord.Member) -> str:
    base = re.sub(
        r"[^a-z0-9-]+",
        "-",
        user.name.lower(),
    ).strip("-") or "student"

    return f"ticket-{base}"[:90]


def get_ticket_owner_id(channel: discord.TextChannel) -> int | None:
    """Read the original ticket owner's ID from the channel topic."""
    topic = channel.topic or ""
    match = re.search(r"\((\d+)\)\s*$", topic)

    if match:
        return int(match.group(1))

    return None


class TicketPanelView(discord.ui.View):
    """Persistent button for the public support panel."""

    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="Create Ticket",
        style=discord.ButtonStyle.primary,
        emoji="🎫",
        custom_id="classcode_create_ticket",
    )
    async def create_ticket(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button,
    ):
        cog = interaction.client.get_cog("Tickets")

        if cog is None:
            await interaction.response.send_message(
                "❌ The ticket system is not loaded. Please tell an admin.",
                ephemeral=True,
            )
            return

        await cog.create_ticket(interaction)


class TicketControlsView(discord.ui.View):
    """Persistent controls inside private ticket channels."""

    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="Close Ticket",
        style=discord.ButtonStyle.secondary,
        emoji="🔒",
        custom_id="classcode_close_ticket",
    )
    async def close_ticket(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button,
    ):
        cog = interaction.client.get_cog("Tickets")

        if cog is None:
            await interaction.response.send_message(
                "❌ Ticket system unavailable.",
                ephemeral=True,
            )
            return

        await cog.close_ticket(interaction)

    @discord.ui.button(
        label="Delete Ticket",
        style=discord.ButtonStyle.danger,
        emoji="🗑️",
        custom_id="classcode_delete_ticket",
    )
    async def delete_ticket(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button,
    ):
        cog = interaction.client.get_cog("Tickets")

        if cog is None:
            await interaction.response.send_message(
                "❌ Ticket system unavailable.",
                ephemeral=True,
            )
            return

        await cog.delete_ticket(interaction)


class Tickets(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def cog_load(self):
        # Persistent views are registered in bot.py.
        return

    @staticmethod
    def is_admin(member: discord.Member) -> bool:
        return member.id == member.guild.owner_id or member.guild_permissions.administrator

    @staticmethod
    def is_ticket_channel(
        channel: discord.abc.GuildChannel,
    ) -> bool:
        return (
            isinstance(channel, discord.TextChannel)
            and channel.name.startswith("ticket-")
        )

    async def ensure_ticket_category(
        self,
        guild: discord.Guild,
    ) -> discord.CategoryChannel:
        """Create or repair the ticket category and existing ticket access."""

        category = discord.utils.get(
            guild.categories,
            name=TICKET_CATEGORY,
        )

        roles = {role.name: role for role in guild.roles}
        admin_role = roles.get("Admin")

        overwrites = {
            guild.default_role: discord.PermissionOverwrite(
                view_channel=False,
            ),
        }

        if guild.me:
            overwrites[guild.me] = discord.PermissionOverwrite(
                view_channel=True,
                send_messages=True,
                read_message_history=True,
                embed_links=True,
                attach_files=True,
                add_reactions=True,
                manage_messages=True,
                manage_channels=True,
            )

        if category:
            try:
                await category.edit(
                    overwrites=overwrites,
                    reason="ClassCode support ticket access sync",
                )
            except discord.Forbidden as error:
                raise RuntimeError(
                    "I cannot update the ticket category permissions. "
                    "Please give the bot Manage Channels permission."
                ) from error

        else:
            try:
                category = await guild.create_category(
                    TICKET_CATEGORY,
                    overwrites=overwrites,
                    reason="ClassCode support ticket setup",
                )
            except discord.Forbidden as error:
                raise RuntimeError(
                    "I cannot create the ticket category. "
                    "Please give the bot Manage Channels permission."
                ) from error

        # Repair existing ticket channels as well as the category.
        # Explicitly deny @everyone and restore bot access. Guild administrators
        # bypass channel overwrites; the named ClassCode Admin role does not.
        # Preserve each owner's individual permission overwrite.
        for channel in guild.text_channels:
            if not self.is_ticket_channel(channel):
                continue

            try:
                await channel.set_permissions(
                    guild.default_role,
                    overwrite=discord.PermissionOverwrite(
                        view_channel=False,
                    ),
                    reason="ClassCode ticket privacy repair",
                )

                if admin_role:
                    await channel.set_permissions(
                        admin_role,
                        overwrite=None,
                        reason="Remove non-authoritative ClassCode Admin ticket access",
                    )

                if guild.me:
                    await channel.set_permissions(
                        guild.me,
                        overwrite=overwrites[guild.me],
                        reason="ClassCode ticket bot access repair",
                    )

            except discord.Forbidden as error:
                raise RuntimeError(
                    f"I cannot repair permissions for {channel.name}. "
                    "Please check the bot's Manage Channels permission."
                ) from error

        return category

    async def find_open_ticket(
        self,
        guild: discord.Guild,
        user: discord.Member,
    ) -> discord.TextChannel | None:
        """Find an existing ticket that still allows its owner to write."""

        for channel in guild.text_channels:
            if not self.is_ticket_channel(channel):
                continue

            if get_ticket_owner_id(channel) != user.id:
                continue

            overwrite = channel.overwrites_for(user)

            if (
                overwrite.view_channel is True
                and overwrite.send_messages is not False
            ):
                return channel

        return None

    async def create_ticket(
        self,
        interaction: discord.Interaction,
    ):
        guild = interaction.guild
        user = interaction.user

        if not guild or not isinstance(user, discord.Member):
            await interaction.response.send_message(
                "❌ This can only be used inside the server.",
                ephemeral=True,
            )
            return

        if not self.is_admin(user) and not any(
            role.name == "Student" for role in user.roles
        ):
            await interaction.response.send_message(
                "🔒 Please verify first. You need the **Student** role "
                "before opening a support ticket.",
                ephemeral=True,
            )
            return

        existing = await self.find_open_ticket(guild, user)

        if existing:
            await interaction.response.send_message(
                f"🎫 You already have an open ticket: {existing.mention}",
                ephemeral=True,
            )
            return

        await interaction.response.defer(ephemeral=True)

        try:
            category = await self.ensure_ticket_category(guild)

            overwrites = {
                guild.default_role: discord.PermissionOverwrite(
                    view_channel=False,
                ),
                user: discord.PermissionOverwrite(
                    view_channel=True,
                    send_messages=True,
                    read_message_history=True,
                    attach_files=True,
                    embed_links=True,
                ),
            }

            if guild.me:
                overwrites[guild.me] = discord.PermissionOverwrite(
                    view_channel=True,
                    send_messages=True,
                    read_message_history=True,
                    embed_links=True,
                    attach_files=True,
                    add_reactions=True,
                    manage_messages=True,
                    manage_channels=True,
                )

            name = safe_ticket_name(user)

            if discord.utils.get(guild.text_channels, name=name):
                name = f"{name}-{user.id % 10000}"[:90]

            channel = await guild.create_text_channel(
                name=name,
                category=category,
                overwrites=overwrites,
                topic=(
                    f"ClassCode support ticket opened by "
                    f"{user} ({user.id})"
                ),
                reason="ClassCode support ticket created",
            )

            embed = discord.Embed(
                title="🎫 ClassCode Support Ticket",
                description=(
                    f"Welcome, {user.mention}!\n\n"
                    "Please describe your problem clearly. Include the "
                    "command you used and any error message if relevant.\n\n"
                    "⚠️ **Never share passwords, API keys, bot tokens, "
                    "or other private information.**\n\n"
                    "An admin can help you here."
                ),
                color=discord.Color.blurple(),
            )

            embed.set_footer(text="ClassCode Support")

            await channel.send(
                content=user.mention,
                embed=embed,
                view=TicketControlsView(),
            )

            await interaction.followup.send(
                f"✅ Your private ticket has been created: {channel.mention}",
                ephemeral=True,
            )

        except discord.Forbidden:
            await interaction.followup.send(
                "❌ I don't have enough permissions to create or configure "
                "the ticket. Check my **Manage Channels**, **View Channels**, "
                "and **Send Messages** permissions.",
                ephemeral=True,
            )

        except RuntimeError as error:
            await interaction.followup.send(
                f"❌ {error}",
                ephemeral=True,
            )

        except discord.HTTPException:
            await interaction.followup.send(
                "❌ Discord could not complete the ticket operation. "
                "Please try again or contact an admin.",
                ephemeral=True,
            )

    async def close_ticket(
        self,
        interaction: discord.Interaction,
    ):
        channel = interaction.channel
        guild = interaction.guild
        user = interaction.user

        if (
            not guild
            or not isinstance(channel, discord.TextChannel)
            or not self.is_ticket_channel(channel)
        ):
            await interaction.response.send_message(
                "❌ This button only works inside a ticket channel.",
                ephemeral=True,
            )
            return

        if not isinstance(user, discord.Member):
            await interaction.response.send_message(
                "❌ Unable to identify your server membership.",
                ephemeral=True,
            )
            return

        owner_id = get_ticket_owner_id(channel)

        if owner_id is None:
            await interaction.response.send_message(
                "❌ I cannot identify this ticket's owner. "
                "Please ask an admin to review the channel topic.",
                ephemeral=True,
            )
            return

        if user.id != owner_id and not self.is_admin(user):
            await interaction.response.send_message(
                "❌ Only the ticket owner or an admin can close this ticket.",
                ephemeral=True,
            )
            return

        await interaction.response.defer(ephemeral=True, thinking=True)

        owner = guild.get_member(owner_id)

        if owner is None:
            try:
                owner = await guild.fetch_member(owner_id)
            except discord.NotFound:
                await interaction.followup.send(
                    "❌ The original ticket owner is no longer in the server. "
                    "An admin can delete this ticket if it is no longer needed.",
                    ephemeral=True,
                )
                return
            except discord.HTTPException:
                await interaction.followup.send(
                    "❌ I couldn't verify the ticket owner. Please try again.",
                    ephemeral=True,
                )
                return

        owner_overwrite = channel.overwrites_for(owner)

        if (
            owner_overwrite.view_channel is not True
            or owner_overwrite.send_messages is False
        ):
            await interaction.followup.send(
                "🔒 This ticket is already closed, or the owner's access "
                "has changed. An admin can review its permissions.",
                ephemeral=True,
            )
            return

        owner_overwrite.send_messages = False

        try:
            await channel.set_permissions(
                owner,
                overwrite=owner_overwrite,
                reason=f"ClassCode ticket closed by {user}",
            )

            await channel.send(
                f"🔒 **Ticket closed** by {user.mention}. "
                "An admin can delete it when finished."
            )

            logger.info(
                "Ticket closed actor_id=%s owner_id=%s channel_id=%s",
                user.id, owner_id, channel.id,
            )

            await interaction.followup.send(
                "🔒 Ticket closed. The requester can still read the "
                "conversation, and authorized admins can manage the ticket.",
                ephemeral=True,
            )

        except discord.Forbidden:
            await interaction.followup.send(
                "❌ I cannot change this ticket's permissions. "
                "Please check the bot's channel permissions.",
                ephemeral=True,
            )

        except discord.HTTPException:
            await interaction.followup.send(
                "❌ Discord couldn't finish closing the ticket. "
                "Please try again.",
                ephemeral=True,
            )

    async def delete_ticket(
        self,
        interaction: discord.Interaction,
    ):
        channel = interaction.channel
        user = interaction.user

        if (
            not isinstance(channel, discord.TextChannel)
            or not self.is_ticket_channel(channel)
        ):
            await interaction.response.send_message(
                "❌ This button only works inside a ticket channel.",
                ephemeral=True,
            )
            return

        if (
            not isinstance(user, discord.Member)
            or not self.is_admin(user)
        ):
            await interaction.response.send_message(
                "🛡️ Only a server administrator can delete a ticket.",
                ephemeral=True,
            )
            return

        await interaction.response.send_message(
            "🗑️ Deleting this ticket...",
            ephemeral=True,
        )

        try:
            await channel.delete(
                reason=f"ClassCode ticket deleted by {user}",
            )
            logger.info(
                "Ticket deleted actor_id=%s channel_id=%s",
                user.id, channel.id,
            )
        except discord.Forbidden:
            await interaction.followup.send(
                "❌ I cannot delete this channel. Check the bot's "
                "Manage Channels permission.",
                ephemeral=True,
            )
        except discord.HTTPException:
            await interaction.followup.send(
                "❌ Discord couldn't delete the ticket. Please try again.",
                ephemeral=True,
            )

    async def post_ticket_panel(
        self,
        guild: discord.Guild,
    ) -> bool:
        """Create or refresh the public support panel in #tickets."""

        channel = discord.utils.get(
            guild.text_channels,
            name=TICKET_PANEL_CHANNEL,
        )

        if not channel:
            return False

        embed = discord.Embed(
            title=TICKET_PANEL_TITLE,
            description=(
                "Need help with ClassCode? Open a private support ticket.\n\n"
                "💻 **Technical problems**\n"
                "🔒 **Verification or permissions**\n"
                "🤖 **Broken bot features**\n"
                "❓ **Other ClassCode server questions**\n\n"
                "For normal C++ or Java programming questions, use the "
                "language help channels instead.\n\n"
                "Click the button below to create your private ticket."
            ),
            color=discord.Color.blurple(),
        )

        embed.set_footer(
            text="ClassCode Support • Never share passwords or API keys"
        )

        async for message in channel.history(limit=50):
            if (
                message.author == self.bot.user
                and message.embeds
                and message.embeds[0].title == TICKET_PANEL_TITLE
            ):
                await message.edit(
                    embed=embed,
                    view=TicketPanelView(),
                )
                return True

        await channel.send(
            embed=embed,
            view=TicketPanelView(),
        )

        return True


async def setup(bot: commands.Bot):
    await bot.add_cog(Tickets(bot))
