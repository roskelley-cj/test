import os
import interactions
from keep_alive import keep_alive

botkey = os.environ['sarcbotk']
to_array = []

bot = interactions.Client(token=botkey)


@bot.command(name="get_guilds",
             description="be nice!!",
             scope=[840020523937169428])
async def get_guilds(ctx: interactions.CommandContext):
    """Counts # of guilds you're in, and creates an output.txt with list of guild names/ids at your host"""
    i = 0
    for gl in bot.guilds:
        with open('output.txt', 'a') as f:
            f.write(gl.name + ': ' + str(gl.id) + '\n')
            i += 1
    await ctx.send(f"You're in {i} servers")


@bot.command()
@interactions.option()
async def sarcastic(ctx: interactions.CommandContext, message: str):
    """i Am FunNy!!"""
    sentence = ""
    for i in range(0, len(message)):
        if i % 2 == 0:
            sentence += message[i].upper()
        else:
            sentence += message[i].lower()
    await ctx.send(f"{sentence}")


@bot.command(name="fucku",
             description="be nice!!",
             scope=[840020523937169428, 797675035208056882, 426532808790638593, 696889715294470166, 352428177374576672, 797675035208056882, 726934771967590420])
async def fucku(ctx: interactions.CommandContext):
    await ctx.send("No, fuck you!")


keep_alive()

bot.start()

