"""
PWM实现呼吸灯
NODEMCU-32S开发板上的LED与GPIO2相连
"""

from machine import Pin, PWM
from time import sleep_ms

led = PWM(Pin(2), freq = 1000) # PWM频率1000Hz

while True:
    for i in range(1024): # 脉冲宽度由最小值0增加到最大值1023
        led.duty(i)
        sleep_ms(1)
    for i in range(1023, -1, -1): # 脉冲宽度由最大值1023减小到最小值0
        led.duty(i)
        sleep_ms(1)   
