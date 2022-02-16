"""
This code runs on PC.
Send command through COM port to control LED on ESP32
Receive LED state
Note: PySerial can only write bytes.
"""

import serial, time

esp32 = serial.Serial(port='COM3', baudrate=9600, timeout=.1)

# code for sender
# while True:
#     c = input("Please Enter LED Command (0-Off, 1-On, 2-Blink): ")
#     esp32.write(c.encode('utf-8')) # bytes
#     time.sleep(0.1)
#     if esp32.in_waiting:
#         s = esp32.readline() # bytes
#         print(s.decode('utf-8'))

# code for receiver
while True:
    if esp32.in_waiting:
        c = esp32.read() # bytes
        if c == b'0':
            esp32.write(b'LED off') 
        elif c == b'1':
            esp32.write(b'LED on')
        elif c == b'2':
             esp32.write(b'LED blinking')
