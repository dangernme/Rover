import smbus
import time

# Device addresses
mpu_adr = 0x68 
ak8963_adr = 0x0c

# Mpu9250 register addresses
pwr_mgmt_1 = 0x6b # To wake up the 6050 module
int_pin_cfg = 0x37 # To enable the ak8963 module

# AK8963 register addresses
hxl = 0x03 # Magnetometer x axis low byte
hyl = 0x05 # Magnetometer y axis low byte
hzl = 0x07 # Magnetometer z axis low byte
st1 = 0x02 # Magnetometer status 1
st2 = 0x09 # Magnetometer status 2
cntl1 = 0x0A # Magnetometer status 1
cntl2 = 0x0B # Magnetometer status 2

class Mpu9250:
    def __init__(self):
        # Power management registers 
        self.bus = smbus.SMBus(1) 
        
        # Enable the magnetometer module
        self.bus.write_byte_data(mpu_adr, int_pin_cfg, 0x22)
        self.bus.write_byte_data(ak8963_adr, cntl1, 0x01)

        # Now wake the 6050 up as it starts in sleep mode
        self.bus.write_byte_data(mpu_adr, pwr_mgmt_1, 0)

    def get_accel(self):
        accel_x = self._read_word_2c(mpu_adr, 0x3b)
        accel_y = self._read_word_2c(mpu_adr, 0x3d)
        accel_z = self._read_word_2c(mpu_adr, 0x3f)
        
        return(accel_x, accel_y, accel_z)
    
    def get_gyro(self):
        gyro_x = self._read_word_2c(mpu_adr, 0x43)
        gyro_y = self._read_word_2c(mpu_adr, 0x45)
        gyro_z = self._read_word_2c(mpu_adr, 0x47)
                
        return(gyro_x, gyro_y, gyro_z)
    
    def get_temp(self):
        temp = self._read_word_2c(mpu_adr, 0x41)
        
        return temp
        
    def get_mag_status(self):
        status1 = self._read_byte(ak8963_adr, st1)
        status2 = self._read_byte(ak8963_adr, st2)
        
        return status1, status2
            
    def get_mag(self):
        self.bus.write_byte_data(ak8963_adr, cntl1, 0x01)
        while True:
            status = self._read_byte(ak8963_adr, st1)
            if (status & 0x01) == 0x01:
                mag_x = self._read_word_2c(ak8963_adr, hxl)
                mag_y = self._read_word_2c(ak8963_adr, hyl)
                mag_z = self._read_word_2c(ak8963_adr, hzl)
                break;
        
        return mag_x, mag_y, mag_z

                
    
    def _read_byte(self, dev_adr, reg_adr):
        byte = self.bus.read_byte_data(dev_adr, reg_adr)
        
        return byte
    
    def _read_word(self, dev_adr, reg_adr):
        high = self.bus.read_byte_data(dev_adr, reg_adr)
        low = self.bus.read_byte_data(dev_adr, reg_adr+1)
        val = (high << 8) + low
        return val

    def _read_word_2c(self, dev_adr, reg_adr):
        val = self._read_word(dev_adr, reg_adr)
        if (val >= 0x8000):
            return -((65535 - val) + 1)
        else:
            return val






        

    







	



