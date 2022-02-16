from machine import I2C, Pin

# Create an I2C object
i2c = I2C(0, sda = Pin(19), scl = Pin(18))

address = i2c.scan()  # list

# Scan for devices
print('Address:', hex(address[0]))