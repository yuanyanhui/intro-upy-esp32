"""
Blink LED - ticks_ms(), ticks_diff()
On-board LED is connected to GPIO2.
"""

import time
from machine import Pin

led = Pin(2, Pin.OUT)  # Pin 2 as output
led.value(1)

old_time = time.ticks_ms() # Old time (ms)

while True:
    new_time = time.ticks_ms()  # New time (ms)
    duration = time.ticks_diff(new_time, old_time)  # duration (ms)
    if (duration >= 1000):
        if (led.value() == 1):
            led.value(0)
        else:
            led.value(1)
        old_time = new_time  # update old time
  