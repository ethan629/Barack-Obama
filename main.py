#invite link:
#https://discord.com/api/oauth2/authorize?client_id=870359778843586621&permissions=0&scope=bot%20applications.commands

import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from replit import db
import os
import json
import random
import requests
from googlesearch import search as gsearch
from uptime import online

def get_prefix(bot, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

intents = discord.Intents.default()  
intents.members = True  
bot = commands.Bot(command_prefix=get_prefix, description="I hate Joe Biden.", help_command=None, intents=intents)

@bot.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = "."

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)

@bot.event
async def on_guild_remove(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)

@bot.command()
async def prefix(ctx, prefix):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f".help || {len(bot.guilds)} servers"))
    print("Successfully logged in as {0.user}".format(bot))

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

def fox_pic():
    response = requests.get("https://randomfox.ca/floof/")
    data = json.loads(response.text)
    pic = data["image"]
    return pic

def get_fact():
    response = requests.get("https://useless-facts.sameerkumar.website/api")
    data = json.loads(response.text)
    fact = data["data"]
    return fact

def get_joke():
    response = requests.get("https://official-joke-api.appspot.com/jokes/random")
    data = json.loads(response.text)
    setup, punchline = data["setup"], data["punchline"]
    return [setup, punchline]

def locate_iss():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = json.loads(response.text)
    longitude = data["iss_position"]["longitude"]
    latitude = data["iss_position"]["latitude"]
    location = f"{longitude}, {latitude}"
    return location

def people_in_space():
    response = requests.get("http://api.open-notify.org/astros.json")
    data = json.loads(response.text)
    info = []
    for i in range(len(data["people"])):
        person = data["people"][i]["name"]
        info.append(person)
    return info

def get_meme():
    response = requests.get("https://meme-api.herokuapp.com/gimme")
    data = json.loads(response.text)
    meme = data["url"]
    title = data["title"]
    link = data["postLink"]
    info = [title, link, meme]
    return info

def google_search(query):
    results = []
    for result in gsearch(query):
        if len(results) < 5:
            results.append(result)
        else:
            break
    return results

@bot.command(aliases=["hi"])
async def hello(ctx):
    await ctx.send("Hey!")

@bot.command()
async def bye(ctx):
    await ctx.send("Bye!")

@bot.command(aliases=["say"])
async def repeat(ctx, *, args):
    await ctx.send(args)

