import discord
import asyncio
from discord.ext import commands

class Eglence(commands.Cog):
    
    def init(self, client):
        
        self.client= client
        
    @commands.command()
    async def cool(self, ctx):
        await ctx.send("sunglasses")
    @commands.command()
    async def test(self, ctx, t : discord.Member):
        await ctx.send(f"{t.mention}")

def setup(client):
    client.add_cog(Eglence(client))
