# bot.py
import os
import random
import discord
import csv

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='!')



@bot.event
async def on_message(message):
    if (message.author == client.user):
        return

    if (message.author.id == 456165982143119361):
        joe_responses = ["Shut up Joe", "Excellent Take Joe", "Log Off Joe"]
        await message.channel.send(f"{random.choice(joe_responses)}")  # C


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'welcome to the server')


@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message' :
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


@bot.command(name='create_puppet')
async def create_puppet(ctx, name, n):
    userID = 0
    for user in client.users:
        if (user.name == name):
            userID = user.id
    corpus = create_corpus(userID, n)
    writeCorpusToFile(corpus, name)

async def writeCorpusToFile(corpus, name):
    return



#creates an array made up of the contents of the given user's posts, up to n posts per channel, if n=0 then no limit
async def create_corpus(userID: discord.User.id, n: int):
    corpus = []
    for guild in bot.guilds:
        for channel in guild.text_channels:
            corpus.append(scrape_channel(channel))
    corpus = sum(corpus, [])
    return corpus

#collects a given user's posts from the given channel
async def scrape_channel(channel: discord.TextChannel, userID: discord.User.id, n: int):
    corpus = []
    for message in channel.history(limit=n):
        if message.author.id == userID:
            corpus.append(message.content)
    return corpus



client.run(TOKEN)
