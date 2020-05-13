import re
import random
import praw
import discord
from discord.ext import commands

# reddit api info
reddit = praw.Reddit(client_id="REDDIT APP CLIENT ID",
                     client_secret="REDDIT APP CLIENT SECRET",
                     user_agent="REDDIT USER AGENT")

# confirm reddit
print(reddit.read_only)

# prefix is .
client = commands.Bot(command_prefix = '.')

# message for when bot is ready
@client.event
async def on_ready():
    print("Redcord is ready!")

# replace command with what you want to type with your prefix to trigger sending the image.
@client.event
async def on_message(message):
    if message.content.startswith('.red'):
        channel = message.channel
        message = message.content
        print(message)
        post = reddit.subreddit(message.replace(".red ", "")).random().url
        print(post)
        await channel.send(reddit.subreddit(message.replace(".red ", "")).random().url)

# enter your discord bot token here
client.run('DISCORD BOT TOKEN')

