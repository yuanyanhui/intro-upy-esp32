"""
This code runs on PC.
Send message to ESP32 socket server
Receive confirmation from ESP32
"""

import socket

HOST = "192.168.1.2"  # server's hostname or IP address
PORT = 2000           # port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    msg = input("Please enter your message (q to quit): ")
    if msg == "q":
        s.close()
        break
    elif msg == '':
        print("Invalid message!")
    else:
        s.sendall(msg.encode('utf-8'))
        data = s.recv(1024)
        print(f"{data.decode('utf-8')}")
