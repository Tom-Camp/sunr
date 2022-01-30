# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test for NeoPixels on Raspberry Pi
import time

import board
import neopixel

sky_blue = (170, 219, 254)
delay = 2
brighness = 0.1

pixels = neopixel.NeoPixel(
    board.D18,
    32,
    brightness=0.1,
    auto_write=False,
    pixel_order=neopixel.RGB
)

up = [
    [11, 20],
    [12, 19],
    [2, 5, 26, 29],
    [3, 4, 10, 13, 18, 21, 27, 28],
    [1, 6, 9, 14, 17, 22, 25, 30],
    [0, 7, 8, 15, 16, 23, 24, 31],
]

def sunrise():
    """
    Start the sun to risin'
    """
    for l in up:
        for r in l:
            pixels[r] = sky_blue
        pixels.show()
        time.sleep(delay)


def stop():
    pixels.fill((0, 0, 0))
    pixels.show()

try:
    sunrise()
except KeyboardInterrupt:
    stop()

stop()
