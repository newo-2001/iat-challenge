import events
import controls as io
import threading
import feedback
import asyncio
from time import sleep

last_button = io.Direction.LEFT
alive = True
pressed = False
done = False
blynk = False
killed = False

def loop():
    while True:
        io.poll()
        sleep(0.02)

def surrender():
    global done
    while not done:
        feedback.balloon_popped(0.5)
        sleep(0.5)

def kill():
    global killed
    killed = True


async def main():
    global alive
    global pressed
    global done
    global blynk
    global killed

    # Register event handlers
    events.BumperPressEvent.listen(button_callback)
    events.BumperReleaseEvent.listen(button_release_callback)
    events.BalloonEvent.listen(balloon_callback)

    # Make a new thread for the event-poll loop
    thread = threading.Thread(target=loop)
    thread.daemon = True # Exit when the main thread exits
    thread.start()

    feedback_thread = threading.Thread(target=feedback.start_motor, args=(3, 0.5))
    feedback_thread.daemon = True
    feedback_thread.start()

    # Car logic
    while alive:
        if killed:
            return
        while blynk:
            sleep(1)
        await io.CAR.forward(-1)
        if not alive:
            break
        if blynk:
            continue
        if killed:
            return
        sleep(0.5)
        await io.CAR.backwards(2)
        if not alive:
            break
        if blynk:
            continue
        if killed:
            return
        sleep(0.5)
        angle = (50, 80, 110, 120, 140)[floor(random.random() * 5)]
        await io.CAR.turn_angle((angle, -angle)[last_button == io.Direction.LEFT])
    
    if killed:
        return

    print("died")
    dead_thread = threading.Thread(target=surrender)
    dead_thread.daemon = True
    dead_thread.start()

    # Drive until hitting a wall
    while True:
        if killed:
            return
        await io.CAR.forward(-1)
        if killed:
            return
        sleep(7)
        if pressed:
            break
    done = True
    # Park the car
    # sleep(0.5)
    # await io.CAR.backwards(0.8)
    # done = True
    # sleep(0.5)
    # await io.CAR.turn_angle(-70)

    # Give dead signal
    while True:
        feedback.balloon_popped(0.05)
        sleep(0.05)
        if killed:
            return

    # Give io the shutdown signal so it can gracefully exit
    io.end()
    feedback.end()

def button_callback(event):
    print(event["side"].name + " has been pressed")
    global pressed
    global last_button
    pressed = True
    last_button = event["side"]
    io.CAR.stop()
def balloon_callback(event):
    print("Balloon has been pressed")
    global alive
    alive = False
    io.CAR.stop()

def button_release_callback(event):
    print(event["side"].name + " has been released")
    global pressed
    pressed = False

def run():
    asyncio.run(main())

if __name__ == "__main__":
    asyncio.run(main())
