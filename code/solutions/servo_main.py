"""
Demo of servo library
 - create a servo object on Pin 13
 - sweep from left to right and right to left
"""

import time, servo

my_servo = servo.Servo(13)

while True:
    for angle in range(0, 180.1, 0.1):
        my_servo.set_angle(angle)
        time.sleep_ms(1)
	
	for angle in range(180, -0.1, -0.1):
        my_servo.set_angle(angle)
        time.sleep_ms(1)

