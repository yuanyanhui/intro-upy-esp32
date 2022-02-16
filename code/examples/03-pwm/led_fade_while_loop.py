import time
from machine import Pin, PWM

led = PWM(Pin(2), freq=1000, duty=0)
inc = 1

while True:
  duty += inc
  led.duty(duty)
  time.sleep_ms(1)
  if duty == 1023:
    inc = -1  
  elif duty == 0:
    inc = 1


