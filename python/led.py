from neopixel import *
import time
import logging
import threading

# LED strip configuration:
LED_COUNT = 27  # Number of LED pixels.
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_PIN = 18


class Led:

    def __init__(self):
        try:
            self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ)
            self.strip.begin()
        except Exception as e:
            logging.error("Initialization of NeoPixel failed: ", e)
        
        self.led_stop_event = threading.Event()

    def knight_rider_on(self):
        logging.info("Knight rider light on")
        self.knight_rider_thread = threading.Thread(target=self.knight_rider, args=(self.led_stop_event,))
        self.knight_rider_thread.start()
        
    def knight_rider_off(self):
        self.led_stop_event.set()
        
    def police_on(self):
        logging.info("Knight rider light on")
        self.police_thread = threading.Thread(target=self.police, args=(self.led_stop_event,))
        self.police_thread.start()
        
    def police_off(self):
        self.led_stop_event.set()

    def light_on(self):
        self.strip.setPixelColorRGB(0, 128, 200, 200)
        self.strip.setPixelColorRGB(5, 128, 200, 200)
        self.strip.setPixelColorRGB(8, 128, 200, 200)
        self.strip.setPixelColorRGB(13, 128, 200, 200)
        self.strip.setPixelColorRGB(18, 128, 200, 200)
        self.strip.setPixelColorRGB(21, 128, 200, 200)
        self.strip.setPixelColorRGB(26, 128, 200, 200)
        self.strip.show()

    def light_off(self):
        self.strip.setPixelColorRGB(0, 0, 0, 0)
        self.strip.setPixelColorRGB(5, 0, 0, 0)
        self.strip.setPixelColorRGB(8, 0, 0, 0)
        self.strip.setPixelColorRGB(13, 0, 0, 0)
        self.strip.setPixelColorRGB(18, 0, 0, 0)
        self.strip.setPixelColorRGB(21, 0, 0, 0)
        self.strip.setPixelColorRGB(26, 0, 0, 0)
        self.strip.show()


    def dim_color(self, color):
        try:
            red = (int(int(color & 0xff0000) / 3) & 0xff0000)
            green = (int(int(color & 0x00ff00) / 3) & 0x00ff00)
            blue = (int(int(color & 0x0000ff) / 3) & 0x0000ff)
        except Exception as e:
            logging.error("Failed to dim color: ", e)
        return (red + green + blue)

    def police(self, event):
        brightness = 128
        while not event.is_set():
            # Blue twice
            for i in range(0, int(self.strip.numPixels() / 2)):
                color = Color(0, brightness, 0)
                self.strip.setPixelColor(i, color)
            self.strip.show()
            time.sleep(0.1)
            for i in range(0, int(self.strip.numPixels() / 2)):
                color = Color(0, 0, 0)
                self.strip.setPixelColor(i, color)
            self.strip.show()
            time.sleep(0.05)
            for i in range(0, int(self.strip.numPixels() / 2)):
                color = Color(0, brightness, 0)
                self.strip.setPixelColor(i, color)
            self.strip.show()
            time.sleep(0.1)
            for i in range(0, int(self.strip.numPixels() / 2)):
                color = Color(0, 0, 0)
                self.strip.setPixelColor(i, color)
            self.strip.show()
            time.sleep(0.1)

            # Red twice
            for i in range(int(self.strip.numPixels() / 2) + 1,
                self.strip.numPixels()):
                color = Color(0, 0, brightness)
                self.strip.setPixelColor(i, color)
            self.strip.show()
            time.sleep(0.1)
            for i in range(int(self.strip.numPixels() / 2) + 1,
                self.strip.numPixels()):
                color = Color(0, 0, 0)
                self.strip.setPixelColor(i, color)
            self.strip.show()
            time.sleep(0.05)
            for i in range(int(self.strip.numPixels() / 2) + 1,
                self.strip.numPixels()):
                color = Color(0, 0, brightness)
                self.strip.setPixelColor(i, color)
            self.strip.show()
            time.sleep(0.1)
            for i in range(int(self.strip.numPixels() / 2) + 1,
                self.strip.numPixels()):
                color = Color(0, 0, 0)
                self.strip.setPixelColor(i, color)
            self.strip.show()
            time.sleep(0.1)

        self.all_leds_off()
        event.clear()

    def knight_rider(self, event):
        while not event.is_set():
            for i in range(self.strip.numPixels()):
                color = Color(0, 255, 0)
                self.strip.setPixelColor(i, color)
                color = Color(0, 255, 0)
                self.strip.setPixelColor(i - 1, self.dim_color(color))
                color = Color(0, 128, 0)
                self.strip.setPixelColor(i - 2, self.dim_color(color))
                color = Color(0, 128, 0)
                self.strip.setPixelColor(i - 3, self.dim_color(color))
                color = Color(0, 64, 0)
                self.strip.setPixelColor(i - 4, self.dim_color(color))
                color = Color(0, 64, 0)
                self.strip.setPixelColor(i - 5, self.dim_color(color))
                color = Color(0, 32, 0)
                self.strip.setPixelColor(i - 6, self.dim_color(color))
                color = Color(0, 32, 0)
                self.strip.setPixelColor(i - 7, self.dim_color(color))
                color = Color(0, 16, 0)
                self.strip.setPixelColor(i - 8, self.dim_color(color))
                color = Color(0, 16, 0)
                self.strip.setPixelColor(i - 9, self.dim_color(color))
                color = Color(0, 8, 0)
                self.strip.setPixelColor(i - 10, self.dim_color(color))
                color = Color(0, 8, 0)
                self.strip.setPixelColor(i - 11, self.dim_color(color))
                self.strip.show()
                time.sleep(20 / 1000.0)
                for k in range(12):
                    self.strip.setPixelColor(i - k, 0)

            if event.is_set():
                break

            for i in range(self.strip.numPixels() - 1, -1, -1):
                color = Color(0, 255, 0)
                self.strip.setPixelColor(i, color)
                color = Color(0, 255, 0)
                self.strip.setPixelColor(i + 1, self.dim_color(color))
                color = Color(0, 128, 0)
                self.strip.setPixelColor(i + 2, self.dim_color(color))
                color = Color(0, 128, 0)
                self.strip.setPixelColor(i + 3, self.dim_color(color))
                color = Color(0, 64, 0)
                self.strip.setPixelColor(i + 4, self.dim_color(color))
                color = Color(0, 64, 0)
                self.strip.setPixelColor(i + 5, self.dim_color(color))
                color = Color(0, 32, 0)
                self.strip.setPixelColor(i + 6, self.dim_color(color))
                color = Color(0, 32, 0)
                self.strip.setPixelColor(i + 7, self.dim_color(color))
                color = Color(0, 16, 0)
                self.strip.setPixelColor(i + 8, self.dim_color(color))
                color = Color(0, 16, 0)
                self.strip.setPixelColor(i + 9, self.dim_color(color))
                color = Color(0, 8, 0)
                self.strip.setPixelColor(i + 10, self.dim_color(color))
                color = Color(0, 8, 0)
                self.strip.setPixelColor(i + 11, self.dim_color(color))
                self.strip.show()

                time.sleep(20 / 1000.0)

                for k in range(12):
                    self.strip.setPixelColor(i + k, 0)

        self.all_leds_off()
        event.clear()

    def all_leds_off(self):
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColorRGB(i, 0, 0, 0)
        self.strip.show()
