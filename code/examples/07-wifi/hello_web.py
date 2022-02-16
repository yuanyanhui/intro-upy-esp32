"""
Display 'Hello World from ESP32!' on web page
"""

try:
  import usocket as socket
except:
  import socket
  
import network, esp, gc

esp.osdebug(None)   # no debug info print
gc.collect()        # garbage collector

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

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    # stops at “conn, addr = s.accept()” waiting for a request
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
    
    response = """<!DOCTYPE html>
        <html lang="en">

        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
        </head>

        <body>
            <p>Hello World from ESP32!</p>
        </body>

        </html>"""

    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()

