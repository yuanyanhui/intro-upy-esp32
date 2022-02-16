"""
This code runs on PC.
Send floats through COM port
Float bytes are guarded by markers: b'<bytes>'
Pack and unpack floats using struct
"""

import serial, time, random, struct   

esp32 = serial.Serial(port='COM3', baudrate=115200, timeout=.1)

# send
while True:
    float_1 = random.uniform(1, 100)  # generate random float between 1 and 100
    float_2 = random.uniform(1, 100)
    raw_bytes = b'<' + struct.pack('ff', float_1, float_2) + b'>'
    esp32.write(raw_bytes)   # send bytes
    time.sleep(0.1)
