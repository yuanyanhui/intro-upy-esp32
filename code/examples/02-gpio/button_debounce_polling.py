"""
Button Debouncing - polling
Button state is stable, if no change for a specified number of readings.
"""

from machine import Pin
import time

button = Pin(33, Pin.IN, Pin.PULL_UP)
led = Pin(2, Pin.OUT)

DEBOUNCE_TIME = 50  # ms
old_btn_state = 1
new_btn_state = 1

def debounce_button():
    button_state = button.value()
    count = 0
    # loop until button state reaches stable state
    while count < DEBOUNCE_TIME:
        # button state did not change, increment count
        if button.value() == button_state:
            count += 1
        # button state changed, reset count and button_state
        else:
            count = 0
            button_state = button.value()
        time.sleep_ms(1)
    # button state unchanged within DEBOUNCE_TIME, return as stable state
    return button_state

while True:
    new_btn_state = debounce_button()
    # detect falling edge
    if old_btn_state == 1 and new_btn_state == 0:
        led.value(not led.value())
    # update button state
    old_btn_state = new_btn_state
    