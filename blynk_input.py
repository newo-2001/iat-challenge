import blynklib
import feedback
import threading
import controls
import asyncio
import main
import sys
from time import sleep

BLYNK_AUTH = 'mz2Zl4gY8cWqcg2Ag2latyNb7SylKGmG'

# initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)
started = False

# start
@blynk.handle_event('write V3')
def start_input(pin, value):
    global started
    if not started:
        thread = threading.Thread(target=main.run)
        thread.daemon = True
        thread.start()
    else:
        controls.CAR.stop()
        main.kill()
        exit()
    started = True

# links
@blynk.handle_event('write V0')
def links_input(pin, value):
    print(value)
    if not main.alive:
        return

    if int(value[0]):
        main.blynk = True
        controls.CAR.stop()
        sleep(0.5)
        asyncio.run(controls.CAR.turn_angle(90))
        print(value, pin)
        main.blynk = False


# rechts
@blynk.handle_event('write V1')
def rechts_input(pin, value):
    if not main.alive:
        return

    if int(value[0]):
        main.blynk = True
        controls.CAR.stop()
        sleep(0.5)
        asyncio.run(controls.CAR.turn_angle(-90))
        # NAAR RECHTS
        print(value, pin)
        main.blynk = False

# 180 graden
@blynk.handle_event('write V2')
def rotate_input(pin, value):
    if not main.alive:
        return
    
    if int(value[0]):
        main.blynk = True
        controls.CAR.stop()
        asyncio.run(controls.CAR.turn_angle(180))
        # 180 GRADEN
        print(value, pin)
        main.blynk = False

while True:
    blynk.run()
    sleep(0.001)
