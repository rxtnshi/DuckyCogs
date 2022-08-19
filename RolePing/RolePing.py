from redbot.core import commands
from discord.ext.commands import cooldown, BucketType
import discord

class RolePing(commands.Cog):
    """RolePing cog for Duck Central"""

    def __init__(self, bot):
        self.bot = bot
       

    @commands.group(invoke_without_command=True)
    async def roleping(self, ctx):
        """Pings a role defined in the bot. Cannot be set via a command."""
        embed = discord.Embed(title="RolePing", description="```Syntax: !roleping <role>``` \nPings a role if registered within the bot.", color=0xFF5733)
        embed.add_field(name="Options Available:", value="`scp` \n Pings the SCP:SL role")
        await ctx.send(embed=embed)
    
    @commands.group(invoke_without_command=True)
    @commands.has_role("Staff")
    async def resetcd(self, ctx):
        """Resets a cooldown on a roleping."""
        embed = discord.Embed(title="RolePing Management", description="```Syntax: !resetcd <role>``` \nResets the cooldown of a role if registered within the bot.", color=0xFF5733)
        embed.add_field(name="Options Available:", value="`scpsl` \n Resets the cooldown for the SCP:SL role")
        await ctx.send(embed=embed)
        
    @roleping.command()
    @cooldown(1, 18000, BucketType.guild)
    async def scp(self, ctx):
        mentions = discord.AllowedMentions(roles=True, users=True, everyone=False)
        await ctx.send("<@&556195199257411594>", allowed_mentions=mentions)
        
    
    @resetcd.command()
    @commands.has_role("Staff")
    async def scpsl(self, ctx):
        if self.bot.get_command("roleping scp").is_on_cooldown(ctx) == True:
            self.bot.get_command("roleping scp").reset_cooldown(ctx)
        await ctx.send("The RolePing for SCP:SL is now reset.")