import board
import adafruit_lps2x
import adafruit_lsm9ds1
import adafruit_hts221
from Measurement import Measurement
from DatabaseHandler import DatabaseHandler
import time
import sys
import socket

class dataServer:

    def init(self):
        self.i2c = board.I2C()
        # Pressure
        self.pressure = adafruit_lps2x.LPS25(i2c_bus=self.i2c, address=0x5c)
        #Acceleration, Magentic Field, Gyroscope, Temperature
        self.accel = adafruit_lsm9ds1.LSM9DS1_I2C(i2c=self.i2c, mag_address=0x1C,xg_address=0x6A)
        #Relative humidity, Temperature
        self.humidity = adafruit_hts221.HTS221(self.i2c)
        self.db = DatabaseHandler()

    def recordMeasurement(self):
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

    def getMeasurementToRemote(self):
        return self.db.readLatestMeasurement().toRemote()
