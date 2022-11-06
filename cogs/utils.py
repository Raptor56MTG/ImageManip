import discord


def embed(title, description, color=discord.Color.blue()):
    """returns a discord embed object."""
    return discord.Embed(title=title,
                         description=description,
                         colour=color)
