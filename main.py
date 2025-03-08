import discord
from discord.ext import commands

from dotenv import load_dotenv

import os

Client = discord.Client(intents=discord.Intents.all())
client = commands.Bot(intents=discord.Intents.all(), command_prefix='%')

print(discord.Intents.all())

@client.event
async def on_ready():
    print("boom")

@client.command(name='boom')
async def boom(message):
    await message.send("boom")  # Testing
    return

load_dotenv('token.env')
client.run(os.getenv("BOT_TOKEN"))