@bot.command()
async def quote(ctx):
    embed = discord.Embed(title="💬 Your quote:", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description=get_quote(), color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def coinflip(ctx):
    results = ["Heads", "Tails"]
    choice = random.choice(results)

    embed = discord.Embed(title="Your coinflip result:", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description=choice, color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def number(ctx, end):
    num = random.randint(1, int(end))

    embed = discord.Embed(title="Your number:", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description=num, color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def dog(ctx):
    embed = discord.Embed(title="🐶 Your dog picture:", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.set_image(url=dog_pic())
    await ctx.send(embed=embed)

@bot.command()
async def cat(ctx):
    embed = discord.Embed(title="🐱 Your cat picture:", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",color=discord.Color.blue())
    embed.set_image(url=cat_pic())
    await ctx.send(embed=embed)

@bot.command()
async def fox(ctx):
    embed = discord.Embed(title="🦊 Your fox picture:", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",color=discord.Color.blue())
    embed.set_image(url=fox_pic())
    await ctx.send(embed=embed)

@bot.command(alises=["fact"])
async def funfact(ctx):
    embed = discord.Embed(title="Your fun fact:", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description=get_fact(), color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def joke(ctx):
    embed = discord.Embed(title="😂 Your joke:", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    output = get_joke()
    embed.add_field(name=output[0], value=output[1])
    await ctx.send(embed=embed)

@bot.command()
async def space(ctx):
    embed = discord.Embed(title="Space facts:", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.set_image(url="https://images.theconversation.com/files/340465/original/file-20200609-176580-1qp5oqg.jpg?ixlib=rb-1.1.0&rect=0%2C350%2C4588%2C2294&q=45&auto=format&w=1356&h=668&fit=crop")
    data = people_in_space()
    data = str(data).strip("[]").replace("\'", "")
    embed.add_field(name="People in space", value=data, inline=False)
    embed.add_field(name="ISS location", value=locate_iss(), inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def meme(ctx):
    info = get_meme()
    embed = discord.Embed(title=f"{info[0]}", url=info[1], color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.set_image(url=info[2])
    await ctx.send(embed=embed)

@bot.command(alises=["google"])
async def search(ctx, *, query):
    result = google_search(query)
    embed = discord.Embed(title="Your search results:", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description=f"{result[0]}\n{result[1]}\n{result[2]}\n{result[3]}\n{result[4]}", color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

@bot.command()
async def add(ctx, num1, num2):
    num1, num2 = float(num1), float(num2)
    output = num1 + num2
    if output.is_integer():
        await ctx.send(int(output))
    else:
        await ctx.send(output)

@bot.command(aliases=["minus"])
async def subtract(ctx, num1, num2):
    num1, num2 = float(num1), float(num2)
    output = num1 - num2
    if output.is_integer():
        await ctx.send(int(output))
    else:
        await ctx.send(output)

@bot.command(aliases=["times"])
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

@bot.command(aliases=["squared"])
async def square(ctx, num):
    num = int(num)
    output = num**2
    await ctx.send(output)

@bot.command(aliases=["cubed"])
async def cube(ctx, num):
    num = int(num)
    output = num**3
    await ctx.send(output)

@bot.command(aliases=["root"])
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
    await ctx.send(num)

@bot.command(aliases=["factor"])
async def factors(ctx, num):
    num = int(num)
    factors = []
    for i in range(1, num+1):
       if num % i == 0:
           factors.append(i)
    
    factors = str(factors).strip("[]").replace("\'", ", ")
    await ctx.send(factors)

@bot.command()
async def gcf(ctx, num1, num2):
    num1, num2 = int(num1), int(num2)
    if num1 > num2:
        smaller = num1
    else:
        smaller = num2
    for i in range(1, smaller+1):
        if((num1 % i == 0) and (num2 % i == 0)):
            gcf = i

    await ctx.send(gcf)

@bot.command()
async def lcm(ctx, num1, num2):
    num1, num2 = int(num1), int(num2)
    if num1 > num2:
       greater = num1
    else:
       greater = num2
    for i in range(greater, num1*num2+1, greater):
       if i % num1 == 0 and i % num2 == 0:
           lcm = i
           break

    await ctx.send(lcm)

@bot.command()
async def primes(ctx, num1, num2):
    num1, num2 = int(num1), int(num2)
    primes = []
    for i in range(num1, num2+1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                primes.append(i)

    primes = str(primes).strip("[]").replace("\'", ", ")
    await ctx.send(primes)

@bot.command(aliases=["latency"])
async def ping(ctx):
    embed = discord.Embed(title="🏓 Pong!", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description=f"My ping is {round(bot.latency*1000)}ms", color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command(aliases=["info", "about_me"])
async def about(ctx):
    embed = discord.Embed(title="About me:", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/870359778843586621/10622885f15bfe05b026e80cbdd39b34.png?size=256")

    embed.add_field(name="Owner", value="ethAN#3163", inline=True)
    embed.add_field(name="Coding language", value="Python", inline=True)
    embed.add_field(name="Date created", value="July 26th, 2021", inline=True)
    embed.add_field(name="Lines of code", value="Over 500", inline=True)
    embed.add_field(name="Github", value="https://github.com/ethan629/obama-bot", inline=True)
    embed.add_field(name="Support server", value="https://discord.gg/duycJBmXzC", inline=True)
    await ctx.send(embed=embed)

@bot.command(aliases=["link"])
async def invite(ctx):
    embed = discord.Embed(title="Invite link", url="https://discord.com/api/oauth2/authorize?client_id=870359778843586621&permissions=0&scope=bot%20applications.commands", color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/870359778843586621/10622885f15bfe05b026e80cbdd39b34.png?size=256")
    await ctx.send(embed=embed)

@bot.command(aliases=["av"])
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
    embed.add_field(name="User ID", value=user.id, inline=True)
    roles = user.roles
    roles.reverse()
    embed.add_field(name="All roles", value=" ".join(role.mention for role in roles), inline=False)
    embed.add_field(name="Top role", value=user.top_role.mention, inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def serverinfo(ctx):
    embed = discord.Embed(title="Server info:",url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", color=discord.Color.blue())

    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.add_field(name="Guild name", value=ctx.guild.name, inline=True)
    embed.add_field(name="Created at", value=ctx.guild.created_at.strftime("%b %d, %Y"), inline=True)
    embed.add_field(name="Owner", value=ctx.guild.owner, inline=True)
    embed.add_field(name="Users", value=ctx.guild.member_count, inline=True)
    embed.add_field(name="Channels", value=len(ctx.guild.channels), inline=True)
    embed.add_field(name="Region", value=ctx.guild.region, inline=True)
    embed.add_field(name="Server ID", value=ctx.guild.id, inline=True)
    await ctx.send(embed=embed)

@bot.command()
@has_permissions(ban_members=True)
async def ban(ctx, *, user:discord.Member, reason="None"):
    await user.send(f"You have been banned in {ctx.guild.name} for {reason}.")
    await user.ban(reason=reason)

    embed = discord.Embed(title="User banned:", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description=f"{user.name} has been banned from {ctx.guild.name}.", color=discord.Color.blue())
    await ctx.send(embed=embed)

@bot.command()
@has_permissions(kick_members=True)
async def kick(ctx, *, user:discord.Member, reason="None"):
    await user.send(f"You have been kicked in {ctx.guild.name} for {reason}.")
    await user.kick(reason=reason)

    embed = discord.Embed(title="User kicked:", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description=f"{user.name} has been kicked from {ctx.guild.name}.", color=discord.Color.blue())
    await ctx.send(embed=embed)
    
@bot.command()
@has_permissions(manage_messages=True)
async def purge(ctx, limit):
    limit = int(limit)
    if limit > 100:
        await ctx.send("You can purge a maximum of 100 messages.")
    else:
        await ctx.channel.purge(limit=limit+1)

@bot.command(aliases=["delay"])
@has_permissions(manage_channels=True)
async def slowmode(ctx, amount):
    amount = int(amount)
    await ctx.channel.edit(slowmode_delay=amount)
    await ctx.send(f"Slowmode successfully set to {amount} second(s).")

@bot.command()
@has_permissions(manage_messages=True)
async def warn(ctx, user:discord.Member, reason="None"):
    await user.send(f"You have been warned in {ctx.guild.name} for {reason} by {ctx.author.name}.")

    embed = discord.Embed(title="User warned:", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description=f"{user.name} has been warned.", color=discord.Color.blue())
    await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Help page:", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.add_field(name=".help_math", value="Commands for math.", inline=True)
    embed.add_field(name=".help_fun", value="Commands for fun.", inline=True)
    embed.add_field(name=".help_utility", value="Commands for utility.", inline=True)
    embed.add_field(name=".help_moderation", value="Commands for moderation.", inline=True)

    await ctx.send(embed=embed)

@bot.command()
async def start(ctx):
    db[f"{ctx.author.id}_bank"] = 0
    db[f"{ctx.author.id}_wallet"] = 0
    await ctx.send(f"{ctx.author.display_name} is now registered for the currency system.")

@bot.command(aliases=["beg"])
async def free(ctx):
    amount = random.randint(10, 1000)
    db[f"{ctx.author.id}_wallet"] += amount
    wallet = db[f"{ctx.author.id}_wallet"]

    embed = discord.Embed(title="You begged on the street.", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description=f"You recieved {amount} coins.\nYou now have {wallet} coins.", color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command(aliases=["bal"])
async def balance(ctx):
    wallet = db[f"{ctx.author.id}_wallet"]
    bank = db[f"{ctx.author.id}_bank"]

    embed = discord.Embed(title="Your balance.", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description=f"Wallet: {wallet}\nBank: {bank}", color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command(aliases=["dep"])
async def deposit(ctx, amount):
    if amount == "all" or amount == "max":
        db[f"{ctx.author.id}_bank"] += db[f"{ctx.author.id}_wallet"]
        db[f"{ctx.author.id}_wallet"] = 0
        bank = db[f"{ctx.author.id}_bank"]
        wallet = db[f"{ctx.author.id}_wallet"]

        await ctx.send(f"You deposited all of your coins, you now have {wallet} coins in your wallet and {bank} coins in your bank.")
    else:
        if amount < wallet:
            amount = int(amount)
            db[f"{ctx.author.id}_bank"] += amount
            db[f"{ctx.author.id}_wallet"] -= amount
            bank = db[f"{ctx.author.id}_bank"]
            wallet = db[f"{ctx.author.id}_wallet"]

            await ctx.send(f"You deposited {amount} coins, you now have {wallet} coins in your wallet and {bank} coins in your bank.")
        else:
            await ctx.send("You can't deposit more than what you have!")

@bot.command(aliases=["with"])
async def withdraw(ctx, amount):
    if amount == "all" or amount == "max":
        db[f"{ctx.author.id}_wallet"] += db[f"{ctx.author.id}_bank"]
        db[f"{ctx.author.id}_bank"] = 0
        bank = db[f"{ctx.author.id}_bank"]
        wallet = db[f"{ctx.author.id}_wallet"]

        await ctx.send(f"You withdrawed all of your coins, you now have {wallet} coins in your wallet and {bank} coins in your bank.")
    else:
        if amount < bank:
            amount = int(amount)
            db[f"{ctx.author.id}_bank"] -= amount
            db[f"{ctx.author.id}_wallet"] += amount
            bank = db[f"{ctx.author.id}_bank"]
            wallet = db[f"{ctx.author.id}_wallet"]

            await ctx.send(f"You withdrawed {amount} coins, you now have {wallet} coins in your wallet and {bank} coins in your bank.")
        else:
            await ctx.send("You can't withdraw more than what you have!")

@bot.command()
async def help_math(ctx):
    embed = discord.Embed(title="Help page:", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

    embed.add_field(name=".add", value="Adds two numbers.", inline=True)
    embed.add_field(name=".subtract", value="Subtracts two numbers.", inline=True)
    embed.add_field(name=".multiply", value="Multiply two numbers.", inline=True)
    embed.add_field(name=".divide", value="Divides two numbers.", inline=True)
    embed.add_field(name=".square", value="Squares a number.", inline=True)
    embed.add_field(name=".cube", value="Cubes a number.", inline=True)
    embed.add_field(name=".squareroot", value="Outputs the square root of a number.", inline=True)
    embed.add_field(name=".factorial", value="Outputs the factorial of a number.", inline=True)
    embed.add_field(name=".gcf", value="Outputs the greatest common factor of two numbers.", inline=True)
    embed.add_field(name=".lcm", value="Outputs the least common multiple of two numbers.", inline=True)
    embed.add_field(name=".factors", value="Outputs the factors of a number.", inline=True)
    embed.add_field(name=".primes", value="Outputs the primes within the range of two number.", inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def help_fun(ctx):
    embed = discord.Embed(title="Help page:", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.add_field(name=".hello", value="Says hi to you.", inline=True)
    embed.add_field(name=".bye", value="Says bye to. you.", inline=True)
    embed.add_field(name=".quote", value="Outputs a random quote.", inline=True)
    embed.add_field(name=".funfact", value="Outputs a random fun fact.", inline=True)
    embed.add_field(name=".joke", value="Outputs a random joke.", inline=True)
    embed.add_field(name=".space", value="Outputs some current facts about space.", inline=True)
    embed.add_field(name=".meme", value="Outputs a random meme.", inline=True)
    embed.add_field(name=".dog", value="Outputs a random dog picture.", inline=True)
    embed.add_field(name=".cat", value="Outputs a random cat picture.", inline=True)
    embed.add_field(name=".fox", value="Outputs a random fox picture.", inline=True)
    embed.add_field(name=".search", value="Outputs the top five search results of your inputed query.", inline=True)
    embed.add_field(name=".coinflip", value="Outputs the result of a coinflip.", inline=True)
    embed.add_field(name=".number", value="Outputs a random number within a limit.", inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def help_utility(ctx):
    embed = discord.Embed(title="Help page:", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    
    embed.add_field(name=".ping", value="Outputs the bot's latency.", inline=True)
    embed.add_field(name=".prefix", value="Changes the bot's prefix.", inline=True)
    embed.add_field(name=".about", value="About page.", inline=True)
    embed.add_field(name=".invite", value="Outputs the invite for this bot.", inline=True)
    embed.add_field(name=".avatar", value="Outputs the avatar of an user.", inline=True)
    embed.add_field(name=".userinfo", value="Outputs the information of an user.", inline=True)
    embed.add_field(name=".serverinfo", value="Outputs the information of a server.", inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def help_moderation(ctx):
    embed = discord.Embed(title="Help page:", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.add_field(name=".ban", value="Bans a member.", inline=True)
    embed.add_field(name=".kick", value="Kicks a member.", inline=True)
    embed.add_field(name=".warn", value="Warns a member.", inline=True)
    embed.add_field(name=".purge", value="Purges the messages within a limit.", inline=True)
    embed.add_field(name=".slowmode", value="Sets the channel slowmode to an amount.", inline=True)
    await ctx.send(embed=embed)

online()
secret = os.environ["token"]
bot.run(secret)
