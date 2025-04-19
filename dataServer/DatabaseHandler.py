import mariadb

from Measurement import Measurement

class DatabaseHandler:

    def __init__(self):
        self.connectToDB()

    def connectToDB(self):
        try :
            self.conn = mariadb.connect(user='rover', password='rover', host='127.0.0.1', port=3306, database='rover')
        #self.conn = mysql.connector.connect(user='rover', password='rover', host='127.0.0.1', port=3306, database='rover')
            print("connected")
        except :
            print("not connected")

    def readLatestMeasurement(self) -> Measurement:
        sql = ("SELECT id, timestamp, pressureInhPa, tempInC, humidityInPerc, magnetFieldXInGauss, magnetFieldYInGauss, magnetFieldZInGauss, "
               "gyroscopeXInRadPS, gyroscopeYInRadPS, gyroscopeZInRadPS, accellerationXInMS2, accellerationYInMS2, accellerationZInMS2 "
               "FROM measurement ORDER BY timestamp DESC LIMIT 1")
        cursor = self.conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        measurement = Measurement(int(row[0]), str(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]), float(row[7]), float(row[8]), float(row[9]), float(row[10]), float(row[11]), float(row[12]), float(row[13]))
        return measurement

    def readLatestMeasurements(self, numberOfMeasurements) -> list[Measurement]:
        measurements = []
        sql = ("SELECT id, timestamp, pressureInhPa, tempInC, humidityInPerc, magnetFieldXInGauss, magnetFieldYInGauss, magnetFieldZInGauss, "
               "gyroscopeXInRadPS, gyroscopeYInRadPS, gyroscopeZInRadPS, accellerationXInMS2, accellerationYInMS2, accellerationZInMS2 "
               "FROM measurement ORDER BY timestamp DESC LIMIT " + str(numberOfMeasurements))
        cursor = self.conn.cursor()
        cursor.execute(sql)
        res = cursor.fetchall()
        for row in res:
            measurement = Measurement(int(row[0]), str(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]), float(row[7]), float(row[8]), float(row[9]), float(row[10]), float(row[11]), float(row[12]), float(row[13]))
        return measurements


    def readMeasurementsSinceTime(self, date, time) -> list[Measurement]:
        measurements = []
        sql = ("SELECT id, timestamp, pressureInhPa, tempInC, humidityInPerc, magnetFieldXInGauss, magnetFieldYInGauss, magnetFieldZInGauss, "
               "gyroscopeXInRadPS, gyroscopeYInRadPS, gyroscopeZInRadPS, accellerationXInMS2, accellerationYInMS2, accellerationZInMS2 "
               "FROM measurement WHERE timestamp > TIMESTAMP('" + str(date) + "', '" + str(time) + "') ORDER BY timestamp DESC")
        cursor = self.conn.cursor()
        cursor.execute(sql)
        res = cursor.fetchall()
        for row in res:
            measurement = Measurement(int(row[0]), str(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]), float(row[7]), float(row[8]), float(row[9]), float(row[10]), float(row[11]), float(row[12]), float(row[13]))
            measurements.append(measurement)
        return measurements

    def insertMeasurement(self, pressureInhPa, tempInC, humidityInPerc, magnetFieldXInGauss, magnetFieldYInGauss, magnetFieldZInGauss, gyroscopeXInRadPS, gyroscopeYInRadPS, gyroscopeZInRadPS, accellerationXInMS2, accellerationYInMS2, accellerationZInMS2) -> bool:
        sql = ("INSERT INTO measurement (pressureInhPa, tempInC, humidityInPerc, magnetFieldXInGauss, magnetFieldYInGauss, magnetFieldZInGauss, "
               "gyroscopeXInRadPS, gyroscopeYInRadPS, gyroscopeZInRadPS, accellerationXInMS2, accellerationYInMS2, accellerationZInMS2) "
               "VALUES (" + str(pressureInhPa) + ", " + str(tempInC) + ", " + str(humidityInPerc) + ", "
               "" + str(magnetFieldXInGauss) + ", " + str(magnetFieldYInGauss) + ", " + str(magnetFieldZInGauss) + ", "
               "" + str(gyroscopeXInRadPS) + ", " + str(gyroscopeYInRadPS) + ", " + str(gyroscopeZInRadPS) + ", "
               "" + str(accellerationXInMS2) + ", " + str(accellerationYInMS2) + ", " + str(accellerationZInMS2) + ")")
        cursor = self.conn.cursor()
        cursor.execute(sql)
        inserted = cursor.rowcount
        self.conn.commit()
        if (inserted > 0):
            print(inserted, " measurement inserted.")
            return True
        else:
            print("No measurement inserted.")
            return False
