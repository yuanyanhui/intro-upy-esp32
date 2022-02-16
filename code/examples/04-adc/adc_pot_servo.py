"""
Control servo using potentiometer
"""

from machine import Pin, ADC, PWM

pot = ADC(Pin(32), atten = ADC.ATTN_11DB)  # 电位器 - ADC
servo = PWM(Pin(33), freq = 50)            # 舵机
    
while True:
    adc_value = pot.read()
    pulse_width_value = (125 - 25)/4095 * adc_value + 25
    servo.duty(int(pulse_width_value))
    