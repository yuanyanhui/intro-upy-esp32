"""
Save this file as main.py to ESP32
Wifi connection is done in boot.py.
https://randomnerdtutorials.com/esp32-esp8266-micropython-web-server/
"""

from machine import Pin
from led_web_page import web_page

# LED on NODEMCU-32S
led = Pin(2, Pin.OUT)
led.value(0)
led_state = "OFF"
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5) # max connections

while True:
  # stops at “conn, addr = s.accept()” waiting for request
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  led_on = request.find('/led_on')
  led_off = request.find('/led_off')
  if 'GET /led_on' in request:
    print('LED ON')
    led.value(1)
    led_state = "ON"
  elif 'GET /led_off' in request:
    print('LED OFF')
    led.value(0)
    led_state = "OFF"
  response = web_page(led_state)
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()
