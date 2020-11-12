import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv("dt.env")

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

#bot=discord.Client()
intents = discord.Intents.default()
bot=commands.Bot(command_prefix = ".",intents=intents)
cogs=["events.on_message"]
@bot.event
async def on_ready():
	print("The bot is ready!")
	for cog in cogs:
		try:
			bot.load_extension(cog)
			print(f"{cog} was loaded.")
		except Exception as e:
			print(e)
aemojis={}
@bot.event
async def on_message(message):
        if message.author==bot.user:
                return
        if message.content=="hello":
                await message.channel.send("Hey")
        if message.content=="<@!{0}> ja na lode".format(bot.user.id):
                await message.delete()
                await message.channel.send("Kuch bol rha tha kya tu <@{0}> ?".format(message.author.id))
                await message.channel.send("<:emoji_54:774352560639180820>")
           


bot.run(DISCORD_TOKEN)


