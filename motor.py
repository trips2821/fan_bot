from machine import PWM, Pin

class Motor:
	def __init__(self, pin_fwd, pin_rev):
		p_fwd = Pin(pin_fwd, Pin.OUT)
		p_fwd.value(0)
		p_rev = Pin(pin_rev, Pin.OUT)
		p_rev.value(0)
		self.fwd = PWM(p_fwd)
		self.rev = PWM(p_rev)

	def move(self, spd):
		if spd > 0:
			self.rev.duty(0)
			self.fwd.duty(spd)
		else:
			self.fwd.duty(0)
			self.rev.duty(abs(spd))
			

	def stop(self):
		self.rev.duty(0)
		self.fwd.duty(0)
