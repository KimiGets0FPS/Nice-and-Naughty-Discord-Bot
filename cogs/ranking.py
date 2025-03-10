import json
import os

from discord.ext import commands


class Ranking(commands.Cog, name="Listing"):
    def __init__(self, bot):
        self.bot = bot

        self.rankings = json.load(open(f"{os.getcwd()}/rankings.json", "r"))

    @commands.hybrid_command(name="testrank", description="This is a testing command")
    async def test_rank(self, ctx):
        await ctx.send("Ranking is currently working.")

    @commands.hybrid_command(name="setpoints", description="Sets the amount of points for a user")
    @commands.has_role("*")
    async def set_points(self, ctx, username, points):
        if not check_valid_user(self.rankings, username):
            await ctx.send(f"Invalid username : {username}")
            return

        self.rankings[username]["gbp"] = int(points)
        await ctx.send(f"{points} points set for {username}")
        return

    @commands.hybrid_command(name="getpoints", description="Outputs the amount of points for a user")
    async def get_points(self, ctx, username):
        if not check_valid_user(self.rankings, username):
            ctx.send(f"Invalid username : {username}")
            return

        await ctx.send(f"{username} has {self.rankings[username].get("gbp")} points.")
        return

    @commands.hybrid_command(name="addpoints", description="Add points for a good boy")
    @commands.has_role("*")
    async def add_points(self, ctx, username, points):
        if not check_valid_user(self.rankings, username):
            ctx.send(f"Invalid username : {username}")
            return

        self.rankings[username]["gbp"] = self.rankings[username].get("gbp") + int(points)
        await ctx.send(f"{points} points added for {username}")
        return

    @commands.hybrid_command(name="removepoints", description="Add points for a good boy")
    @commands.has_role("*")
    async def remove_points(self, ctx, username, points):
        if not check_valid_user(self.rankings, username):
            ctx.send(f"Invalid username : {username}")
            return

        self.rankings[username]["gbp"] = self.rankings[username].get("gbp") - int(points)
        await ctx.send(f"{points} points removed for {username}")
        return

    @commands.hybrid_command(name="listpoints", description="List the amount of points for all users")
    async def list_points(self, ctx):
        ranked_list = {}
        for username in self.rankings:
            if not self.rankings[username].get("exception"):
                ranked_list[username] = self.rankings[username].get("gbp")
        ranked_list = dict(sorted(ranked_list.items(), key=lambda x: x[1], reverse=True))

        output = []
        for username in ranked_list:
            output.append(f"{len(output)+1}. {username}: {ranked_list[username]}")
        await ctx.send("\n".join(output))


    @commands.hybrid_command(name="addexception", description="Excludes a user from the list")
    @commands.has_role("*")
    async def add_exception(self, ctx, username):
        if not check_valid_user(self.rankings, username):
            ctx.send(f"Invalid username : {username}")
            return

        if self.rankings[username].get("exception"):
            await ctx.send(f"{username} is already excluded from being ranked")
            return

        self.rankings[username]["exception"] = True
        update_rankings(self.rankings)
        await ctx.send(f"{username} is now excluded from being ranked")
        return

    @commands.hybrid_command(name="removeexception", description="Removes a user from the list")
    @commands.has_role("*")
    async def remove_exception(self, ctx, username):
        if not check_valid_user(self.rankings, username):
            ctx.send(f"Invalid username : {username}")
            return

        if self.rankings[username].get("exception"):
            self.rankings[username]["exception"] = False
            update_rankings(self.rankings)
            await ctx.send(f"{username} is now included in being ranked")
            return

        await ctx.send(f"{username} was already excluded from being ranked")
        return


def update_rankings(rankings):
    members = json.dumps(rankings, indent=4)

    rankings_file = open("rankings.json", "w")
    rankings_file.write(members)
    rankings_file.close()

def check_valid_user(rankings, username):
    for member in rankings:
        if username == member:
            return True
    return False

async def setup(bot):
    await bot.add_cog(Ranking(bot))
