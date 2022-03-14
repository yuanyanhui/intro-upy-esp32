"""
Display internal temperature and up time of ESP32 on web page
"""

try:
  import usocket as socket
except:
  import socket
  
import time, network, esp32, esp, gc
from temp_web_page import web_page

gc.collect()
esp.osdebug(None)

start_time = time.ticks_ms()

# connect to wifi (station mode)
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect("your-ssid", "your-password")
while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

# Access Point Mode
# ssid = 'ESP32-AP'
# password = '123456789'

# ap = network.WLAN(network.AP_IF)
# ap.config(essid=ssid, password=password)
# ap.config(authmode=3)
# ap.active(True)
# while not ap.active():
    # pass
# print('network config:', ap.ifconfig())

# open socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)  # max connections

while True:
    # stops at “conn, addr = s.accept()” waiting for a request
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
    temp = esp32.raw_temperature() # Fahrenheit
    temp = (temp - 32)/1.8   # Celsius
    duration = time.ticks_ms() - start_time  # ms
    duration = round(duration / 1000)   # sec
    response = web_page(temp, duration)
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
