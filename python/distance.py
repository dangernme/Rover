import RPi.GPIO as GPIO
import time

PIN_TRIGGER_LEFT = 24
PIN_ECHO_LEFT = 22
PIN_TRIGGER_RIGHT = 23
PIN_ECHO_RIGHT = 5

class Distance:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PIN_TRIGGER_LEFT, GPIO.OUT)
        GPIO.setup(PIN_ECHO_LEFT, GPIO.IN) 
        GPIO.output(PIN_TRIGGER_LEFT, True)
        GPIO.setup(PIN_TRIGGER_RIGHT, GPIO.OUT)
        GPIO.setup(PIN_ECHO_RIGHT, GPIO.IN) 
        GPIO.output(PIN_TRIGGER_RIGHT, True)
        
    def get_distance_left(self):
        try:          
            GPIO.output(PIN_TRIGGER_LEFT, False)
            while GPIO.input(PIN_ECHO_LEFT) == 0:
                nosig = time.time()

            while GPIO.input(PIN_ECHO_LEFT) == 1:
                sig = time.time()

            tl = sig - nosig
            distance = tl / 0.000058
            GPIO.output(PIN_TRIGGER_LEFT, True)
            
            return distance
        except:
            distance = 100
            return distance
            
    def get_distance_right(self):
        try:          
            GPIO.output(PIN_TRIGGER_RIGHT, False)
            while GPIO.input(PIN_ECHO_RIGHT) == 0:
                nosig = time.time()

            while GPIO.input(PIN_ECHO_RIGHT) == 1:
                sig = time.time()

            tl = sig - nosig
            distance = tl / 0.000058
            GPIO.output(PIN_TRIGGER_RIGHT, True)
            
            return distance
        except:
            distance = 100
            return distance