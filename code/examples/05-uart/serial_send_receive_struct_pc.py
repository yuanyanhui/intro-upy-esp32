"""
This code runs on PC.
Send and receive through COM port
Pack and unpack floats using struct
"""

import serial, time, random, struct   

esp32 = serial.Serial(port='COM3', baudrate=9600, timeout=.1)

# code for sender
while True:
    float_1 = random.uniform(1, 100)  # generate random float between 1 and 100
    float_2 = random.uniform(1, 100)
    packet_bytes = struct.pack('ff', float_1, float_2)  # 'ff': two floats
    esp32.write(packet_bytes)   # send 8 bytes, one float is 4 bytes
    time.sleep(0.01)

# code for receiver
# while True:
#     if esp32.in_waiting:       # Get the number of bytes in the input buffer
#         packet_bytes = esp32.read(8)   # receive 8 bytes
#         float_1, float_2 = struct.unpack('ff', packet_bytes)  # unpack into two floats
#         print(float_1, float_2)
