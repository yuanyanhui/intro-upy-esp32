"""
Blink LED - time.sleep()
time.sleep() is blocking.
On-board LED is connected to GPIO2.
"""

import time
from machine import Pin

led = Pin(2, Pin.OUT)  # Pin 2 as output

while True:
  led.value(1)      # LED on
  time.sleep(0.5)   # delay for 0.5 second
  led.value(0)      # LED off
  time.sleep(0.5)   # delay for 0.5 second
  
  