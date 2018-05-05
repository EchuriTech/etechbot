import random
import asyncio
import aiohttp
import time
import discord
from discord import Message
from discord.ext.commands import Bot
from pyshorteners import Shortener


TOKEN = ''
client = Bot(command_prefix="!")


# Generate Command
@client.command(name='gen', pass_context=True)
async def generate(ctx):
    f = open('alts.txt', 'r')
    lines = f.readlines()
    randomAlt = random.choice(lines)
    f.close()
    print(randomAlt)
    alt = randomAlt.split(':')

    url = 'https://etechgen.000webhostapp.com/generate.php'+"?creds="+randomAlt
    print(url)
    shortener = Shortener('Adfly', uid='', key='')
    shortUrl = shortener.short(url)
    
    msg = "Hey, go generate your alt here: "+shortUrl
    await client.send_message(ctx.message.author, msg)


@client.command(name='test', pass_context=True)
async def thisTest(ctx):
    await client.say("Hi "+str(ctx.message.author.name))

# Help Command
@client.command(name='helpme', pass_context=True)
async def help(ctx):
    await client.say("This command is being worked on, please ask a moderator for help for now!")

# Clear Command
@client.command(name="clear", pass_context=True)
async def clear(ctx, number):
    if "437242123579031554" in [role.id for role in ctx.message.author.roles]:
        msgs = []
        number = int(number)
        number += 1
        async for x in client.logs_from(ctx.message.channel, limit=number):
            msgs.append(x)
        await client.delete_messages(msgs)
        number -= 1
        clearMsg = await client.say("I have deleted "+str(number)+" messages.")
        time.sleep(3)
        await client.delete_message(clearMsg)
    else:
        botMsg = await client.say("Sorry, you do not have permission to do that "+str(ctx.message.author.name))
        time.sleep(3)
        await client.delete_message(botMsg)

        
# Logging in with bot
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
