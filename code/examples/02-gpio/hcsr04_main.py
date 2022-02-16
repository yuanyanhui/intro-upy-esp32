from hcsr04 import HCSR04
from time import sleep

sensor = HCSR04(trigger_pin = 26, echo_pin = 27)

while True:
    distance = sensor.distance_cm()
    print('Distance:', distance, 'cm')
#     print(f'Distance: {distance: .1f} cm')
    sleep(1)