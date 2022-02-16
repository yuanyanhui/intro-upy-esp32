"""
This code runs in 1st Thonny instance.
Interpreter: Python 3 on PC

Send and receive an integer through PC COM port using PySerial
- taking input (integer) from user
- encode string into bytes
- send bytes through COM port
- receive bytes through COM port
- convert bytes to integer
"""

import serial   # PySerial module
import time

esp32 = serial.Serial(port='COM3', baudrate=9600, timeout=0.1)

while True:
    number_string = input("Enter an integer number: ")  # taking input from user
    number_bytes = number_string.encode('utf-8')  # convert string to bytes
    esp32.write(number_bytes)    # send bytes
    time.sleep(0.05)
    if esp32.in_waiting:      # incoming data available
        data_bytes = esp32.readline()   # receive bytes
        print(data_bytes)
        number = int(data_bytes)    # convert bytes to integer
        print(number)
