# fan_bot for MicroPython
# authors: Tom Stephens & Matthew Johnson
#
# motor.py
# Simple class for driving a motor

from machine import PWM, Pin

class Motor:
	def __init__(self, pin_fwd, pin_rev):
		"""
		Takes a PWM pin for forward and reverse.
		Sets the values to 0, make sure  we're off
		"""
		p_fwd = Pin(pin_fwd, Pin.OUT)
		p_fwd.value(0)
		p_rev = Pin(pin_rev, Pin.OUT)
		p_rev.value(0)
		self.fwd = PWM(p_fwd)
		self.rev = PWM(p_rev)

	def move(self, spd):
		"""
		Take speed as positive or negative. Negative is reverse.
		There is no max to the speed, this will depend on the frequency set.
		"""
		if spd > 0:
			self.rev.duty(0)
			self.fwd.duty(spd)
		else:
			self.fwd.duty(0)
			self.rev.duty(abs(spd))
			

	def stop(self):
		self.rev.duty(0)
		self.fwd.duty(0)
