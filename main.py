import discord, os
from flask import Flask
from threading import Thread

# ما نحطوش التوكن هنا - ناخذوه من Render
TOKEN = os.environ.get("TOKEN")
SERVER_NAME = "TOP LIBYA"

app = Flask('')
@app.route('/')
def home(): return "TOP LIBYA Bot Online!"
def run(): app.run(host='0.0.0.0', port=8080)
Thread(target=run).start()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ {SERVER_NAME} شغال!")

@client.event
async def on_message(message):
    if message.author.bot: return
    if "تفعيل" in message.content and message.mentions:
        u = message.mentions[0]
        g = message.content.replace("تفعيل","")
        for m in message.mentions: g = g.replace(f"<@{m.id}>","").replace(f"<@!{m.id}>","")
        g = g.replace("@","").strip().split()[0] if g.strip() else "غير معروف"
        embed = discord.Embed(title=SERVER_NAME, description=f"[✓] تم ربط الحساب بنجاح\nالحساب في اللعبة : {g}\nالحساب في الديسكورد : {u.mention}", color=0x2b2d31)
        await message.channel.send(embed=embed)

client.run(TOKEN)
