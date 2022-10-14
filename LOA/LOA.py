from redbot.core import commands
from discord.ext.commands import cooldown, BucketType

import discord

class LOA(commands.Cog):
    """LOAPing cog for Duck Central"""

    def __init__(self, bot):
        self.bot = bot
       
   @bot.command()
   @commands.has_role("Staff")
   async def loa(invoke_without_command=True) {
    """LOA form"""
    embed = discord.Embed(title="Leave of Absence Request", description="The LOA cog has been replaced with a form for easier tracking.", color=0xFF5733)
        embed.add_field(name="To request a leave, please fill out the form below.", value="https://google.com")
        await ctx.send(embed=embed)
   }
