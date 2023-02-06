from discord.ext import commands
import discord

class Hybrid(
    commands.Cog, name="Hybrid", description="Hybrid"):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @commands.hybrid_command(name="hybrid", description="hybrid")
    async def hybrid(self, ctx: commands.Context):
        await ctx.send("Pong :table_tennis:")

async def setup(client: commands.Bot) -> None:
    await client.add_cog(Hybrid(client))
