"""
This code runs on ESP32.
UART send and receive
Pack and unpack floats using struct
"""

import machine, time, random, struct 

uart1 = machine.UART(1, baudrate=9600, tx=33, rx=32)

# code for sender
# while True:
#     float_1 = random.uniform(1, 100)
#     float_2 = random.uniform(1, 100)
#     packet_bytes = struct.pack('ff', float_1, float_2)  # 'ff': two floats
#     uart1.write(packet_bytes)   # send 8 bytes, one float is 4 bytes
#     time.sleep_ms(500)
    
# code for receiver
while True:
    if uart1.any():
        packet_bytes = uart1.read(8)   # receive 8 bytes
        float_1, float_2 = struct.unpack('ff', packet_bytes)   # unpack into two floats
        print(float_1, float_2)
    