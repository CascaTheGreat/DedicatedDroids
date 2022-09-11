import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PUL = 17
DIR = 27
ENA = 22

GPIO.setup(PUL,GPIO.OUT)
GPIO.setup(DIR,GPIO.OUT)
GPIO.setup(ENA,GPIO.OUT)
