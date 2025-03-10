import json

from discord.ext import commands

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
        await ctx.send("Shutting down the bot.")
        await self.bot.close()

    @commands.hybrid_command(name="reload", help="Reloads a cog")
    @commands.is_owner()
    async def reload(self, ctx, cog):
        try:
            await self.bot.reload_extension(cog)
            await ctx.send(f"Reloaded '{cog}'")
        except Exception:
            await ctx.send("Cog not found.")

    @commands.hybrid_command(name="setup", help="Sets up the bot for first server's first use")
    @commands.is_owner()
    async def setup(self, ctx):
        members = {}
        for member in ctx.guild.members:
            if not member.bot:
                members[member.name] = {"gbp": 0, "exception": False}

        members = json.dumps(members, indent=4)

        rankings_file = open("rankings.json", "w")
        rankings_file.write(members)
        rankings_file.close()

        await ctx.send(f"Setup Complete.")


async def setup(bot):
    await bot.add_cog(General(bot))
