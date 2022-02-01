import datetime
import json
import time

import board
import neopixel

with open("configuration.json", "r") as j:
    config = json.load(j)

color = config.get("color")
delay = config.get("delay")
brighness = 0.1

pixels = neopixel.NeoPixel(
    board.D18, 32, brightness=0.1, auto_write=False, pixel_order=neopixel.RGB
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
    for row in up:
        for p in row:
            pixels[p] = color
        pixels.show()
        time.sleep(delay)


def brighten():
    for d in range(1, 8):
        br = d * 0.1
        pixels.brightness = br
        pixels.show()
        time.sleep(delay)


def stop():
    pixels.fill((0, 0, 0))
    pixels.show()


while True:
    dow = time.strftime("%U").lower()
    alarm = config.get("week").get(dow)
    now = datetime.datetime.now()
    start = now.replace(hour=alarm[0], minute=alarm[1], second=0, microsecond=0)

    if now == start:
        try:
            sunrise()
            brighten()
        except KeyboardInterrupt:
            stop()

        stop()
