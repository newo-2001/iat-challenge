import events
import controls as io
import threading
import asyncio
from time import sleep

def loop():
    while True:
        io.poll()
        sleep(0.02)

async def main():
    # Register event handlers
    events.BumperPressEvent.listen(button_callback)
    events.BumperReleaseEvent.listen(button_release_callback)
    events.BalloonEvent.listen(balloon_callback)

    # Make a new thread for the event-poll loop
    thread = threading.Thread(target=loop)
    thread.daemon = True # Exit when the main thread exits
    thread.start()

    # Car logic
    await io.CAR.forward(-1)
    sleep(0.5)
    await io.CAR.backwards(1)
    
    # Wait indefinitely
    while True:
        sleep(1)

    # Give io the shutdown signal so it can gracefully exit
    io.end()

def button_callback(event):
    print(event["side"].name + " has been pressed")
    io.CAR.stop()

def balloon_callback(event):
    print("Balloon has been pressed")

def button_release_callback(event):
    print(event["side"].name + " has been pressed")

if __name__ == "__main__":
    asyncio.run(main())
else:
    print("This file cannot be loaded as a module")
