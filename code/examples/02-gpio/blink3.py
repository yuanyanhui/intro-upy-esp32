"""
Blink LED - timer callback
On-board LED is connected to GPIO2.
"""

from machine import Pin, Timer

led = Pin(2, Pin.OUT)
my_timer = Timer(0)  # using timer 0

# define callback function
def toggle_led(t):
    led.value(not led.value()) # reverse led pin state

my_timer.init(period = 1000, callback = toggle_led)  # 1000ms

while True:
    pass    # do nothing