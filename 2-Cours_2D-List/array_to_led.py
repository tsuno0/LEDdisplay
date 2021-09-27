import time
import neopixel
from board import *

# constant color :
G = (255, 0, 0)
R = (0, 255, 0)
B = (0, 0, 255)
N = (0, 0, 0)

# On a Raspberry pi, use this
pixel_pin = D18

# The number of NeoPixels
num_pixels = 30*20

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
ORDER = neopixel.GRB



class ArrayLED:
    def __init__(self, array):
        self.array = array
        self.pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.5, auto_write=False, pixel_order=ORDER)
        self.width = 20
        self.height = 30
        self.size = 600

    def _array_to_pixels(self):
        x = 0
        for i in range(self.width):
            if (i%2 == 0):
                for j in range(self.height):
                    self.pixels[x] = self.array[i][j]
                    x+=1
            else:
                for j in range(self.height):
                    self.pixels[x] = self.array[i][self.height-1-j]
                    x+=1

    def update(self):
        self._array_to_pixels()
        self.pixels.show()

