import discord
from discord.ext import commands
from discord import app_commands

class CommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # command creation
    @app_commands.command(name="helloworld", description="Dit hello world")
    async def hello_world(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hello World!")

    # use "interaction.followup.send(TEXT)" to send "TEXT" as a followup (as only one answer allowed)
    # use "interaction.response.defer()" to tell discord the bot is thinking. Then, use a followup to answer.

async def setup(bot):
    await bot.add_cog(CommandsCog(bot))