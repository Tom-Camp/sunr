import datetime
import json
import logging
import time

import board
import neopixel

logging.basicConfig(filename="sunr.log", filemode="w", level=logging.DEBUG)

with open("configuration.json", "r") as j:
    config = json.load(j)

color = config.get("color")
delay = config.get("delay")
brightness = 0.1

pixels = neopixel.NeoPixel(
    board.D18, 32, brightness=0.1, auto_write=False, pixel_order=neopixel.RGB
)

up = [11, 20, 12, 19, 2, 5, 26, 29, 3, 4, 10, 13, 18, 21, 27, 28,
      1, 6, 9, 14, 17, 22, 25, 30, 0, 7, 8, 15, 16, 23, 24, 31]


def sunrise():
    """
    Start the sun to risin'
    """
    pixels.brightness = brightness
    for p in up:
        pixels[p] = color
        try:
            pixels.show()
            time.sleep(delay)
        except ValueError as e:
            logging.debug(f"An error occurred during sunrise: {e}")


def brighten():
    """
    Increase brightness
    """
    for d in range(1, 8):
        br = d * 0.1

        try:
            pixels.brightness = br
            pixels.show()
            time.sleep(delay)
        except ValueError as e:
            logging.debug(f"An error occurred during brighten: {e}")


def stop():
    """
    Clear pixels
    """
    pixels.fill((0, 0, 0))
    pixels.show()


while True:
    dow = time.strftime("%A").lower()
    alarm = tuple(config.get("week").get(dow))
    now = datetime.datetime.now()

    if now.hour == alarm[0] and now.minute == alarm[1] and now.second == 0:
        try:
            sunrise()
            brighten()
            time.sleep(delay * 10)
        except KeyboardInterrupt:
            stop()

        stop()
