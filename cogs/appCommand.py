from discord.ext import commands
from discord import app_commands
import discord

class App(
    commands.Cog, name="App", description="App"):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @app_commands.command(name="appne", description="App commands Without an Ephemeral Message")
    async def appne(self, interaction: discord.Interaction):
        await interaction.response.send_message("Pong :table_tennis:")

    @app_commands.command(name="app", description="App commands With an Ephemeral Message")
    async def app(self, interaction: discord.Interaction):
        await interaction.response.send_message("Pong :table_tennis:", ephemeral=True)

async def setup(client: commands.Bot) -> None:
    await client.add_cog(App(client))
