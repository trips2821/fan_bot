from motor import Motor
from bot import Bot

PIN_LEFT_FWD = 14
PIN_LEFT_REV = 12

PIN_RIGHT_FWD = 13
PIN_RIGHT_REV = 15

motor_left = Motor(PIN_LEFT_FWD, PIN_LEFT_REV)
motor_right = Motor(PIN_RIGHT_FWD, PIN_RIGHT_REV)

fan_bot = Bot(motor_left, motor_right)