import blynklib


BLYNK_AUTH = 'mz2Zl4gY8cWqcg2Ag2latyNb7SylKGmG'

# initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)


#links
@blynk.handle_event('write V0')
def links_input(pin, value):
	if int(value[0]):
		#NAAR LINKS
		print(value, pin)


#rechts
@blynk.handle_event('write V1')
def rechts_input(pin, value):
	if int(value[0]):
		#NAAR RECHTS
		print(value, pin)

#180 graden
@blynk.handle_event('write V2')
def rotate_input(pin, value):
	if int(value[0]):
		#180 GRADEN
		print(value, pin)

while True:
	blynk.run()
