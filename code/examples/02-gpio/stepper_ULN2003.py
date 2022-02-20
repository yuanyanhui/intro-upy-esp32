"""
Drive stepper motor 28BYJ-48 using ULN2003
"""

from machine import Pin
from time import sleep_ms

# define pins for ULN2003
IN1 = Pin(16, Pin.OUT)
IN2 = Pin(17, Pin.OUT)
IN3 = Pin(5,  Pin.OUT)
IN4 = Pin(18, Pin.OUT)

# half-step mode
# clockwise step sequence
seq_cw = [[1, 0, 0, 0],
          [1, 1, 0, 0],
          [0, 1, 0, 0],
          [0, 1, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 1],
          [0, 0, 0, 1],
          [1, 0, 0, 1]]

# counterclockwise step sequence
seq_ccw = seq_cw[::-1]

delay = 1  # ms, delay between steps

# one clockwise revolution (4096 steps)
for i in range(4096):
    step = i % 8
    IN1.value(seq_cw[step][0])
    IN2.value(seq_cw[step][1])
    IN3.value(seq_cw[step][2])
    IN4.value(seq_cw[step][3])
    sleep_ms(1)
    
# one counterclockwise revolution (4096 steps)
for i in range(4096):
    step = i % 8
    IN1.value(seq_ccw[step][0])
    IN2.value(seq_ccw[step][1])
    IN3.value(seq_ccw[step][2])
    IN4.value(seq_ccw[step][3])
    sleep_ms(1)
