from discord.ext import commands
from discord import app_commands
import discord

class Ping(
    commands.Cog, name="Ping", description="Ping"):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client
    
    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send("Pong :table_tennis:")

async def setup(client: commands.Bot) -> None:
    await client.add_cog(Ping(client))
