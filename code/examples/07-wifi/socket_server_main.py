"""
This code runs on ESP32.
Receive message from PC socket client
Send confirmation to PC
"""

try:
  import usocket as socket
except:
  import socket
  
import network, esp, gc

gc.collect()
esp.osdebug(None)

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
s.bind(('', 2000))
s.listen(5)

while True:
    conn, addr = s.accept()  # waiting for connection
    print('Got a connection from %s' % str(addr))
    while True:
        msg = conn.recv(1024)   # bytes
        if msg == b'':
            print("Client disconnected...")
            conn.close()
            break
        else:
            print(f"Message = {msg.decode('utf-8')}")
            msg += b' received by ESP32!'
            conn.sendall(msg)
