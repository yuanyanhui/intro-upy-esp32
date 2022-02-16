"""
Servo motor
"""

import time
from machine import Pin, PWM

# 舵机控制信号线连接引脚13，PWM频率为50Hz
servo = PWM(Pin(13), freq = 50)

pulse_time_0 = 0.5       # 0度角，脉冲宽度时长为0.5ms
pulse_time_180 = 2.5     # 180度角，脉冲宽度时长为2.5ms
pwm_period = 20          # PWM周期为20ms
pwm_max_width = 1023     # PWM周期（20ms）对应的脉冲宽度数值

# 舵机角度转换为PWM脉冲宽度数值
def angle_to_pwm(x):
    # 角度x对应的脉冲宽度时长
    pulse_time = x * (pulse_time_180 - pulse_time_0) / 180 + pulse_time_0
    # 脉冲宽度时长对应的脉冲宽度数值
    pulse_width = int(pulse_time * pwm_max_width / pwm_period)
    return pulse_width

pwm0 = angle_to_pwm(0)     # 0度角脉冲宽度数值
pwm90 = angle_to_pwm(90)   # 90度角脉冲宽度数值
pwm180 = angle_to_pwm(180) # 180度角脉冲宽度数值

while True:
    # 舵机位置0度
    servo.duty(pwm0)
    time.sleep(1)
    # 舵机位置90度
    servo.duty(pwm90)
    time.sleep(1)
    # 舵机位置180度
    servo.duty(pwm180)
    time.sleep(1)
    # 舵机位置90度
    servo.duty(pwm90)
    time.sleep(1)

