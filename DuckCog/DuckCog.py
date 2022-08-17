from redbot.core import commands
from discord.ext.commands import cooldown, BucketType
import discord

class DuckCog(commands.Cog):
    """Ducky's Funni cog thing"""

    def __init__(self, bot):
        self.bot = bot
       

    @commands.group(invoke_without_command=True)
    async def pinger(self, ctx):
        embed = discord.Embed(title="Ping Cog", description="```Syntax: [p]pinger <subcommand>``` \nPings a role if registered within the bot.", color=0xFF5733)
        embed.add_field(name="Options Available:", value="`scp` \n Pings the staff role")
        await ctx.send(embed=embed)
        
    @pinger.command()
    @cooldown(1, 3600, BucketType.user)
    async def scp(self, ctx):
        mentions = discord.AllowedMentions(roles=True, users=True, everyone=False)
        await ctx.send("<@&556195199257411594>", allowed_mentions=mentions)
        
