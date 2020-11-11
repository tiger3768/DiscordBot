import discord
import os
from dotenv import load_dotenv

load_dotenv("dt.env")

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = discord.Client()

@bot.event
async def on_ready():
	guild_count = 0
	for guild in bot.guilds:
		print(f"- {guild.id} (name: {guild.name})")
		guild_count = guild_count + 1
	print("SampleDiscordBot is in " + str(guild_count) + " guilds.")
aemojis={}
@bot.event
async def on_message(message):
        if message.author==bot.user:
                return
        if message.content=="hello":
                await message.channel.send("Hey")
        if message.content=="<@!{0}> ja na lode".format(bot.user.id):
                await message.delete()
                print(message.author)
                await message.channel.send("Kuch bol rha tha kya tu <@{0}> ?".format(message.author.id))
                await message.channel.send("<:emoji_54:774352560639180820>")
        for x in bot.emojis:
                if x.animated==True:
                   aemojis[':%s:'%x.name]=('<a:%s:%s>')%(x.name,x.id)
        if message.content in aemojis.keys():
                await message.delete()
                await message.channel.send(aemojis[message.content])

                


bot.run(DISCORD_TOKEN)
