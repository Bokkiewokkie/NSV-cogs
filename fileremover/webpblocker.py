import discord

from redbot.core import commands
from redbot.core.bot import Red


__version__ = "0.1.3"
__author__ = "Bokkiewokkie"


class WebpBlocker(commands.Cog):

    def __init__(self, bot: Red):
        self.bot = bot

    @commands.Cog.listener()
    @commands.Cog.listener("on_message_edit")
    async def on_message(self, *args):
        message = args[-1]
        assert isinstance(message, discord.message)
        if not message.guild:
            return

        assert isinstance(message.channel, discord.TextChannel)
        if await self.bot.cog_disabled_in_guild(self, message.guild):
            return

        for embed in message.embeds:
            if embed.type == "webp":
                await message.edit(suppress=True)
                break