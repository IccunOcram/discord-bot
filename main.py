import requests as rq
import time
import discord
from dotenv import load_dotenv
import os

def get_insult():
    mill = int(time.time() * 1000)
    url = f"https://evilinsult.com/generate_insult.php?type=plain&lang=en&_={mill}"
    insult = rq.get(url).text
    return insult

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = discord.Client()

@bot.event
async def on_ready():
	guild_count = 0
	for guild in bot.guilds:
		print(f"- {guild.id} (name: {guild.name})")
		guild_count = guild_count + 1
	print("SampleDiscordBot is in " + str(guild_count) + " guilds.")

@bot.event
async def on_message(message):
	if message.content == "hello":
		await message.channel.send("hey dirtbag")

@bot.event
async def on_message(message):
	if "insult" in message.content.lower():
		insult = get_insult()
		await message.channel.send(insult)

bot.run(DISCORD_TOKEN)