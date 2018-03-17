import RPi.GPIO as GPIO
import logging

PWMA1 = 6
PWMA2 = 13
PWMB1 = 20
PWMB2 = 21
D1 = 12
D2 = 26

class Drive:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(PWMA1, GPIO.OUT)
        GPIO.setup(PWMA2, GPIO.OUT)
        GPIO.setup(PWMB1, GPIO.OUT)
        GPIO.setup(PWMB2, GPIO.OUT)
        GPIO.setup(D1, GPIO.OUT)
        GPIO.setup(D2, GPIO.OUT)
        self.p1 = GPIO.PWM(D1, 500)
        self.p2 = GPIO.PWM(D2, 500)
    
        self.p1.start(99)
        self.p2.start(99)
        self.stop_motor()

    def drive_forward(self, speed):
        self.set_drive(1, 0, 0, 1, speed)

    def stop_motor(self):
        self.set_drive(0, 0, 0, 0, 0)

    def drive_backward(self, speed):
        self.set_drive(0, 1, 1, 0, speed)

    def turn_left(self, speed):
        self.set_drive(0, 1, 0, 1, speed)

    def turn_right(self, speed):
        self.set_drive(1, 0, 1, 0, speed)

    def set_drive(self, a1, a2, b1, b2, end_speed):
        try:
            self.p1.ChangeDutyCycle(end_speed)
            self.p2.ChangeDutyCycle(end_speed)
        except Exception as e:
            self.stop_motor()
            logging.error("Failed to set motor duty cycle: ", e)

        try:
            GPIO.output(PWMA1, a1)
            GPIO.output(PWMA2, a2)
            GPIO.output(PWMB1, b1)
            GPIO.output(PWMB2, b2)
        except Exception as e:
            self.stop_motor()
            logging.error("Failed to set motor outputs: ", e)

