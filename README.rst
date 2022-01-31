NeoPixel FeatherWing Sunrise Alarm
==================================

A sunrise alarm clock using the the `Adafruit NeoPixel FeatherWing <https://www.adafruit.com/product/2945>`_
and a `Raspberry Pi Zero W <https://www.raspberrypi.com/products/raspberry-pi-zero-w/>`_.

`Dawn simulation <https://en.wikipedia.org/wiki/Dawn_simulation>`_

.. code-block:: text

    Dawn simulation is a technique that involves timing lights, often called wake up lights, sunrise
    alarm clock or natural light alarm clocks, in the bedroom to come on gradually, over a period of
    30 minutes to 2 hours, before awakening to simulate dawn.

Setup
-----

Follow `this guide <https://learn.adafruit.com/neopixels-on-raspberry-pi>`_ from Adafruit to install
the libraries needed to use the ``board`` and ``neopixel`` libraries on the Raspberry Pi.

Connect GPIO 18 on the Pi Zero to the data pin on the FeatherWing.

Set the times to wake in the ``configuration.json``. You can set one time for each day of the week06
using 24 hour time, for example 0630 for 6:30am.

.. code-block:: json

   {
      "week":{
         "monday": 0600,
         "tuesday": 0650
      }
   }


Authors
-------

`Tom Camp <https://github.com/Tom-Camp>`_

Version
-------

- 0.1
  #. Initial release


License
-------

- GNU General Public License v3.0 or later.
- SPDX-License-Identifier: ``GPL-3.0-or-later``
