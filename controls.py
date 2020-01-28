from enum import Enum
from time import sleep
import RPi.GPIO as GPIO
import events

# Classes
class Direction(Enum):
    FORWARD = 1
    BACKWARDS = 2
    LEFT = 3
    RIGHT = 4

class Motor:
    def __init__(self, side, pins):
        self.side = side
        self.__pins = pins

    def __step(self, states):
        for i in range(0, 4):
            GPIO.output(self.__pins[i], states[i])
        sleep(globals()["__MOTOR_DELAY"])

    def __step_forward(self):
        instructions = globals()["__INSTRUCTIONS"]
        for i in range(0, len(instructions)):
            self.__step(instructions[len(instructions) - i - 1])

    def __step_backwards(self):
        for s in globals()["__INSTRUCTIONS"]:
            self.__step(s)

    def forward(self, time):
        for t in range(0, int(time / (globals()["__MOTOR_DELAY"] * 4))):
            self.__step_forward()

    def backwards(self, time):
        for t in range(0, int(time / (globals()["__MOTOR_DELAY"] * 4))):
            self.__step_backwards()

# API methods
def end():
    GPIO.cleanup()

def poll():
    for pin in __INPUT_PINS.values():
        state = GPIO.input(pin)
        if state == 0 and last_input_state[str(pin)] == 1:
            last_input_state[str(pin)] = 0
            if pin == 12:
                events.BumperPressEvent.fire({"side": Direction.RIGHT})
            elif pin == 16:
                events.BumperPressEvent.fire({"side": Direction.LEFT})
            elif pin == 21:
                events.BalloonEvent.fire({})
        elif state == 1 and last_input_state[str(pin)] == 0:
            last_input_state[str(pin)] = 1
            if pin == 12:
                events.BumperReleaseEvent.fire({"side": Direction.RIGHT})
            elif pin == 16:
                events.BumperReleaseEvent.fire({"side": Direction.LEFT})

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
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 1]
]

__MOTOR_DELAY = 0.002

# Initialize GPIO pins
GPIO.setmode(GPIO.BCM)
for pin in __INPUT_PINS.values():
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
for pin in __OUTPUT_PINS.values():
    GPIO.setup(pin, GPIO.OUT)

LEFT_MOTOR = Motor(Direction.LEFT, [2, 3, 4, 17])
RIGHT_MOTOR = Motor(Direction.RIGHT, [27, 22, 10, 9])

last_input_state = {
        "12": 1,
        "16": 1,
        "21": 1
}