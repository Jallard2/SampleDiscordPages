from discord.ext import commands
from discord import app_commands
from discord.ext import menus
import discord



class Pages(
    commands.Cog, name="Pages", description="Pages"):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client
    
    class MyMenu(menus.Menu):
        async def send_initial_message(self, ctx: commands.Context, channel:discord.TextChannel):
            return await channel.send(f'Hello {ctx.author}')

        @menus.button('\N{THUMBS UP SIGN}')
        async def on_thumbs_up(self, payload):
            await self.message.edit(content=f'Thanks {self.ctx.author}!')

        @menus.button('\N{THUMBS DOWN SIGN}')
        async def on_thumbs_down(self, payload):
            await self.message.edit(content=f"That's not nice {self.ctx.author}...")

        @menus.button('\N{BLACK SQUARE FOR STOP}\ufe0f')
        async def on_stop(self, payload):
            self.stop()

    @commands.command()
    async def menu_example(self, ctx: commands.Context):
        m = Pages.MyMenu()
        await m.start(ctx)

async def setup(client: commands.Bot) -> None:
    await client.add_cog(Pages(client))
