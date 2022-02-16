"""
Simple demo to read data from MPU6050

- wake up MPU6050
- read raw bytes from register
- convert raw bytes to number
- scale number to physical unit
"""

from machine import Pin, I2C
from time import sleep
import struct

i2c = I2C(0, scl=Pin(18), sda=Pin(19))

MPU_ADDR    =  0x68      # mpu6050 i2c address
PWR_MGMT    =  0x6B      # register of power management
ACCEL_ZOUT  =  0x3F      # register of acceleration along z-axis 

i2c.writeto_mem(MPU_ADDR, PWR_MGMT, bytearray([0])) # wake up mpu6050

# Read acceleration along z-axis
while True:
    raw_bytes = i2c.readfrom_mem(MPU_ADDR, ACCEL_ZOUT, 2)   # read two raw bytes
    print(raw_bytes)
    print(len(raw_bytes))
    raw_accel_z = struct.unpack('>h', raw_bytes)[0]   # bytes to number: big endian, short
    accel_z = raw_accel_z / 16384    # number to acceleration (g)
    print("AccZ =", accel_z, 'g') 
    print("***************")
    sleep(1)