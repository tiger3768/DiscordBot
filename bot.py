from discord.ext import commands
import asyncio
import discord
import os

from dotenv import load_dotenv
load_dotenv('dt.env')
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix = ".", intents = intents)
cogs = ["events.on_message"]

@bot.event
async def on_ready():
	print("The bot is ready!")
	for cog in cogs:
		try:
			bot.load_extension(cog)
			print(f"{cog} was loaded.")
		except Exception as e:
			print(e)
prefix="$"
@bot.event
async def on_message(message):
    if message.content==prefix+"snipe":
        await snipe(message)
    if message.content==f"<@!{bot.user.id}> Hi":
        await message.delete()
        await message.channel.send("Hello"+f"<@{message.author.id}>")
        
snipe_message_content = None
snipe_message_author = None
snipe_message_id = None

@bot.event
async def on_message_delete(message):

    global snipe_message_content
    global snipe_message_author
    global snipe_message_id

    snipe_message_content = message.content
    snipe_message_author = message.author.display_name
    snipe_message_id = message.id
    await asyncio.sleep(60)

    if message.id == snipe_message_id:
        snipe_message_author = None
        snipe_message_content = None
        snipe_message_id = None

@bot.command()
async def snipe(message):
    if snipe_message_content==None:
        await message.channel.send("Theres nothing to snipe.")
    else:
        embed = discord.Embed(description=f"{snipe_message_content}")
        embed.set_footer(text=f"Asked by {message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
        embed.set_author(name=snipe_message_author)
        await message.channel.send(embed=embed)
        return

bot.run(DISCORD_TOKEN)
