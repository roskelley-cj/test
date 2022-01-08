import os
# This example requires the 'members' privileged intents
my_secret = os.environ['botkey']
from random import seed
from random import randint
seed(1)

import discord
from discord.ext import commands

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='/', description=description, intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(
  name="add", description="Adds two numbers seperated by a space together"
)
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command(
    name="sarcastic", description="Makes your sentence sArCaStIc"
)
async def sarcastic(ctx, *, message:str):
    sentence = ""
    for i in range(0,len(message)):
        if i % 2 == 0:
            sentence += message[i].lower()
        else:
            sentence += message[i].upper()
    await ctx.send(sentence)

@bot.command(
    name="helpme", description="If you need help with Sarcastibot"
)
async def helpme(ctx):
    message = ""

    for _ in range(2):
        x = randint(0,1)
        print(x)
    if x == 0:
        message = "No can do. Gonna cry?"
    if x == 1:
        message = "Did you try turning it off and on?"
    else:
        print(x)
    await ctx.send(message)



bot.run(my_secret)


#285615405120