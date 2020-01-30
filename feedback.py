import RPi.GPIO as GPIO
from time import sleep
import events

def start_motor(count, interval):
    for i in range(0, count):
        GPIO.output(OUTPUT_PINS["LED_WHITE_FRONT"],GPIO.HIGH)
        sleep(interval)
        GPIO.output(OUTPUT_PINS["LED_WHITE_FRONT"],GPIO.LOW)
        sleep(interval)

def hit_wall(interval):    
    GPIO.output(OUTPUT_PINS["LED_RED_BACK"],GPIO.HIGH)
    sleep(interval)
    GPIO.output(OUTPUT_PINS["LED_RED_BACK"],GPIO.LOW)      
    sleep(interval/2)

def away_from_wall():
    GPIO.output(OUTPUT_PINS["LED_RED_BACK"],GPIO.LOW)

def car_backward():
    GPIO.output(OUTPUT_PINS["LED_RED_BACK"], GPIO.HIGH)

def car_forward():
    GPIO.output(OUTPUT_PINS["LED_RED_BACK"], GPIO.LOW)

def balloon_popped(interval):
    GPIO.output(OUTPUT_PINS["LED_WHITE_FRONT"],GPIO.HIGH)
    GPIO.output(OUTPUT_PINS["LED_RED_BACK"],GPIO.HIGH)
    sleep(interval)
    GPIO.output(OUTPUT_PINS["LED_WHITE_FRONT"],GPIO.LOW)
    GPIO.output(OUTPUT_PINS["LED_RED_BACK"],GPIO.LOW)

def end():
    for pin in OUTPUT_PINS:
        GPIO.output(pin, GPIO.LOW)
# Initialize local constants
OUTPUT_PINS = {
    "LED_WHITE_FRONT": 26,
    "LED_RED_BACK": 19
}

# Initialize GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(OUTPUT_PINS["LED_WHITE_FRONT"],GPIO.OUT)
GPIO.setup(OUTPUT_PINS["LED_RED_BACK"],GPIO.OUT)

balloon_popped(0.05)
