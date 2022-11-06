import discord
from discord.ext import commands
from .twistImage import twist, blend
from .config import image_types
from .utils import embed


class BotCommands(commands.Cog):

    """This class holds all the commands related to the scryfallAPI."""

    def __init__(self, bot):
        self.bot = bot

    async def image_validation(self, ctx) -> bool:
        """Determines if input is valid."""
        try:
            image_url = ctx.message.attachments[0].url
            if image_url.endswith(image_types):
                await ctx.message.attachments[0].save("image.png")
                return True
            else:
                await ctx.send(embed=embed("Error", "The attachment provided was not an image."))
                return False
        except IndexError:
            await ctx.send(embed=embed("Error", "No image attached."))
            return False

    @commands.command(aliases=["T", "t", "Twist", "twist"])
    async def twistImage(self, ctx, buffer=None):
        """This takes in any image and outputs a twisted
        version of that image."""
        valid = await self.image_validation(ctx)
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
        valid = await self.image_validation(ctx)
        if valid:
            blend()
            await ctx.send(file=discord.File("final.png"))


async def setup(bot):
    await bot.add_cog(BotCommands(bot))
