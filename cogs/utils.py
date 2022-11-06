import discord
from .config import image_types


def embed(title, description, color=discord.Color.blue()) -> object:
    """returns a discord embed object."""
    return discord.Embed(title=title,
                         description=description,
                         colour=color)


async def image_validation(ctx) -> bool:
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
