
import random
import neopixel
from board import *

def random_pixel():
    color =  random.randint(0,10), random.randint(0,10), random.randint(0,10)
    return color
    

pixels = neopixel.NeoPixel(D18, 30*20, auto_write=True)
for i in range(len(pixels)):
    pixels[i] = random_pixel()


