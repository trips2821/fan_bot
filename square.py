from time import sleep

LINE_TIME = 3
LINE_SPEED = 4

TURN_TIME = 1
TURN_SPEED = 3


def run(fanatics_bot):
	fanatics_bot.forward(LINE_SPEED)
	sleep(LINE_TIME)
	fanatics_bot.turn_left(TURN_SPEED)
	sleep(TURN_TIME)
	fanatics_bot.forward(LINE_SPEED)
	sleep(LINE_TIME)
	fanatics_bot.turn_left(TURN_SPEED)
	sleep(TURN_TIME)
	fanatics_bot.forward(LINE_SPEED)
	sleep(LINE_TIME)
	fanatics_bot.turn_left(TURN_SPEED)
	sleep(TURN_TIME)
	fanatics_bot.forward(LINE_SPEED)
	sleep(LINE_TIME)
	fanatics_bot.stop()
