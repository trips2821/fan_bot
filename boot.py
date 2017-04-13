# fan_bot for MicroPython
# authors: Tom Stephens & Matthew Johnson
#
# boot.py
# make sure all pins are off on boot
# start from a known state

from machine import Pin
import webrepl

# these are the pins available on an ESP8266
for pin in [0,2,4,5,12,13,14,15,16]:
	p = Pin(pin, Pin.OUT)
	p.value(0)
	
webrepl.start()
