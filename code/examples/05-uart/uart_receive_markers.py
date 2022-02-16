"""
This code runs on ESP32.
UART receiving bytes guarded by markers: b'<bytes>'
"""

import time, machine, struct

uart1 = machine.UART(1, baudrate=115200, tx=33, rx=32)

while True:
    if uart1.any():
        raw_bytes = uart1.read()  # '<ff>'
        # float = 4 bytes, char = 1 byte
        # two floats + two chars = 10 bytes
        # '<'==60, '>'==62 in ASCII
        if len(raw_bytes) == 10 and raw_bytes[0] == 60 \
                                and raw_bytes[-1] == 62:  
            float_1, float_2 = struct.unpack('ff', raw_bytes[1:-1])
            print(float_1, float_2)
