import time
import board
import socket
import threading
from adafruit_motorkit import MotorKit

class Main:
    def getClientIp(self):
        print("waiting for handshake")
        while True:
            data, address = self.sock.recvfrom(64)
            time.sleep(.1)
            print(str(data)[2:6])
            if (str(data)[2:6] == "ping" and address!=""):
                print("successful handshake with " + str(address))
                self.sock.sendto("ping".encode(), address)
                self.lastPing = 0
                self.connected = True
                self.REMOTE = address
                return True

    def ping(self):
        while self.connected:
            if self.lastPing >= 4000:
                self.fullStop()
                self.getClientIp()
                return
            self.sock.sendto("ping".encode(), self.REMOTE)
            print("ping sent")
            time.sleep(.5)
            self.lastPing += 200

    def fullStop(self):
        self.hat1.motor1.throttle = 0
        self.hat1.motor2.throttle = 0
        self.hat1.motor3.throttle = 0
        self.hat1.motor4.throttle = 0
        self.hat2.motor1.throttle = 0
        self.hat2.motor2.throttle = 0
        self.hat2.motor3.throttle = 0
        self.hat2.motor4.throttle = 0
        print("panic-shutoff")

    def setDrivingMotors(self, m1,m2,m3,m4):
        self.hat1.motor1.throttle = m1
        self.hat1.motor2.throttle = m2
        self.hat1.motor3.throttle = m3
        self.hat1.motor4.throttle = m4

    def setArmMotors(self, m1,m2):
        self.hat2.motor1.throttle = m1
        self.hat2.motor2.throttle = m2

    def setGreiferMotor(self, m1):
        self.hat2.motor3.throttle = m1

    def handleInput(self):
        while True:
            data, address = self.sock.recvfrom(256)
            data = str(data)[2:-1].split('#')
            print(data[0])
            if (data[0] != ""):# and address == self.REMOTE):
                match data[0]:
                    case "motors":
                        self.setDrivingMotors(float(data[1]),float(data[2]),float(data[3]),float(data[4]))
                        self.lastPing = 0
                    case "ping":
                        print("ping recieved")
                        #self.sock.sendto("ping".encode(), self.REMOTE)
                        self.lastPing = 0
                    case "handshake":
                        self.getClientIp()
                    case "arm":
                        self.setArmMotors(float(data[1]),float(data[2]))
                    case "greifer":
                        self.setGreiferMotor(float(data[1]))
                    case "stop":
                        self.fullStop()

    def __init__(self):
        self.IP = ""
        self.PORT = 5000
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.IP, self.PORT))
        self.lastping = -1
        self.connected = False
        self.REMOTE = []
        self.getClientIp()
        self.hat1 = MotorKit(i2c=board.I2C(), address = 0x60)
        self.hat2 = MotorKit(i2c=board.I2C(), address = 0x61)
        self.pingThread = threading.Thread(target=self.ping)
        self.pingThread.daemon = True
        self.pingThread.start()
        self.handleInput()

if __name__ == '__main__':
    Main()
