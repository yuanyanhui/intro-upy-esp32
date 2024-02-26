'''
Control switch pin using hcsr04 (auto) or browser (manual)
'''

from microdot import Microdot, Response
from microdot.template import Template
import asyncio
from machine import Pin
import time
import hcsr04


sensor = hcsr04.HCSR04(trigger_pin=19, echo_pin=18, echo_timeout_us=1000000)
switch = Pin(5, Pin.OUT)
debounce_time = 30         # ms
distance_tolerance = 10    # cm

app = Microdot()
Response.default_content_type = 'text/html'

state = 'off'
mode = 'auto'

@app.route('/', methods=['GET', 'POST'])
async def index(req):
    global state, mode

    if req.method == 'POST':
        if 'mode' in req.form:
            mode = req.form.get('mode')
        else:
            state = req.form.get('state')
            if state == 'off':
                switch.on()
            else:
                switch.off()
    
    return Template('index.html').render(mode=mode, state=state)


async def auto_light():
    global state, mode
    
    while True:
        await asyncio.sleep(1)
        if mode == 'auto':            
            count = 0
            current_value = sensor.distance_cm()

            while count < debounce_time:
                next_value = sensor.distance_cm()
                if abs(next_value - current_value) < distance_tolerance:
                    count += 1
                else:
                    count = 0
                    current_value = next_value
                await asyncio.sleep_ms(1)
                
            if current_value < 100:
                switch.off()
                state = 'on'
            else:
                switch.on()
                state = 'off'
  
    
if __name__ == '__main__':
    asyncio.create_task(auto_light())    
    app.run(port=80, debug=True)
