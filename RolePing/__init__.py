from .RolePing import RolePing


def setup(bot):
    bot.add_cog(RolePing(bot))