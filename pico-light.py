import machine
from machine import Pin
import utime
import sys
# import our libraries
import motor
from sen0390sensor import Sen0390sensor

i2c = machine.I2C(0, scl=machine.Pin(9), sda=machine.Pin(8), freq=400000)

lightSensor = Sen0390sensor(i2c)
print(lightSensor.isPresent())
motor.stopMotor()

#sys.exit()
while True:
    lux = lightSensor.read()
    print("Light intensity: %6.2f lux" % (lux))
    if lux > 200:
        print("too bright, rotate motor CW")
        motor.motorSteps(True, 10)
    elif lux < 20:
        print("too shady, rotate motor ACW")
        motor.motorSteps(False, 10)
    utime.sleep(0.2)

