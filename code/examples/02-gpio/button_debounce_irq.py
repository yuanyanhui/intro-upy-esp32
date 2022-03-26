"""
Button Debouncing - interrupt
Button state change triggers timer.
After timer elapse, read button state.
"""

from machine import Pin, Timer


# timer elapse callback
def toggle_led(timer):
    if button.value() == 0:
        led.value(not led.value())
    # stop timer
    timer.deinit()
    # enable interrupt
    button.irq(handler=debounce,trigger=Pin.IRQ_FALLING)

# pin interrupt callback
def debounce(pin):
    # disable interrupt
    button.irq(handler=None)
    # start timer
    timer.init(mode=Timer.ONE_SHOT, period=DEBOUNCE_TIME, callback=toggle_led)


button = Pin(33, Pin.IN, Pin.PULL_UP)
led = Pin(2, Pin.OUT)
timer = Timer(0)

DEBOUNCE_TIME = 50  # ms
button.irq(handler=debounce,trigger=Pin.IRQ_FALLING)

while True:
    pass
