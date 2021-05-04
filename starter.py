import discord
import asyncio
from discord.ext import commands
import ayarlar

client = commands.Bot(command_prefix="!")

cogs = ["cogs.eglence"]
for cog in cogs:
    try:
        client.load_extension(cog)
    except:
        print(f"{cog}: inmedi morq {str(e)}")

def owner(ctx):
    return int(ctx.author.id) in Config.OWNERIDS

@bot.command(aliases = ["retard"])
@commands.check(owner)
async def restart(ctx):
    yenile = discord.Embed(
        title = "Yenileniyor...",
        color = Config.MAINCOLOR
    )
    msg = await ctx.send(embed = yenile)
    for cog in cogs:
        bot.reload_extension("cogs." + cog)
        restarting.add_field(name = f"{cog}", value = "✅ Coglari kontrol ettim!!")
        await msg.edit(embed = yenile)
    importlib.reload(Config)
    restarting.add_field(name="Config", value="Reloaded")
    restarting.title = "Bot Yenilendi"
    await msg.delete(delay = 2)
    if ctx.guild != None:
        await ctx.message.delete(delay = 2)

client.run(TOKEN)
