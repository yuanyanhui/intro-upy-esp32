"""
MPU6050 code adapted from:
https://github.com/m-rtijn/mpu6050

Compelementary filter code adapted from:
https://github.com/pms67/Attitude-Estimation

The reset value is 0x00 for all registers other than the registers below.
 - PWR_MGMT_1 Register 107: 0x40.
 - WHO_AM_I Register 117: 0x68.
"""

from time import time, sleep_ms
import math
import ustruct

# Global Variables
GRAVITIY_MS2 = 9.80665

# Scale Modifiers
ACCEL_SCALE_MODIFIER_2G = 16384.0
ACCEL_SCALE_MODIFIER_4G = 8192.0
ACCEL_SCALE_MODIFIER_8G = 4096.0
ACCEL_SCALE_MODIFIER_16G = 2048.0

GYRO_SCALE_MODIFIER_250DEG = 131.0
GYRO_SCALE_MODIFIER_500DEG = 65.5
GYRO_SCALE_MODIFIER_1000DEG = 32.8
GYRO_SCALE_MODIFIER_2000DEG = 16.4

# Pre-defined ranges
ACCEL_RANGE_2G = 0x00
ACCEL_RANGE_4G = 0x08
ACCEL_RANGE_8G = 0x10
ACCEL_RANGE_16G = 0x18

GYRO_RANGE_250DEG = 0x00
GYRO_RANGE_500DEG = 0x08
GYRO_RANGE_1000DEG = 0x10
GYRO_RANGE_2000DEG = 0x18

FILTER_BW_256 = 0x00
FILTER_BW_188 = 0x01
FILTER_BW_98 = 0x02
FILTER_BW_42 = 0x03
FILTER_BW_20 = 0x04
FILTER_BW_10 = 0x05
FILTER_BW_5 = 0x06

# MPU-6050 Registers
SMPLRT_DIV = 0x19
PWR_MGMT_1 = 0x6B
PWR_MGMT_2 = 0x6C

ACCEL_XOUT0 = 0x3B
ACCEL_YOUT0 = 0x3D
ACCEL_ZOUT0 = 0x3F

TEMP_OUT0 = 0x41

GYRO_XOUT0 = 0x43
GYRO_YOUT0 = 0x45
GYRO_ZOUT0 = 0x47

ACCEL_CONFIG = 0x1C
GYRO_CONFIG = 0x1B
MPU_CONFIG = 0x1A

