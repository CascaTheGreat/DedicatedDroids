import RPi.GPIO as GPIO
import time
def setup():
    GPIO.setmode(GPIO.BOARD)

    PUL1 = 0
    DIR1 = 5
    PUL2 = 6
    DIR2 = 13
    PUL3 = 19
    DIR3 = 26
    ENA = 17 #emergency stop

    GPIO.setup(PUL1,GPIO.OUT)
    GPIO.setup(DIR1,GPIO.OUT)
    GPIO.setup(PUL2,GPIO.OUT)
    GPIO.setup(DIR2,GPIO.OUT)
    GPIO.setup(PUL3,GPIO.OUT)
    GPIO.setup(DIR3,GPIO.OUT)
    GPIO.setup(ENA,GPIO.OUT)
def move(x,y):
    pass
def look(x,y):
    pass
def stop():
    pass
def cleanup():
    GPIO.cleanup()