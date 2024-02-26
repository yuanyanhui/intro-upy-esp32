# This file is executed on every boot (including wake-boot from deepsleep)
import esp
esp.osdebug(None)

def do_connect(ssid, pwd):
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, pwd)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
 
# Attempt to connect to WiFi network
do_connect('your-ssid', 'your-password')

# import network
# import webrepl

# webrepl.start()

# ssid = 'ESP32-AP'
# password = '123456789'
# ap = network.WLAN(network.AP_IF)
# ap.config(essid=ssid, password=password)
# ap.config(authmode=3)
# ap.active(True)
# while not ap.active():
    # pass
# print('network config:', ap.ifconfig())
