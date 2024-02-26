"""
Wait for change of pin state.
True change lasts for a continuous 20ms.
"""

# https://docs.micropython.org/en/latest/pyboard/tutorial/debounce.html

import machine, time

def wait_pin_change(pin):
    """
    wait for pin to change value
    returns after pin stays in changed state for a continuous 20ms
    """
    # read current pin state
    cur_value = pin.value()
    active = 0
    # infinite loop, if no pin change
    while active < 20:
        if pin.value() != cur_value:
            active += 1
        else:
            active = 0
        time.sleep_ms(1)
        
button = machine.Pin(33, machine.Pin.IN, machine.Pin.PULL_UP)
led = machine.Pin(2, machine.Pin.OUT)

while True:
    wait_pin_change(button)  # blocking
    if not button.value():
        led.value(not led.value())
        