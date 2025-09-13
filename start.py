import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from keep_alive import keep_alive

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

class TechnoBot(commands.Bot):
    async def setup_hook(self):
        for extension in ['commands']:
            await self.load_extension(f"cogs.{extension}")

intents = discord.Intents.all()
bot = TechnoBot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Connected as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} command(s) synced")
    except Exception as e:
        print(e)

keep_alive()
bot.run(token)