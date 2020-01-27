import events
import io
from time import sleep

def main():
    print("Hello world!")

    events.BumperEvent.listen(button_callback)
    events.BalloonEvent.listen(balloon_callback)

    sleep(0.5)
    io.RIGHT_MOTOR.backwards(2)
    sleep(0.5)
    io.RIGHT_MOTOR.forward(2)
    sleep(0.5)
    io.LEFT_MOTOR.backwards(2)
    sleep(0.5)
    io.LEFT_MOTOR.forward(2)
    sleep(0.5)

    while True:
        io.poll()
        sleep(0.02)
    
    io.end()

def button_callback(event):
    print(event["side"].name + " has been pressed")

def balloon_callback(event):
    print("Balloon has been pressed")

if __name__ == "__main__":
    main()
else:
    print("This file cannot be loaded as a module")
