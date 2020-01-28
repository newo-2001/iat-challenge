import blynklib



BLYNK_AUTH = 'mz2Zl4gY8cWqcg2Ag2latyNb7SylKGmG'

# initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)


# register handler for virtual pin V4 write event
@blynk.handle_event('write V4')
def read_virtual_pin_handler(pin, value):
    if int(value[0]) == 1:
        print('ja')
 
while True:
	blynk.run()
