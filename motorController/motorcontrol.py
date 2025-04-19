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
                print("successful handshake with " + address[0])
                self.sock.sendto("ping".encode(), address)
                return address
                break

    def ping(self):
        while True:
            self.lastPing += 500
            if self.lastPing >= 4000:
                self.panicStop()
            self.sock.sendto("ping".encode(), self.REMOTE)
            print("ping sent")
            time.sleep(.5)

    def panicStop(self):
        self.setDrivingMotors(0,0,0,0)

    def setDrivingMotors(self, m1,m2,m3,m4):
        self.hat1.motor1.throttle = m1
        self.hat1.motor2.throttle = m2
        self.hat1.motor3.throttle = m3
        self.hat1.motor4.throttle = m4

    def handleInput(self):
        while True:
            print("hi")
            data, address = self.sock.recvfrom(64)
            data = str(data)[2:-1].split('#')
            print(data[0])
            if (data[0] != ""):# and address == self.REMOTE):
                match data[0]:
                    case "motors":
                        self.setDrivingMotors(float(data[1]),float(data[2]),float(data[3]),float(data[4]))
                    case "ping":
                        print("ping")
                        self.lastPing = 0

    def __init__(self):
        self.IP = ""
        self.PORT = 5000
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.IP, self.PORT))
        self.REMOTE = self.getClientIp()
        self.lastPing = -1
        self.hat1 = MotorKit(i2c=board.I2C(), address = 0x60)
        self.hat2 = MotorKit(i2c=board.I2C(), address = 0x61)
        self.pingThread = threading.Thread(self.ping())
        self.pingThread.daemon = True
        self.pingThread.start()
        print("handle")
        self.inputThread = threading.Thread(self.handleInput())
        self.inputThread.daemon = True
        self.inputThread.start()

if __name__ == '__main__':
    Main()
