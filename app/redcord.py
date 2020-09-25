import sys
import re
import random
import praw
import discord
from discord.ext import commands

# reddit api info
reddit = praw.Reddit(client_id='CLIENT_ID',
                     client_secret='CLIENT_SECRET',
                     user_agent='Redcord bot for Discord')

# confirm connection to reddit
if str(reddit.read_only) == 'True':
    print('Connected to reddit!')
else:
    print('There was an issue connecting to reddit. Exiting...')
    sys.exit()


# prefix is .
client = commands.Bot(command_prefix = '.')

# message for when bot is ready
@client.event
async def on_ready():
    print('Redcord is ready!')

# replace all instances of '.red' for whatever command you want to use instead
@client.event
async def on_message(message):
    if message.content.startswith('.red'):
        channel = message.channel
        message = message.content
        print(message)
        post = reddit.subreddit(message.replace('.red ', '')).random().url
        print(post)
        await channel.send(post)

# enter your discord bot token here
client.run('BOT_TOKEN')