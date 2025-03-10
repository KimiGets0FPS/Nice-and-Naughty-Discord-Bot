from discord.ext import commands

import json, os

class Ranking(commands.Cog, name="Listing"):
    def __init__(self, bot):
        self.bot = bot
        try:
            rankings = json.load(open(f"{os.getcwd()}\\cogs\\rankings.json", "r"))
        except FileNotFoundError:
            ...

        exceptions = open(f"{os.getcwd()}\\cogs\\exceptions.txt", "r").readlines()
        for i in range(len(exceptions)):
            exceptions[i] = exceptions[i].strip()

    @commands.hybrid_command(name="testrank", description="This is a testing command")
    async def testrank(self, ctx):
        await ctx.send("Ranking is currently working.")

    @commands.hybrid_command(name="setpoints", description="Sets the amount of points for a user")
    async def setpoints(self, ctx):
        ...

    @commands.hybrid_command(name="getpoints", description="Gets the amount of points for a user")
    async def getpoints(self, ctx, username):
        ...

    @commands.hybrid_command(name="addpoints", description="Add points for a good boy")
    async def addpoints(self, ctx, username):
        ...

    @commands.hybrid_command(name="removepoints", description="Add points for a good boy")
    async def removepoints(self, ctx, username):
        ...

    @commands.hybrid_command(name="listpoints", description="List the amount of points for all users")
    async def listpoints(self, ctx):
        ...

    @commands.hybrid_command(name="addexception", description="Excludes a user from the list")
    async def addexception(self, ctx, username):
        ...

def update_rankings():
    ...


async def setup(bot):
    await bot.add_cog(Ranking(bot))
