"""
DC motor control using L298N module
Three-pin mode: ENA - pwm, IN1/IN2 - digital output
"""

from machine import Pin, PWM
import time

ENA = PWM(Pin(23), freq = 1000)
IN1 = Pin(22, Pin.OUT) 
IN2 = Pin(21, Pin.OUT)

while True:
    # 全速正转（脉冲宽度1023）
    IN1.value(1)
    IN2.value(0)
    ENA.duty(1023)
    time.sleep(2)
    # 停止
    IN1.value(0)
    IN2.value(0)
    time.sleep(1)
    # 半速反转（脉冲宽度512）
    IN1.value(0)
    IN2.value(1)
    ENA.duty(512)
    time.sleep(2)
    # 停止
    IN1.value(0)
    IN2.value(0)
    time.sleep(1)
