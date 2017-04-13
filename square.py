# fan_bot for MicroPython
# authors: Tom Stephens & Matthew Johnson
#
# square.py
# Drive the bot in roughly a square-ish shape

from time import sleep

LINE_TIME = 3
LINE_SPEED = 4

TURN_TIME = 1
TURN_SPEED = 3


def run(fan_bot):
	fan_bot.forward(LINE_SPEED)
	sleep(LINE_TIME)
	fan_bot.turn_left(TURN_SPEED)
	sleep(TURN_TIME)
	fan_bot.forward(LINE_SPEED)
	sleep(LINE_TIME)
	fan_bot.turn_left(TURN_SPEED)
	sleep(TURN_TIME)
	fan_bot.forward(LINE_SPEED)
	sleep(LINE_TIME)
	fan_bot.turn_left(TURN_SPEED)
	sleep(TURN_TIME)
	fan_bot.forward(LINE_SPEED)
	sleep(LINE_TIME)
	fan_bot.stop()
