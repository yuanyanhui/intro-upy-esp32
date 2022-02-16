from machine import Pin, PWM
import time

IN1 = PWM(Pin(22), freq = 1000) 
IN2 = PWM(Pin(21), freq = 1000)

while True:
    # 全速正转（脉冲宽度1023）
    IN1.duty(1023)
    IN2.duty(0)
    time.sleep(2)
    # 停止
    IN1.duty(0)
    IN2.duty(0)
    time.sleep(1)
    # 半速反转（脉冲宽度512）
    IN1.duty(0)
    IN2.duty(512)
    time.sleep(2)
    # 停止
    IN1.duty(0)
    IN2.duty(0)
    time.sleep(1)
