from enum import Enum
from time import sleep
import RPi.GPIO as GPIO
import event

# Classes
class Direction(Enum):
    FORWARD = 1
    BACKWARDS = 2
    LEFT = 3
    RIGHT = 4

class Motor:
    __init__(self, side, pins):
        self.side = side
        self.__pins = pins

    __step(self, states):
        for i in range(0, 4):
            GPIO.output(self.__pins[i], states[i])

    __step_forward():
        for i in range(0, len(__INSTRUCTIONS)):
            step(__INSTRUCTIONS[len(__INSTRUCTIONS - i - 1)]):

    __step_backwards():
        for s in __INSTRUCTIONS:
            step(s)

    forward(time):
        for t in range(0, time / __MOTOR_DELAY):
            __step_forward()
            sleep(__MOTOR_DELAY)

    backwards(time):
        for t in range(0, time / __MOTOR_DELAY):
            __step_backwards()
            sleep(__MOTOR_DELAY)

# API methods
def end():
    GPIO.cleanup()

def poll():
    for pin in __INPUT_PINS.items():
        if GPIO.input() == 0:
            if pin == 12:
                events.BumperEvent.fire({"side": Direction.RIGHT})
            elif pin == 16:
                events.BumperEvent.fire({"side": Direction.LEFT})
            elif pin == 21:
                events.BalloonEvent.fire({})

# Initialize local constants
__INPUT_PINS = {
    "BUTTON_BUMPER_RIGHT": 12,
    "BUTTON_BUMPER_LEFT": 16,
    "BUTTON_BALLOON": 21
}

__OUTPUT_PINS = {
    "MOTOR_LEFT_1": 2,
    "MOTOR_LEFT_2": 3,
    "MOTOR_LEFT_3": 4,
    "MOTOR_LEFT_4": 17,
    "MOTOR_RIGHT_1": 27,
    "MOTOR_RIGHT_2": 22,
    "MOTOR_RIGHT_3": 10,
    "MOTOR_RIGHT_4": 9
}

__INSTRUCTIONS = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 1]
]

__MOTOR_DELAY = 0.002

# Initialize GPIO pins
GPIO.setmode(GPIO.BCM)
for pin in __INPUT_PINS.items():
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
for pin in __OUTPUT_PINS.items():
    GPIO.setup(pin, GPIO.OUT)

LEFT_MOTOR = Motor(Direction.LEFT, [2, 3, 4, 17])
RIGHT_MOTOR = Motor(Direction.RIGHT, [27, 22, 10, 9])
