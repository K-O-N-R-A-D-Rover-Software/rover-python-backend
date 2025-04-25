import time
import threading
import socket
from dataServer import dataServer
from motorController import motorController

class Main:

    def __init__(self):
        self.dataServer = dataServer
        self.dataServer.init(self.dataServer)
        self.motorController = motorController
        self.motorController.init(self.motorController)

        self.IP = ""
        self.PORT = 5000
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.IP, self.PORT))
        self.lastping = -1
        self.connected = False
        self.REMOTE = []

        self.connectToApp()
        self.pingThread = threading.Thread(target=self.ping)
        self.pingThread.daemon = True
        self.pingThread.start()

        self.measurementThread = threading.Thread(target=self.measure)
        self.measurementThread.daemon = True
        self.measurementThread.start()


        while True:
            self.handleInput()

    def connectToApp(self):
        self.connected = False
        self.getClientIp()

    def sendToApp(self, data):
        print("sending", data)
        self.sock.sendto(data.encode(), self.REMOTE)

    def getClientIp(self):
        print("connecting")
        while not self.connected:
            data, address = self.sock.recvfrom(64)
            time.sleep(.1)
            print(str(data))
            if (data != "" and address != ""):
                print("successful handshake with "+ str(address))
                self.lastPing = 0
                self.REMOTE = address
                self.connected = True
                return True

    def ping(self):
        while True:
            if self.lastPing >= 4000:
                self.motorController.fullStop(self.motorController)
                self.connected = False
                self.connectToApp()
            self.sendToApp("ping")
            time.sleep(.5)
            self.lastPing += 200

    def handleInput(self):
        while self.connected:
            data, address = self.sock.recvfrom(256)
            data = str(data)[2:-1].split('#')
            print(data[0])
            if (data[0] != ""):# and address == self.REMOTE):
                match data[0]:
                    case "motors":
                        self.motorController.setDrivingMotors(self.motorController, (data[1]),float(data[2]),float(data[3]),float(data[4]))
                        self.lastPing = 0
                    case "ping":
                        print("ping recieved")
                        #self.sock.sendto("ping".encode(), self.REMOTE)
                        self.lastPing = 0
                    case "handshake":
                        self.connectToApp()
                    case "arm":
                        self.motorController.setArmMotors(self.motorController, float(data[1]),float(data[2]))
                    case "greifer":
                        self.motorController.setGreiferMotor(self.motorController, float(data[1]))
                    case "stop":
                        self.motorController.fullStop(self.motorController)

    def measure(self):
        while True:
            self.dataServer.recordMeasurement(self.dataServer)
            self.sendToApp(self.dataServer.getMeasurementToRemote(self.dataServer))
            time.sleep(1)

if __name__ == '__main__':
    Main()
