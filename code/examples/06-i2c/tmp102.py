"""
TMP102 Temperature Sensor

Temperature register is 12-bit.
Throw away D3-D0 of byte 2 and combine with byte 1.

Byte 1 of Temperature Register
D7  D6  D5 D4 D3 D2 D1 D0
T11 T10 T9 T8 T7 T6 T5 T4

Byte 2 of Temperature Register
D7 D6 D5 D4 D3 D2 D1 D0
T3 T2 T1 T0 0  0  0  0
"""

from machine import I2C, Pin
import time

i2c = I2C(0, scl=Pin(18), sda=Pin(19))

TMP102_ADDR = 0x48     # TMP102 address on the I2C bus
TEMP_REG    = 0x00     # temperature register address

while True:
    # Read two bytes from temperature register
    raw_bytes = i2c.readfrom_mem(TMP102_ADDR, TEMP_REG, 2)
    value = (raw_bytes[0] << 4) | (raw_bytes[1] >> 4)   # get 12 bits from two bytes
    if value & (1 << 11) != 0:     # bit 11 == 1, value is negative
        value = value - (1 << 12)  # two's complement
    temp_c = value * 0.0625        # temperature (C)
    print(round(temp_c , 2), "C")
    time.sleep(1)
    