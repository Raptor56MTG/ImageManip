import discord
from discord.ext import commands
from .imagemanip import twist, blend
from .utils import embed, image_validation


class BotCommands(commands.Cog):

    """This class holds all the commands related to the scryfallAPI."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["T", "t", "Twist", "twist"])
    async def twistImage(self, ctx, buffer=None):
        """This takes in any image and outputs a twisted
        version of that image."""
        valid = await image_validation(ctx)
        if valid:
            if buffer is None:
                twist()
                await ctx.send(file=discord.File("final.png"))
            elif buffer.isnumeric():
                twist(int(buffer))
                await ctx.send(file=discord.File("final.png"))
            else:
                await ctx.send(embed=embed("Error", "Need an integer buffer value."))

    @commands.command(aliases=["B", "b", "Blend", "blend"])
    async def blendImage(self, ctx, buffer=None):
        """This takes in any image and outputs 180 degree blend."""
        valid = await image_validation(ctx)
        if valid:
            blend()
            await ctx.send(file=discord.File("final.png"))


async def setup(bot):
    await bot.add_cog(BotCommands(bot))
