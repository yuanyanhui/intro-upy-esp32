"""
Calculate tilt angles using complementary filter
"""

from machine import Pin, I2C
from mpu6050 import MPU6050
from time import sleep

i2c = I2C(0, scl = Pin(18), sda = Pin(19))

mpu = MPU6050(i2c)
mpu.calibrate()

while True:
#     temp = mpu.get_temp()
#     print(f"Temperature: {temp: 4.1f}C")
# 
    Ax, Ay, Az = mpu.get_accel()
    print(f"Ax: {Ax: 6.1f}    Ay: {Ay: 6.1f}    Az: {Az: 6.1f}")

    Gx, Gy, Gz = mpu.get_gyro()
    print(f"Gx: {Gx: 6.1f}    Gy: {Gy: 6.1f}    Gz: {Gz: 6.1f}")
    
    angle_x, angle_y = mpu.get_angle_xy()   # tilt angles, deg     
    print(f"Angle_X: {angle_x: 6.1f}    Angle_Y: {angle_y: 6.1f}")

    sleep(0.01)