class MPU6050:
    def __init__(self, i2c, address=0x68):
        self.i2c = i2c
        self.address = address
        # gyro offsets
        self.bx = 0.0   
        self.by = 0.0
        self.bz = 0.0
        # for complementary filter
        self.phi_hat = 0.0  
        self.theta_hat = 0.0  
        
        # default accelerometer and gyro configuration
        self.accel_scale_modifier = ACCEL_SCALE_MODIFIER_2G
        self.gyro_scale_modifier = GYRO_SCALE_MODIFIER_250DEG
        
        # Wake up the MPU-6050 since it starts in sleep mode
        self.i2c.writeto_mem(self.address, PWR_MGMT_1, bytearray([0x00]))

    # I2C communication methods
    def read_i2c_word(self, register):
        """
        Read two bytes and return an integer
        """
        # Read the data from the registers
        # MSB (15-8) are read first followed by LSB (7-0) (see mpu6050 Register Map)
        raw_bytes = self.i2c.readfrom_mem(self.address, register, 2)
        return ustruct.unpack('>h', raw_bytes)[0]  # big endian, short
        
    def set_sample_rate(self, sample_rate):
        """
        set sample rate
        """
        # Write the new range to the SMPLRT_DIV register
        self.i2c.writeto_mem(self.address, SMPLRT_DIV, bytearray([sample_rate]))

    # MPU-6050 Methods
    def get_temp(self):
        """
        Returns the temperature in degrees Celcius.
        """
        raw_temp = self.read_i2c_word(TEMP_OUT0)

        # Get the actual temperature using the formule given in the
        # MPU-6050 Register Map and Descriptions revision 4.2, page 30
        actual_temp = (raw_temp / 340.0) + 36.53

        return actual_temp

    def set_accel_range(self, accel_range):
        """
        Set the range of the accelerometer
        """
        if accel_range == ACCEL_RANGE_2G:
            self.accel_scale_modifier = ACCEL_SCALE_MODIFIER_2G
        elif accel_range == ACCEL_RANGE_4G:
            self.accel_scale_modifier = ACCEL_SCALE_MODIFIER_4G
        elif accel_range == ACCEL_RANGE_8G:
            self.accel_scale_modifier = ACCEL_SCALE_MODIFIER_8G
        elif accel_range == ACCEL_RANGE_16G:
            self.accel_scale_modifier = ACCEL_SCALE_MODIFIER_16G
        else:
            print(
                "Unkown range - accel_scale_modifier set to self.ACCEL_SCALE_MODIFIER_2G")
            self.accel_scale_modifier = ACCEL_SCALE_MODIFIER_2G

        # Write the new range to the ACCEL_CONFIG register
        self.i2c.writeto_mem(self.address, ACCEL_CONFIG, bytearray([accel_range]))

    def get_accel(self, g = True):
        """
        Gets and returns the X, Y and Z values from the accelerometer.
        If g is True, it will return the data in g
        If g is False, it will return the data in m/s^2
        Returns a dictionary with the measurement results.
        """
        x = self.read_i2c_word(ACCEL_XOUT0)
        y = self.read_i2c_word(ACCEL_YOUT0)
        z = self.read_i2c_word(ACCEL_ZOUT0)

        x = x / self.accel_scale_modifier
        y = y / self.accel_scale_modifier
        z = z / self.accel_scale_modifier

        if g is True:
            return x, y, z    # unit: g
        elif g is False:
            x = x * GRAVITIY_MS2
            y = y * GRAVITIY_MS2
            z = z * GRAVITIY_MS2
            return x, y, z
            
    # deg
    def get_accel_angles(self):
        ax, ay, az = self.get_accel()
        # roll - axis x (deg)
        phi = math.atan2(ay, math.sqrt(ax ** 2.0 + az ** 2.0))* 180.0 / math.pi
        # pitch - axis y (deg)
        theta = math.atan2(-ax, math.sqrt(ay ** 2.0 + az ** 2.0)) * 180.0 / math.pi

        return phi, theta

    def set_gyro_range(self, gyro_range):
        """
        Sets the range of the gyroscope to range.
        gyro_range -- the range to set the gyroscope to. Using a pre-defined
        range is advised.
        """
        if gyro_range == GYRO_RANGE_250DEG:
            self.gyro_scale_modifier = GYRO_SCALE_MODIFIER_250DEG
        elif gyro_range == GYRO_RANGE_500DEG:
            self.gyro_scale_modifier = GYRO_SCALE_MODIFIER_500DEG
        elif gyro_range == GYRO_RANGE_1000DEG:
            self.gyro_scale_modifier = GYRO_SCALE_MODIFIER_1000DEG
        elif gyro_range == GYRO_RANGE_2000DEG:
            self.gyro_scale_modifier = GYRO_SCALE_MODIFIER_2000DEG
        else:
            print("Unkown range - gyro_scale_modifier set to self.GYRO_SCALE_MODIFIER_250DEG")
            self.gyro_scale_modifier = GYRO_SCALE_MODIFIER_250DEG
        
        # First change it to 0x00 to make sure we write the correct value later
        self.i2c.writeto_mem(self.address, GYRO_CONFIG,  bytearray([0x00]))

        # Write the new range to the ACCEL_CONFIG register
        self.i2c.writeto_mem(self.address, GYRO_CONFIG,  bytearray([gyro_range]))

    def set_filter_range(self, filter_range = FILTER_BW_256):
        """Sets the low-pass bandpass filter frequency"""
        # Keep the current EXT_SYNC_SET configuration in bits 3, 4, 5 in the MPU_CONFIG register
        EXT_SYNC_SET_bytes = self.i2c.readfrom_mem(self.address, MPU_CONFIG, 1)
        EXT_SYNC_SET = int.from_bytes(EXT_SYNC_SET_bytes, 'little') & 0b00111000
        self.i2c.writeto_mem(self.address, MPU_CONFIG, bytearray([EXT_SYNC_SET | filter_range]))

    def get_gyro(self):
        """Gets and returns the X, Y and Z values from the gyroscope.
        Returns the read values in a dictionary.
        """
        x = self.read_i2c_word(GYRO_XOUT0)
        y = self.read_i2c_word(GYRO_YOUT0)
        z = self.read_i2c_word(GYRO_ZOUT0)
        
        # dps (deg/s)
        x = x / self.gyro_scale_modifier
        y = y / self.gyro_scale_modifier
        z = z / self.gyro_scale_modifier

        return x, y, z
        
    # get gyro offsets, deg/s
    def calibrate(self, N=100):
        bx = 0.0
        by = 0.0
        bz = 0.0
        print("Calibration started... Do not move sensor!")
        for i in range(N):
            gx, gy, gz = self.get_gyro()
            bx += gx
            by += gy
            bz += gz
            sleep_ms(10)
        print("Calibration done...")
        self.bx, self.by, self.bz = bx/N, by/N, bz/N 

    def get_all_data(self):
        """Reads and returns all the available data."""
        temp = self.get_temp()
        accel = self.get_accel_data()
        gyro = self.get_gyro_data()

        return accel, gyro, temp
    
    # complementary_filter
    # phi_hat, theta_hat (deg)
    def get_angle_xy(self):
        # Filter coefficient
        alpha = 0.1

        # Measured sampling time
        dt = 0.0
        start_time = time()

        dt = time() - start_time
        start_time = time()
        
        # Get estimated angles from raw accelerometer data
        phi_hat_acc, theta_hat_acc = self.get_accel_angles()
        
        # Get raw gyro data and subtract biases (deg/s)
        p, q, r = self.get_gyro()
        p -= self.bx
        q -= self.by
        r -= self.bz
        # https://github.com/pms67/Attitude-Estimation
        # Calculate Euler angle derivatives (deg/s)
        # phi_dot = p + math.sin(phi_hat * math.pi / 180.0) * math.tan(theta_hat* math.pi / 180.0) * q + math.cos(phi_hat* math.pi / 180.0) * math.tan(theta_hat* math.pi / 180.0) * r
        # theta_dot = math.cos(phi_hat* math.pi / 180.0) * q - math.sin(phi_hat* math.pi / 180.0) * r
        
        phi_dot = p
        theta_dot = q
        
        # Update complimentary filter (unit: deg)
        self.phi_hat = (1 - alpha) * (self.phi_hat + dt * phi_dot) + alpha * phi_hat_acc
        self.theta_hat = (1 - alpha) * (self.theta_hat + dt * theta_dot) + alpha * theta_hat_acc   
        
        return self.phi_hat, self.theta_hat   # roll-x axis, pitch-y axis
    

