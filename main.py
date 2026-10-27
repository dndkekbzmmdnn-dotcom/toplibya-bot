import discord
from discord.ext import commands
import os
import datetime

TOKEN = os.getenv("MTU0MDg4MDE2NDQyNTE3MDk4Ng.GptaI8.agBMqzddj9_1f5blSZrRCo-RSpvqws9G_2YpkY")
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# وقت تشغيل البوت باش يحسب مدة التشغيل
start_time = datetime.datetime.now()

@bot.event
async def on_ready():
    print(f"شغال: {bot.user}")
    await bot.tree.sync()
    print("تمت مزامنة الاوامر")

def get_uptime():
    delta = datetime.datetime.now() - start_time
    days = delta.days
    hours = delta.seconds // 3600
    minutes = (delta.seconds // 60) % 60
    return f"{days} يوم، {hours} ساعة، {minutes} دقيقة"

# امر السيرفر مفتوح
@bot.tree.command(name="open", description="حالة السيرفر - مفتوح")
async def open_server(interaction: discord.Interaction):
    embed = discord.Embed(
        color=0x2b2d31,
    )
    embed.set_author(name="حالة السيرفر APP", icon_url="https://i.imgur.com/6VBx3io.png")
    
    embed.add_field(name="🔓 السيرفر مفتوح", value="\
