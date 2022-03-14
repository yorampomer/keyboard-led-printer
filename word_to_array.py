from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as np

def char_to_pixels(text, path='arialbd.ttf', fontsize=14):
    """
    Based on https://stackoverflow.com/a/27753869/190597 (jsheperd)
    """
    font = ImageFont.truetype(path, fontsize)
    w, h = font.getsize(text)
    h *= 2
    image = Image.new('L', (w, h), 1)
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), text, font=font)
    arr = np.asarray(image)
    arr = np.where(arr, 0, 1)
    arr = arr[(arr != 0).any(axis=1)]
    return arr

def display(arr):
    result = np.where(arr, '#', ' ')
    print('\n'.join([''.join(row) for row in result]))


def word_to_array(word: str):
    for c in word.upper():
        arr = char_to_pixels(c,path='./Cascadia.ttf',fontsize=9)
        padded = np.pad(arr, ((1,1),(0,0)),constant_values=0)
        padded = np.flip(padded, axis=0)

        for i in range(0, len(padded[0]), 2):
            padded[:, i] = np.flip(padded[:, i])
        return padded
