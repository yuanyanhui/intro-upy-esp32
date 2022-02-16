"""
servo library
"""

from machine import PWM, Pin

class Servo:
    def __init__(self, pin):
        self.pwm = PWM(Pin(pin), freq = 50)
        self.pulse_time_0 = 0.5       # 0度角，脉冲宽度时长为0.5ms
        self.pulse_time_180 = 2.5     # 180度角，脉冲宽度时长为2.5ms
        self.pwm_period = 20          # PWM周期为20ms
        self.pwm_max_width = 1023     # PWM周期（20ms）对应的脉冲宽度数值

    # 舵机角度转换为PWM脉冲宽度数值
    def set_angle(self, x):
        # 角度x对应的脉冲宽度时长
        pulse_time = x * (self.pulse_time_180 - self.pulse_time_0) / 180 + self.pulse_time_0
        # 脉冲宽度时长对应的脉冲宽度数值
        pulse_width = int(pulse_time * self.pwm_max_width / self.pwm_period)
        self.pwm.duty(pulse_width)
