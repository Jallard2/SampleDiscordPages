from os import environ, listdir
import asyncio
import discord
from discord.ext import commands, menus
from cogs.view import View


intents = discord.Intents.default()
intents.members = True
intents.reactions = True
intents.message_content = True
intents.messages = True

TOKEN = environ["TOKEN"]
command_prefix = "?"
client = commands.Bot(command_prefix=command_prefix, description="Neptune's Testing Bot!", intents=intents)

async def load_extensions():
    for filename in listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")
    print("All Cogs Loaded")

async def main():
    async with client:
        await load_extensions()
        discord.utils.setup_logging()
        await client.start(TOKEN, reconnect=True)

@client.event
async def on_ready():
    print('Bot is Online')
    await client.change_presence(activity=discord.Game(name='Testing'))



@client.command(hidden=True)
@commands.is_owner()
async def sync(ctx):
    print(True)
    await client.tree.sync()

asyncio.run(main())