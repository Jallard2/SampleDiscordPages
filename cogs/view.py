from discord.ext import commands
from discord import app_commands
from discord.ext import menus
import discord



class View(
    commands.Cog, name="View", description="View"):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    class ResponderView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)
        
        @discord.ui.button(label='\N{THUMBS UP SIGN}', style=discord.ButtonStyle.green, custom_id="Bad")
        async def countOne(self, interaction: discord.Interaction, button: discord.ui.Button):
            if button.label == "Test":
                button.label = "2"
            else:
                button.label = "Test"

            # Make sure to update the message with our updated selves
            await interaction.response.edit_message(view=self)
        
        @discord.ui.button(label='\N{THUMBS DOWN SIGN}', style=discord.ButtonStyle.red, custom_id="Good")
        async def countTwo(self, interaction: discord.Interaction, button: discord.ui.Button):
            if button.label == "Test":
                button.label = "2"
            else:
                button.label = "Test"
            await interaction.response.edit_message(view=self)

    @commands.command()
    async def counter(self, ctx: commands.Context):
        """Starts a counter for pressing."""
        await ctx.send("What's your favourite colour?", view=View.ResponderView())

async def setup(client: commands.Bot) -> None:
    await client.add_cog(View(client))