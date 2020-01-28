import blynklib

waarde = 0

BLYNK_AUTH = 'mz2Zl4gY8cWqcg2Ag2latyNb7SylKGmG'

# initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

WRITE_EVENT_PRINT_MSG = "[WRITE_VIRTUAL_PIN_EVENT] Pin: V{} Value: '{}'"



# register handler for virtual pin V4 write event
@blynk.handle_event('write V4')
def read_virtual_pin_handler(pin, value):
	global waarde
	if int(value[0]) == 1:

		kaas()



@blynk.handle_event('write V11')
def read_virtual_pin_handler(pin):
	global waarde
	blynk.virtual_write(pin, waarde)

while True:
	blynk.run()
