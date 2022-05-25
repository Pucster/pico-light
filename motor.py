from machine import Pin
import utime

MOTOR_PIN_1 = Pin(0, Pin.OUT)
MOTOR_PIN_2 = Pin(1, Pin.OUT)
MOTOR_PIN_3 = Pin(2, Pin.OUT)
MOTOR_PIN_4 = Pin(3, Pin.OUT)
PINS = [MOTOR_PIN_1, MOTOR_PIN_2, MOTOR_PIN_3, MOTOR_PIN_4]

CW_SEQUENCE = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

def stopMotor():
    MOTOR_PIN_1.low()
    MOTOR_PIN_2.low()
    MOTOR_PIN_3.low()
    MOTOR_PIN_4.low()

def motorStep(clockwise):
    sequence = CW_SEQUENCE
    if not clockwise:
        sequence = CW_SEQUENCE[::-1]
    for step in sequence:
        for i in range(len(PINS)):
            PINS[i].value(step[i])
        utime.sleep(0.002)

def motorSteps(clockwise, n):
    for i in range(0,n):
        motorStep(clockwise)
    stopMotor()

