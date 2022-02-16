"""
Use button to toggle LED - polling
"""

from machine import Pin

led = Pin(2, Pin.OUT)
# Pin 23 as input, activate pull-down resistor
button = Pin(23, Pin.IN, Pin.PULL_DOWN) 

led_state = 0
old_button_state = 0
new_button_state = 0
    
while True:
    new_button_state = button.value()
    # Button is pressed: old state is 0, new state is 1.
    if old_button_state == 0 and new_button_state == 1:
        led_state = led.value()     # read led pin state
        led_state = not led_state   # reverse led pin state
        led.value(led_state)        # write new led pin state
    old_button_state = new_button_state  # update button pin state
    