import discord
from discord.ext import commands
import os
import json
import random
import requests
from uptime import online


bot = commands.Bot(command_prefix=".", description="I hate Joe Biden")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=".commands"))
    print("Logged in as {0.user}".format(bot))

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    data = json.loads(response.text)
    quote = f"{data[0]['q']} -{data[0]['a']}"
    return quote

def dog_pic():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    data = json.loads(response.text)
    pic = data["message"]
    return pic  

def cat_pic():
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    data = json.loads(response.text)
    pic = data[0]["url"]
    return pic

@bot.command()
async def hello(ctx):
    await ctx.send("Hey!")

@bot.command()
async def bye(ctx):
    await ctx.send("Bye!")

@bot.command()
async def repeat(ctx, *, args):
    await ctx.send(args)

@bot.command()
async def quote(ctx):
    embed=discord.Embed(title="Your quote:", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description=get_quote(), color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def coinflip(ctx):
    results = ["Heads", "Tails"]
    choice = random.randint(0, 1)

    embed=discord.Embed(title="Your coinflip result:", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description=results[choice], color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def number(ctx, end):
    num = random.randint(1, int(end))

    embed=discord.Embed(title="Your number:", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description=num, color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def dog(ctx):
    embed = discord.Embed(title="Your dog picture:", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.set_image(url=dog_pic())
    await ctx.send(embed=embed)

@bot.command()
async def cat(ctx):
    embed = discord.Embed(title="Your cat picture:", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",color=discord.Color.blue())
    embed.set_image(url=cat_pic())
    await ctx.send(embed=embed)

@bot.command()
async def add(ctx, num1, num2):
    num1, num2 = float(num1), float(num2)
    output = num1 + num2
    if output.is_integer():
        await ctx.send(int(output))
    else:
        await ctx.send(output)

@bot.command()
async def subtract(ctx, num1, num2):
    num1, num2 = float(num1), float(num2)
    output = num1 - num2
    if output.is_integer():
        await ctx.send(int(output))
    else:
        await ctx.send(output)

@bot.command()
async def multiply(ctx, num1, num2):
    num1, num2 = float(num1), float(num2)
    output = num1 * num2
    if output.is_integer():
        await ctx.send(int(output))
    else:
        await ctx.send(output)

@bot.command()
async def divide(ctx, num1, num2):
    num1, num2 = float(num1), float(num2)
    output = num1 / num2
    if output.is_integer():
        await ctx.send(int(output))
    else:
        await ctx.send(output)

@bot.command()
async def square(ctx, num):
    num = int(num)
    output = num**2
    await ctx.send(output)

@bot.command()
async def cube(ctx, num):
    num = int(num)
    output = num**3
    await ctx.send(output)

@bot.command()
async def squareroot(ctx, num):
    num = int(num)
    output = num**0.5
    if output.is_integer():
        await ctx.send(int(output))
    else:
        await ctx.send(output)

@bot.command()
async def factorial(ctx, num):
    num = int(num)
    for i in range(2, num):
        num *= i
    await ctx.send(int(num))

@bot.command()
async def about(ctx):
    embed = discord.Embed(title="About me:", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

    embed.add_field(name="Owner", value="ethAN#3163", inline=True)
    embed.add_field(name="Coding language", value="Python", inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def avatar(ctx, *, user:discord.Member = None):
    embed = discord.Embed(title="Avatar:",url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", color=discord.Color.blue())
    if user == None:
        user = ctx.author
    embed.set_author(name=user.display_name, icon_url=user.avatar_url)
    embed.set_image(url=user.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def userinfo(ctx, *, user:discord.Member = None):
    embed = discord.Embed(title="User info:", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", color=discord.Color.blue())
    if user == None:
        user = ctx.author

    embed.set_author(name=user.display_name, icon_url=user.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Date created", value=user.created_at.strftime("%b %d, %Y"))
    embed.add_field(name="Date joined", value=user.joined_at.strftime("%b %d, %Y"))
    embed.add_field(name="User ID", value=user.id)
    await ctx.send(embed=embed)

@bot.command()
async def commands(ctx):
    embed = discord.Embed(title="Help page:", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

    embed.add_field(name=".add", value="Adds two numbers.", inline=True)
    embed.add_field(name=".subtract", value="Subtracts two numbers.", inline=True)
    embed.add_field(name=".multiply", value="Multiply two numbers.", inline=True)
    embed.add_field(name=".divide", value="Divides two numbers.", inline=True)
    embed.add_field(name=".square", value="Squares a number.", inline=True)
    embed.add_field(name=".cube", value="Cubes a number.", inline=True)
    embed.add_field(name=".squareroot", value="Takes the square root of a number.", inline=True)
    embed.add_field(name=".factorial", value="Takes the factorial of a number.", inline=True)
    embed.add_field(name=".hello", value="Says hi to you.", inline=True)
    embed.add_field(name=".bye", value="Says bye to. you.", inline=True)
    embed.add_field(name=".coinflip", value="Takes the result of a coinflip.", inline=True)
    embed.add_field(name=".number", value="Takes a random number within a limit.", inline=True)
    embed.add_field(name=".quote", value="Takes a random quote.", inline=True)
    embed.add_field(name=".dog", value="Takes a random dog picture.", inline=True)
    embed.add_field(name=".cat", value="Takes a random cat picture.", inline=True)
    embed.add_field(name=".about", value="About page.", inline=True)
    embed.add_field(name=".avatar", value="Takes the avatar of an user.", inline=True)
    embed.add_field(name=".userinfo", value="Takes the information of an user.", inline=True)
    await ctx.send(embed=embed)


online()
secret = os.environ['token']
bot.run(secret)