"""
This code runs on ESP32.
Send command through UART to control LED on ESP32
Note：ESP32 UART can write string or bytes.
"""

import time
from machine import UART, Pin

uart1 = UART(1, baudrate=9600, tx=33, rx=32)

# # code for ESP32 receiver
# led = Pin(2, Pin.OUT)
# c = b'0'

# while True:
#     if uart1.any():
#         c = uart1.read() # bytes
#         if c == b'0':
#             led.value(0)
#             uart1.write('LED off') 
#         elif c == b'1':
#             led.value(1)
#             uart1.write('LED on')
#         elif c == b'2':
#              uart1.write('LED blinking')
#     
#     if c == b'2':
#         led.value(not led.value())    
#         time.sleep(1)   


# code for ESP32 sender
while True:
    c = input("Please Enter Option (0-Off, 1-On, 2-Blink): ")
    uart1.write(c) # c is string
    time.sleep(0.1)
    if uart1.any():
        s = uart1.readline() # s is bytes
        print(s.decode('utf-8'))  