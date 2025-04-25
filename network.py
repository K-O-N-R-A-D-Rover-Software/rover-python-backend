import socket
import time

class Network:

    def sendToApp(self, data):
        print("sending ", data)
        self.sock.sendto(data.encode(), self.REMOTE)

    def __init__(self):
        self.IP = ""
        self.PORT = 5000
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.IP, self.PORT))
        self.lastping = -1
        self.connected = False
        self.REMOTE = []

    def connectToApp(self):
        self.getClientIp()
        self.pingThread = threading.Thread(target=self.ping)
        self.pingThread.daemon = True
        self.pingThread.start()
        self.handleInput()

    def getClientIp(self):
        print("connecting")
        while not self.connected:
            data, address = self.sock.recvfrom(64)
            time.sleep(.1)
            print(str(data))
            if (str(data).split("#")[0]== "ping" and address != ""):
                print("successful handshake with "+ str(address))
                self.lastPing = 0
                self.REMOTE = address
                self.connected = True
                return True

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

    def ping(self):
        while self.connected:
            if self.lastPing >= 4000:
                self.fullStop()
                self.getClientIp()
                return
            self.sendToApp("ping")
            print("ping sent")
            time.sleep(.5)
            self.lastPing += 200

