from redbot.core import commands
from discord.ext.commands import cooldown, BucketType
import discord

class DuckCog(commands.Cog):
    """Ducky's Funni cog thing"""

    def __init__(self, bot):
        self.bot = bot
       

    @commands.group(invoke_without_command=True)
    @commands.cooldown(1, 120, commands.BucketType.user)
    async def pinger(self, ctx):
        embed = discord.Embed(title="Ping Cog", description="Pings a role if registered within the bot.", color=0xFF5733)
        embed.add_field(name="Options Available:", value="`staff` \n *Pings the staff role*")
        await ctx.send(embed=embed)
        
    @pinger.command()
    async def staff(self, ctx):
        mentions = discord.AllowedMentions(roles=True, users=True, everyone=False)
        await ctx.send("<@&1009509393609535548>", allowed_mentions=mentions)
        
