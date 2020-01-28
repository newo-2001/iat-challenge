import RPI.GPIO as GPIO
from time import sleep
import events

class Feedback:
    def __start_motor(self, interval):
        GPIO.output(OUTPUT_PINS["LED_WHITE_FRONT"],GPIO.HIGH)
        sleep(interval)
        GPIO.output(OUTPUT_PINS["LED_WHITE_FRONT"],GPIO.LOW)
        sleep(interval)
        GPIO.output(OUTPUT_PINS["LED_WHITE_FRONT"],GPIO.HIGH)

    def __hit_wall(self, interval):
        while True:
            GPIO.output(OUTPUT_PINS["LED_RED_BACK"],GPIO.HIGH)
            sleep(interval)
            GPIO.output(OUTPUT_PINS["LED_RED_BACK"],GPIO.LOW)
            sleep(interval/2)

    def __away_from_wall(self):
        GPIO.output(OUTPUT_PINS["LED_RED_BACK"],GPIO.LOW)

    def __car_backward(self):
        GPIO.output(OUTPUT_PINS["LED_RED_BACK"], GPIO.HIGH)

    def __car_forward(self):
        GPIO.output(OUTPUT_PINS["LED_RED_BACK"], GPIO.LOW)

    def __balloon_popped(self, interval):
        while True:
            GPIO.output(OUTPUT_PINS["LED_WHITE_FRONT"],GPIO.HIGH)
            GPIO.output(OUTPUT_PINS["LED_RED_BACK"],GPIO.HIGH)
            sleep(interval)
            GPIO.output(OUTPUT_PINS["LED_WHITE_FRONT"],GPIO.LOW)
            GPIO.output(OUTPUT_PINS["LED_RED_BACK"],GPIO.LOW)
            sleep(interval)

# Initialize local constants
OUTPUT_PINS = {
    "LED_WHITE_FRONT": 26,
    "LED_RED_BACK": 19
}

# Initialize GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)