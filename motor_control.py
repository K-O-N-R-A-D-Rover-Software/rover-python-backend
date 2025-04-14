import board
from adafruit_motorkit import MotorKit

kit = MotorKit(address=0x61)
#Motor 1 geht an
kit.motor1.throttle = 1
