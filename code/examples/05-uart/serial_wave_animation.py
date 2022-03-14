"""
This code runs on ESP32.
UART send and receive
Pack and unpack floats using struct
"""

import machine, time, struct, math

uart1 = machine.UART(1, baudrate=115200, tx=33, rx=32)

while True:
    for x in range(0, 500):
        y1 = math.sin(2*math.pi*x/500)
        y2 = math.cos(2*math.pi*x/500)
        packet_bytes = struct.pack('ff', y1, y2) + b'\n'  # end packet with new line '\n'
        uart1.write(packet_bytes)     # send 9 bytes, float=4 bytes
        # print(len(packet_bytes))
        time.sleep_ms(10)
