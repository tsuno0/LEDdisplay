import board
import neopixel


# On a Raspberry pi, use this
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 30*20

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.5, auto_write=False, pixel_order=ORDER
)