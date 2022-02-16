"""
Infrared sensor outputs both digital and analog signals
"""

from machine import Pin, ADC
from time import sleep

# DO数字量输入, AO模拟量输入
DO = Pin(32, Pin.IN)
AO = ADC(Pin(33), atten = ADC.ATTN_11DB)  # 0.0v - 3.55v range
    
while True:
    print('DO = ', DO.value())
    print('AO = ', AO.read())
    sleep(1)
    
    
    