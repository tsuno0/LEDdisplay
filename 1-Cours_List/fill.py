import neopixel
from board import *

pixels = neopixel.NeoPixel(D18, 30*20, auto_write=True)
for i in range(len(pixels)):
    pixels[i] = (255, 255, 255)