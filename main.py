# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class CustomClient(discord.client) :
    async def on_ready(self):
        print(f'{self.user} has connected to discord!')





client = CustomClient()
commands = {

}

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'welcome to the server')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content =

    elif message.content == 'raise-exception':
        raise discord.DiscordException

@client.event


client.run(TOKEN)
