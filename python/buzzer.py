import RPi.GPIO as GPIO
import threading
import logging

PIN_BUZZER = 19

class Buzzer:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(PIN_BUZZER, GPIO.OUT)
        self.buzzer_stop_event = threading.Event()

    def run(self, frequency, duration=None):
        self.p1 = GPIO.PWM(PIN_BUZZER, frequency)
        self.p1.start(50)

        if duration is not None:
            self.stop_timer = threading.Timer(duration, self.stop)
            self.stop_timer.start()

    def stop(self):
        self.p1.stop()
