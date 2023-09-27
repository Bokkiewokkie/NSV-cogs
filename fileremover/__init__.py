from .webpblocker import WebpBlocker


async def setup(bot):
    await bot.add_cog(WebpBlocker(bot))