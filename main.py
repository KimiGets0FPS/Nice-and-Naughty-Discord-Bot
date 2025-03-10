import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv('token.env')

class Main(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='!',
            intents=discord.Intents.all(),
            help_command=commands.HelpCommand())

    async def on_ready(self):
        print(
            f"Bot Name: {os.getenv("BOT_NAME")}\nBot Token: {os.getenv("BOT_TOKEN")[0:3]}{len(os.getenv("BOT_TOKEN")[3:-1]) * "X"}\nBot is now running!")
        await self.load_cogs()

    async def load_cogs(self) -> None:
        for filename in os.listdir(f"{os.getcwd()}/cogs"):
            if filename.endswith(".py"):
                try:
                    await self.load_extension(f"cogs.{filename[:-3]}")
                    print(f"Loaded {filename[:-3]}")
                except Exception as e:
                    print(f"Failed to load {filename} with exception {e}")

    async def on_message(self, message: discord.Message) -> None:
        if message.author == self.user or message.author.bot:
            return
        await self.process_commands(message)


client = Main()
client.run(os.getenv("BOT_TOKEN"))
