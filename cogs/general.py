from discord.ext import commands

import os, time


class General(commands.Cog, name="general"):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="test")
    async def test(self, ctx):
        await ctx.send("Bot is Currently online.")  # Testing
        return

    @commands.hybrid_command(name="shutdown", help="Shuts down the bot")
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.send("Shutting down the bot")
        await self.bot.close()

    @commands.hybrid_command(name="reload", help="Reloads a cog")
    @commands.is_owner()
    async def reload(self, ctx, cog):
        try:
            self.bot.reload_extension(cog)
            await ctx.send(f"Reloaded '{cog}'")
        except Exception:
            await ctx.send("Cog not found.")

    @commands.hybrid_command(name="members", help="Lists members in a guild")
    async def members(self, ctx):
        print(ctx.guild.members)


async def setup(bot):
    await bot.add_cog(General(bot))
