import RPi.GPIO as GPIO
import time

#Forward movement motors
PUL1 = 0
DIR1 = 5
PUL2 = 6
DIR2 = 13
#Body turning motor
PUL3 = 19
DIR3 = 26
#Head turning motor
PUL4 = 21
DIR4 = 20
#Emergency stop
ENA = 17

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PUL1,GPIO.OUT)
    GPIO.setup(DIR1,GPIO.OUT)
    GPIO.setup(PUL2,GPIO.OUT)
    GPIO.setup(DIR2,GPIO.OUT)
    GPIO.setup(PUL3,GPIO.OUT)
    GPIO.setup(DIR3,GPIO.OUT)
    GPIO.setup(ENA,GPIO.OUT)
    GPIO.output(ENA,GPIO.HIGH)
def move(x,y):
    if -0.1 < x < 0.1 and -0.1 < y < 0.1: #set deadzone
        GPIO.output(PUL1,GPIO.LOW)
        GPIO.output(PUL2,GPIO.LOW)
        GPIO.output(PUL3,GPIO.LOW)
    elif y < -0.1: #move backwards if y is negative
        GPIO.output(DIR1,GPIO.LOW)
        GPIO.output(PUL1,GPIO.HIGH)
        GPIO.output(DIR2,GPIO.HIGH)
        GPIO.output(PUL2,GPIO.HIGH)
    elif y > 0.1: #move forwards if y is positive
        GPIO.output(DIR1,GPIO.HIGH)
        GPIO.output(PUL1,GPIO.HIGH)
        GPIO.output(DIR2,GPIO.LOW)
        GPIO.output(PUL2,GPIO.HIGH)
    if x < -0.1: #turn left if x is negative
        GPIO.output(DIR3,GPIO.LOW)
        GPIO.output(PUL3,GPIO.HIGH)
    elif x > 0.1: #turn right if x is positive
        GPIO.output(DIR3,GPIO.HIGH)
        GPIO.output(PUL3,GPIO.HIGH)
def look(x,y):
    if x < -0.1: #look left if x is negative
        GPIO.output(DIR4,GPIO.LOW)
        GPIO.output(PUL4,GPIO.HIGH)
    elif x > 0.1: #look right if x is positive
        GPIO.output(DIR4,GPIO.HIGH)
        GPIO.output(PUL4,GPIO.HIGH)
def stop():
    GPIO.output(ENA,GPIO.LOW) #disable motors
def cleanup():
    GPIO.cleanup()