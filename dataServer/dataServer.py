import board
import adafruit_lps2x
import adafruit_lsm9ds1
import adafruit_hts221
from Measurement import Measurement
from DatabaseHandler import DatabaseHandler
import time
import sys
import socket

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

    def __init__(self):
        self.IP = ""
        self.PORT = 5000
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.IP, self.PORT))
        self.REMOTE = []
        self.getClientIp()
        self.i2c = board.I2C()
        # Pressure
        self.pressure = adafruit_lps2x.LPS25(i2c_bus=self.i2c, address=0x5c)
        #Acceleration, Magentic Field, Gyroscope, Temperature
        self.accel = adafruit_lsm9ds1.LSM9DS1_I2C(i2c=self.i2c, mag_address=0x1C,xg_address=0x6A)
        #Relative humidity, Temperature
        self.humidity = adafruit_hts221.HTS221(self.i2c)
        self.db = DatabaseHandler()
        while True:
            self.getMeasurement()
            time.sleep(1)

    def getMeasurement(self):
        pressure = self.pressure.pressure
        self.accellist =  list(self.accel.acceleration)
        accelx = self.accellist[0]
        accely = self.accellist[1]
        accelz = self.accellist[2]
        self.maglist =  list(self.accel.magnetic)
        magx = self.maglist[0]
        magy = self.maglist[1]
        magz = self.maglist[2]
        self.gyrolist =  list(self.accel.gyro)
        gyrox = self.gyrolist[0]
        gyroy = self.gyrolist[1]
        gyroz = self.gyrolist[2]
        humidity = self.humidity.relative_humidity
        humidityTemp = self.humidity.temperature
        # insert all measurement values into the database
        self.db.insertMeasurement(pressure, humidityTemp, humidity, magx, magy, magz, gyrox, gyroy, gyroz, accelx, accely, accelz)
        # get latest measurement and send them to the app
        measurement = self.db.readLatestMeasurement()
        self.sock.sendto(measurement.toRemote().encode(), self.REMOTE)

if __name__ == '__main__':
    Main()

