"""
This code runs in 2nd Thonny instance.
Interpreter: MicroPython on ESP32

Receive and send an integer through UART
- receive bytes through uart
- convert bytes to integer
- computation on integer
- convert integer to string
- send string through uart
"""

from machine import UART

uart1 = UART(1, baudrate=9600, tx=33, rx=32)

while True:
    if uart1.any():    # incoming data available
        number_bytes = uart1.read() # bytes
        print(number_bytes)
        number = int(number_bytes) + 1  # convert bytes to integer and add 1
        print(number)
        number_string = str(number)  # convert integer to string
        uart1.write(number_string)   # send string      
