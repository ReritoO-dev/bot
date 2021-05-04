import discord
import asyncio
from discord.ext import commands
from ayarlar import *

client = commands.Bot(command_prefix="!")

cogs = ["cogs.eglence"]
for cog in cogs:
    try:
        client.load_extension(cog)
    except:
        print(f"{cog}: inmedi morq {str(e)}")

client.run()
