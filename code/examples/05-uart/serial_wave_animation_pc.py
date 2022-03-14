"""
This code runs on PC.
Receive data through COM port
Animate data using matplotlib
"""

import serial, time, random, struct  

# Imports for plotting data on a graph
import matplotlib.pyplot as plt
import matplotlib.animation as animation 

INTERVAL_UPDATE_MS = 1

esp32_serial = serial.Serial(port='COM3', baudrate=115200, timeout=.1)

# Setup Figure for temperature plotting
fig = plt.figure()
# fig.suptitle("Data Received from ESP32", fontsize =16)
ax = fig.add_subplot(1,1,1)
# ax.set_xlim(0, 1000)
ax.set_ylim(-2, 2)
ax.set_xlabel('x', fontsize = 15)
ax.set_ylabel('y', fontsize = 15)
ax.set_title("Data Received from ESP32", fontsize =16)

x_left = 0      # initial left limit of x-axis
x_right = 2000  # initial right limit of x-axis

line1, = plt.plot([], [], color='r')
line2, = plt.plot([], [], color='g')

def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2

# Stores the x,y data for the temperature figure (1)
x1_data = []
y1_data = []
x2_data = []
y2_data = []

# The animate function is called by the animate threads to update
# the figures. It first checks to see if there is any new serial data
# to process and if there is, will then empty the serial buffer. 
# The data that is received will be parsed up to a newline character
# and unpack into two floats which are then added to the dataset.
def animate(i):
    # Process the serial stream until there are no characters waiting
    while esp32_serial.in_waiting:
        raw_bytes = esp32_serial.readline()  # read until new line '\n'
        if (len(raw_bytes) == 9): 
            # print(raw_bytes)
            y1, y2 = struct.unpack('ff', raw_bytes[0:-1])
            # print(y1, y2)
            y1_data.append(y1)
            x1_data.append(i)
            y2_data.append(y2)
            x2_data.append(i)
            
            line1.set_data(x1_data, y1_data)
            line2.set_data(x2_data, y2_data)
                      
            ax.set_xlim(max(0, i-2000), max(2000, i)) #added ax attribute here

    return (line1, line2)

# Create the animation threads that will update the plots at our specified interval. 
ani = animation.FuncAnimation(fig, animate, interval = INTERVAL_UPDATE_MS, init_func = init, blit = True)
plt.show()


