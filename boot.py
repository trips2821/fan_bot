from machine import Pin

all_pins = [0,2,4,5,12,13,14,15,16]

for pin in all_pins:
	p = Pin(pin, Pin.OUT)
	p.value(0)
	
import webrepl
webrepl.start()
