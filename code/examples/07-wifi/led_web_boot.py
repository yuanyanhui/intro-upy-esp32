"""
Save this file as boot.py to ESP32

Station Mode
 - connect ESP32 and PC/Phone to same wifi
 
Access Point Mode
 - connect PC/Phone to ESP32 hot spot
"""

try:
  import usocket as socket
except:
  import socket

import network

import esp
esp.osdebug(None)

import gc
gc.collect()

# Station Mode
# station = network.WLAN(network.STA_IF)
# station.active(True)
# station.connect('your-ssid', 'your-password')
# while station.isconnected() == False:
  # pass
# print('Connection successful')
# print(station.ifconfig())

# Access Point Mode
ssid = 'ESP32-AP'
password = '123456789'
ap = network.WLAN(network.AP_IF)
ap.config(essid=ssid, password=password)
ap.config(authmode=3)
ap.active(True)
while not ap.active():
    pass
print('network config:', ap.ifconfig())
