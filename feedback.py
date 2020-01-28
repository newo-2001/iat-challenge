import RPi.GPIO as GPIO
from time import sleep
import events

def start_motor(interval):
    GPIO.output(OUTPUT_PINS["LED_WHITE_FRONT"],GPIO.HIGH)
    sleep(interval)
    GPIO.output(OUTPUT_PINS["LED_WHITE_FRONT"],GPIO.LOW)
    sleep(interval)
    GPIO.output(OUTPUT_PINS["LED_WHITE_FRONT"],GPIO.HIGH)


def hit_wall(interval):
    while True:
        GPIO.output(OUTPUT_PINS["LED_RED_BACK"],GPIO.HIGH)
        sleep(interval)
        GPIO.output(OUTPUT_PINS["LED_RED_BACK"],GPIO.LOW)      
        sleep(interval/2)

def away_from_wall():
    GPIO.output(OUTPUT_PINS["LED_RED_BACK"],GPIO.LOW)


def car_backward():
    GPIO.output(OUTPUT_PINS["LED_RED_BACK"], GPIO.HIGH)

def __car_forward():
    GPIO.output(OUTPUT_PINS["LED_RED_BACK"], GPIO.LOW)

def __balloon_popped(interval):
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

start_motor(0.1)