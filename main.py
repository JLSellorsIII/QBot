# bot.py
import os

import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


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

@bot.command(name='roll')
async def rollEx(ctx, number_of_dice: int, trick):
    dice = [
        str(random.choice(range(1,10 + 1)))
        for _ in range(number_of_dice)
        ]
    await ctx.send(', '.join(dice))

@bot.command(name='GenerateName')
async def generateName(ctx):



bot.run(TOKEN)
