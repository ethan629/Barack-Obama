import discord
from discord.ext.commands import Bot
from discord.ext import commands
import os
import json
import requests
import random
from uptime import online

bot = commands.Bot(command_prefix="b!", description="I hate Joe Biden")
client = discord.Client()

@client.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you"))
    print("Logged in as {0.user}".format(client))

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    data = json.loads(response.text)
    quote = f"{data[0]['q']} -{data[0]['a']}"
    return quote

#commands
@client.event
async def on_message(message):
    msg = message.content
    msg = msg.lower()

    if message.author == client.user:
        return
    #hi
    if msg.startswith("b!hello"):
        userid = message.author.id
        mention = f"<@{userid}>"
        await message.channel.send(f"Hey {mention}!")

    #bye
    if msg.startswith("b!bye"):
        userid = message.author.id
        mention = f"<@{userid}>"
        await message.channel.send(f"Bye {mention}!")

    #quote
    if msg.startswith("b!quote"):
        await message.channel.send(get_quote())

    #shut up
    if msg.startswith("shut up") or msg.startswith("stfu"):
        userid = message.author.id
        mention = f"<@{userid}>"
        await message.channel.send(f"Shut up {mention}!")

    #i love you
    if msg.startswith("ily obama") or msg.startswith("i love you obama"):
        userid = message.author.id
        mention = f"<@{userid}>"
        await message.channel.send(f"I love you too {mention}!")




online()
secret = os.environ['token']
client.run(secret)