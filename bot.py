# fan_bot for MicroPython
# authors: Tom Stephens & Matthew Johnson
#
# bot.py
# Simple Class for a two wheel drive bot

class Bot:
	def __init__(self, motor_left, motor_right):
		self.left = motor_left
		self.right = motor_right

	def __translate_speed(self, spd):
		"""
		To simplify the speed property we translate to the right duty cycle
		based on a 0-4 number.
		"""
		if spd >= 4:
			return 1024
		elif spd == 3:
			return 750
		elif spd == 2:
			return 500
		elif spd == 1:
			return 250
		else:
			return 0

	def forward(self, spd):
		t_spd = self.__translate_speed(spd)
		self.left.move(t_spd)
		self.right.move(t_spd)

	def backwards(self, spd):
		t_spd = self.__translate_speed(spd)
		self.left.move(t_spd * -1)
		self.right.move(t_spd * -1)	

	def turn_left(self, spd):
		"""
		Zero radius turn right
		"""
		t_spd = self.__translate_speed(spd)
		self.left.move(t_spd * -1)
		self.right.move(t_spd)

	def turn_right(self, spd):
		"""
		Zero radius turn right
		"""
		t_spd = self.__translate_speed(spd)
		self.left.move(t_spd)
		self.right.move(t_spd * -1)

	def stop(self):
		self.left.stop()
		self.right.stop()	
