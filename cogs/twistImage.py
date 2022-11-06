from PIL import Image
import math


def twist(buffer=1):
    """This takes an image and rotates it back and forth
    moving inside towards the center at a pixel rate of the
    buffer value."""

    image1 = Image.open('image.png')
    width, height = image1.size
    i = buffer
    min_center_dist = min(math.ceil(height / 2), math.ceil(width / 2))
    for i in range(0, min_center_dist, buffer):
        image2 = image1.crop((i, i, width - i, height - i)).transpose(Image.ROTATE_180)
        image1.paste(image2, [i, i])
    image1.save('image-twist.png')
