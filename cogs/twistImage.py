from PIL import Image
import math


def twist(buffer=1):
    """This takes an image and rotates 180 degrees
    moving inside towards the center at a pixel rate of the
    buffer value."""
    image1 = Image.open('image.png')
    width, height = image1.size
    min_center_dist = min(math.ceil(height / 2), math.ceil(width / 2))
    for i in range(0, min_center_dist, buffer):
        image2 = image1.crop((i, i, width - i, height - i)).transpose(3)
        image1.paste(image2, [i, i])
    image1.save('final.png')


def blend():
    """This takes an image and rotates 180
    degrees and blends it wth the original."""
    Image.blend(Image.open('image.png'),
                Image.open('image.png').transpose(3), 0.5).save('final.png')
