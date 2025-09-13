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

    @app_commands.command(name="confirm_player", description="Permet de donner la listes des infos a un joueur.")
    async def verify_mc_player(self, interaction: discord.Interaction, pseudo: str):
        embed = discord.Embed(
            title="Le TechnoSMP :",
            description=f"> → IP: `outerlands.fr:30001`\n"
                        f"> → Modpack: [TechnoMastery](https://www.curseforge.com/minecraft/modpacks/techno-mastery)\n"
                        f"> → Version de modpack : *v8.5*\n"
                        f"> Rôle <1342104059234222160> donné à tout les membres\n"
                        f"> → Règlement dans <1248891010965045328>\n\n"
                        f"**Ton pseudo** :`{pseudo}`\n",
            color=discord.Color.red()
        )

        await interaction.response.send_message(embed=embed)

    # use "interaction.followup.send(TEXT)" to send "TEXT" as a followup (as only one answer allowed)
    # use "interaction.response.defer()" to tell discord the bot is thinking. Then, use a followup to answer.

async def setup(bot):
    await bot.add_cog(CommandsCog(bot))