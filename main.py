import discord
from discord.ext import commands
import os
import datetime

TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

start_time = datetime.datetime.now()

@bot.event
async def on_ready():
    print(f"{bot.user} جاهز")
    await bot.tree.sync()
    print("تمت المزامنة")

def get_uptime():
    delta = datetime.datetime.now() - start_time
    days = delta.days
    hours = delta.seconds // 3600
    minutes = (delta.seconds // 60) % 60
    return f"{days} يوم {hours} ساعة {minutes} دقيقة"

@bot.tree.command(name="open", description="فتح السيرفر")
async def open_server(interaction: discord.Interaction):
    embed = discord.Embed(
        color=0x2b2d31
    )
    embed.add_field(name="🔓 السيرفر مفتوح", value="السيرفر مفتوح 🟢", inline=False)
    embed.add_field(name="⏰ المدة", value=get_uptime(), inline=False)
    await interaction.response.send_message(embed=embed)

bot.run(TOKEN)
