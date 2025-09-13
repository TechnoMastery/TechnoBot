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

    pseudo_site = {
        "minheur2000": "Minheur"
    }

    @app_commands.command(name="pseudo_site", description="Récupérer votre pseudo sur le site.")
    async def get_site_pseudo(self, interaction: discord.Interaction):
        global pseudo_site
        if interaction.user.id in pseudo_site:
            await interaction.response.send_message(
                f"Salut {interaction.user.mention} !\n"
                f"Ton pseudo sur le site est `{pseudo_site[interaction.user.id]}` !"
            )
        else:
            await interaction.response.send_message(
                f"Salut {interaction.user.mention} !\n"
                f"Tu n'a pas de pseudo sur le site...\n"
                f"Demande à <@1095678128195653772> de t'ajouter !"
            )
    # use "interaction.followup.send(TEXT)" to send "TEXT" as a followup (as only one answer allowed)
    # use "interaction.response.defer()" to tell discord the bot is thinking. Then, use a followup to answer.

async def setup(bot):
    await bot.add_cog(CommandsCog(bot))