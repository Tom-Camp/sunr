NeoPixel FeatherWing Sunrise Alarm
==================================

A sunrise alarm clock using the the `Adafruit NeoPixel FeatherWing <https://www.adafruit.com/product/2945>`_
and a `Raspberry Pi Zero W <https://www.raspberrypi.com/products/raspberry-pi-zero-w/>`_.

`Dawn simulation <https://en.wikipedia.org/wiki/Dawn_simulation>`_

.. code-block:: text

    Dawn simulation is a technique that involves timing lights, often called wake
    up lights, sunrise alarm clock or natural light alarm clocks, in the bedroom to
    come on gradually, over a period of 30 minutes to 2 hours, before awakening to
    simulate dawn.

Setup
-----

Follow `this guide <https://learn.adafruit.com/neopixels-on-raspberry-pi>`_ from
Adafruit to install the libraries needed to use the ``board`` and ``neopixel`` libraries
on the Raspberry Pi.

Connect GPIO 18 on the Pi Zero to the data pin on the FeatherWing.

Set the times to wake in the ``configuration.json``. You can set one time for each day
of the week using 24 hour time in hour and minute pairs, for example 0630 as [6, 0].

The alarm will start by lighting 2 LEDs and after a delay lighting more until all of the
LEDs are lit. You can set the color and the delay in the configuration file.

.. code-block:: json

   {
    "week": {
         "monday": [6, 0],
         "tuesday": [6, 0],
         "wednesday": [6, 0],
         "thursday": [6, 0],
         "friday": [6, 0],
         "saturday": [6, 30],
         "sunday": [6, 30]
      },
      "color": [51, 153, 255],
      "delay": 60
   }

You can create a Systemd service so that the alarm runs on startup by creating
a service in ``/etc/systemd/service/sunr.service`` with the following information:

.. code-block:: bash

   [Unit]
   Description=Sunrise alarm clock.

   [Service]
   Type=simple
   User=root
   WorkingDirectory=/home/pi/sunr
   ExecStart=/usr/bin/python /home/pi/sunr/sunr/sunrise.py
   Restart=always

   [Install]
   WantedBy=default.target

Authors
-------

`Tom Camp <https://github.com/Tom-Camp>`_

Version
-------

- 0.1
  - Initial release


License
-------

- GNU General Public License v3.0 or later.
- SPDX-License-Identifier: ``GPL-3.0-or-later``
