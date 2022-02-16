"""
Use button to toggle LED - interrupt
"""

from machine import Pin

led = Pin(2, Pin.OUT)
# Pin 23 as input, activate pull-down resistor
button = Pin(23, Pin.IN, Pin.PULL_DOWN)

# define interrupt callback function
def toggle_led(p):
    led_state = led.value()     # read led pin state
    led_state = not led_state   # reverse led pin state
    led.value(led_state)        # write led pin state

# trigger interrupt on rising edge - from 0 to 1
button.irq(handler = toggle_led, trigger = Pin.IRQ_RISING)  
    
while True:
    pass   # do nothing
    