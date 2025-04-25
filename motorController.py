import time
import board
import socket
import threading
from adafruit_motorkit import MotorKit

class motorController:

    def init(self):
        #self.hat1 = MotorKit(i2c=board.I2C(), address = 0x60)
        self.hat2 = MotorKit(i2c=board.I2C(), address = 0x61)

    def fullStop(self):
        #self.hat1.motor1.throttle = 0
        #self.hat1.motor2.throttle = 0
        #self.hat1.motor3.throttle = 0
        #self.hat1.motor4.throttle = 0
        self.hat2.motor1.throttle = 0
        self.hat2.motor2.throttle = 0
        self.hat2.motor3.throttle = 0
        self.hat2.motor4.throttle = 0
        print("panic-shutoff")

    def setDrivingMotors(self, m1,m2,m3,m4):
        print("drive")
        #self.hat1.motor1.throttle = m1
        #self.hat1.motor2.throttle = m2
        #self.hat1.motor3.throttle = m3
        #self.hat1.motor4.throttle = m4

    def setArmMotors(self, m1,m2):
        print("arm")
        self.hat2.motor1.throttle = m1
        self.hat2.motor2.throttle = m2

    def setGreiferMotor(self, m1):
        print("greifer")
        self.hat2.motor3.throttle = m1

if __name__ == '__main__':
    motorController()
