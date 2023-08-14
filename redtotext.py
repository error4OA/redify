from PIL import Image
import argparse

parser = argparse.ArgumentParser(description='Translate red pixels to text')

parser.add_argument('-i', '--image', help='Image to use', required=True)
parser.add_argument('-st', '--save-to', help='Save to file', required=False, default="output.txt")

args = parser.parse_args()

def get_pixel_rgb(image_path):
    image = Image.open(image_path)
    width, height = image.size

    pixel_rgb_values = []

    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            pixel_rgb_values.append(pixel)

    return pixel_rgb_values

image_path = args.image
pixel_rgb_values = get_pixel_rgb(image_path)

chars = []
for pixel in pixel_rgb_values:
    red_value = pixel[0]
    chars.append(chr(red_value))

with open(args.save_to, "w") as f:
    f.write("".join(chars))
