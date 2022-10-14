from redbot.core import commands
from discord.ext.commands import cooldown, BucketType

import discord

class LOA(commands.Cog):
    """LOAPing cog for Duck Central"""

    def __init__(self, bot):
        self.bot = bot
       
   @commands.command()
   @commands.has_role("Staff")
   async def loa(invoke_without_command=True) {
    """LOA form"""
    embed = discord.Embed(title="Leave of Absence Request", description="The LOA cog has been replaced with a form for easier tracking.", color=0xFF0000)
        embed.add_field(name="To request a leave, please click here.", value="Make sure to fill out the required information in the form in order to request a leave.", url="https://google.com")
        await ctx.send(embed=embed)
   }

   bot.add_command(loa)
