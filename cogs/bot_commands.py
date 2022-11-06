import discord
from discord.ext import commands
from .twistImage import twist
from .config import image_types


class BotCommands(commands.Cog):

    """This class holds all the commands related to the scryfallAPI."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['T', 't', 'Twist', 'twist'])
    async def twistImage(self, ctx, buffer=None):
        """This takes in any image and outputs a twisted
        version of that image."""
        try:
            image_url = ctx.message.attachments[0].url
            if image_url.endswith(image_types):
                await ctx.message.attachments[0].save('image.png')
                if buffer is not None:
                    if buffer.isnumeric():
                        twist(int(buffer))
                        await ctx.send(file=discord.File('image-twist.png'))
                    else:
                        await ctx.send("need an integer buffer value.")
                else:
                    twist()
                    await ctx.send(file=discord.File('image-twist.png'))
            else:
                await ctx.send(discord.Embed(
                    title="Error",
                    description="The attachment provided was not an image.",
                    colour=discord.Color.blue()))
        except IndexError:
            await ctx.send(embed=discord.Embed(
                title="Error",
                description="No image attached.",
                colour=discord.Color.blue()))


async def setup(bot):
    await bot.add_cog(BotCommands(bot))
