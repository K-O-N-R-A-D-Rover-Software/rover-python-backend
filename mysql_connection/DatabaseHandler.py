import mysql.connector

from Measurement import Measurement

class DatabaseHandler:

    def __init__(self):
        self.connectToDB()

    def connectToDB(self):
        self.conn = mysql.connector.connect(user='rover', password='rover', host='10.201.202.236', port=3306, database='rover')
        #self.conn = mysql.connector.connect(user='rover', password='rover', host='127.0.0.1', port=3306, database='rover')
        if (self.conn.is_connected()) :
            print("connected")
        else :
            print("not connected")

    def readLatestMeasurement(self) -> Measurement:
        sql = "SELECT id, timestamp, pressureInhPa, tempInC, magnetFieldInGauss, gyroscopeInDPS, accellerationInG FROM measurement ORDER BY timestamp DESC LIMIT 1"
        cursor = self.conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        print("Id: ", row)
        measurement = Measurement(int(row[0]), str(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]))
        return measurement

    def readLatestMeasurements(self, numberOfMeasurements) -> list[Measurement]:
        measurements = []
        sql = ("SELECT id, timestamp, pressureInhPa, tempInC, magnetFieldInGauss, gyroscopeInDPS, accellerationInG " 
               "FROM measurement ORDER BY timestamp DESC LIMIT " + str(numberOfMeasurements))
        cursor = self.conn.cursor()
        cursor.execute(sql)
        res = cursor.fetchall()
        for row in res:
            measurement = Measurement(int(row[0]), str(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]))
            measurements.append(measurement)
        return measurements


    def readMeasurementsSinceTime(self, date, time) -> list[Measurement]:
        measurements = []
        sql = ("SELECT id, timestamp, pressureInhPa, tempInC, magnetFieldInGauss, gyroscopeInDPS, accellerationInG " 
               "FROM measurement WHERE timestamp > TIMESTAMP('" + str(date) + "', '" + str(time) + "') ORDER BY timestamp DESC")
        cursor = self.conn.cursor()
        cursor.execute(sql)
        res = cursor.fetchall()
        for row in res:
            measurement = Measurement(int(row[0]), str(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]))
            measurements.append(measurement)
        return measurements

    def insertMeasurement(self, pressureInhPa, tempInC, magnetFieldInGauss, gyroscopeInDPS, accellerationInG) -> bool:
        sql = ("INSERT INTO measurement (pressureInhPa, tempInC, magnetFieldInGauss, gyroscopeInDPS, accellerationInG) "
               "VALUES (" + str(pressureInhPa) + ", " + str(tempInC) + ", " + str(magnetFieldInGauss) + ", "
               "" + str(gyroscopeInDPS) + ", " + str(accellerationInG) + ")")
        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.conn.commit()
        inserted = cursor.rowcount
        if (inserted > 0):
            print(cursor.rowcount, " measurement inserted.")
            return True
        else:
            print("No measurement inserted.")
            return False