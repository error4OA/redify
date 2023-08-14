from PIL import Image
import argparse

parser = argparse.ArgumentParser(description='Translate text to red pixels')

parser.add_argument('-t', '--text', help='Text to use', required=True)
parser.add_argument('-st', '--save-to', help='Save to file, must be an image', required=False, default="output.png")

args = parser.parse_args()

text = args.text

width, height = len(text), 1
background_color = (255, 255, 255, 0)
image = Image.new("RGBA", (width, height), background_color)

pixels = image.load()

for x, char in enumerate(text):
    pixels[x, 0] = (ord(char), 0, 0, 255)

image.save(args.save_to)
