from redbot.core import commands

import discord

class LOA(commands.Cog):
    """LOA cog for Duck Central"""

    def __init__(self, bot):
        self.bot = bot
       
    @commands.group(invoke_without_command=True)
    @commands.has_role("Staff")
    async def loa(self, ctx):
        """LOA form"""
        embed = discord.Embed(title="Leave of Absence Request", description="The LOA cog has been replaced with a form for easier tracking.", color=0xFF0000, url="https://forms.gle/yynHeRZVYqaohGj77")
        embed.add_field(name="To request a leave, please click the title", value="Make sure to fill out the required information in the form in order to request a leave.")
        await ctx.send(embed=embed)