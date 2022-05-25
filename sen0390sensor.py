from machine import I2C
import time
import sys

class Sen0390sensor:
    LIGHT_SENS_ADDR=0x4a
    i2c = None
    MODE = b'79'
    CONFIG_ADDR = 0x04
    DATA_ADDR = 0x00
    
    def __init__(self, i2c):
        self.i2c = i2c
        self.initI2C

#    def __init__(self, i2c, mode):
#        self.i2c = i2c
#        self.MODE = mode
#        self.initI2C
    
    def initI2C():
        try:
            self.i2c.writeto_mem(self.LIGHT_SENS_ADDR, self.CONFIG_ADDR, self.MODE)
        except OSError:
            print("Cannot initialise sensor. Check cables!")
            sys.exit()
        time.sleep(0.5)        
    
    def isPresent(self):
        found = False
        devices = self.i2c.scan()
        if devices:
            for d in devices:
                if d == self.LIGHT_SENS_ADDR:
                    print("Sensor is here!")
                    found = True
        return found
    
    def read(self):
        value=self.i2c.readfrom_mem(self.LIGHT_SENS_ADDR, self.DATA_ADDR, 4)
        lux = value[3]
        lux = (lux<<8)|value[2]
        lux = (lux<<8)|value[1]
        lux = (lux<<8)|value[0]
        lux = lux * 1.4 / 1000
#        print("Lux: "+str(lux))
        return lux



