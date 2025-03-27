from DatabaseHandler import DatabaseHandler

db = DatabaseHandler()
print()
print("readLatestMeasurement():")
measurement = db.readLatestMeasurement()
print(measurement.toString())
print("Temp: " + str(measurement.getTempInC()) + "°C")
print()
print("readLatestMeasurements(10):")
measurements = db.readLatestMeasurements(10)
for m in measurements:
    print(m.toString())
print()
print("readMeasurementsSinceTime(\"2025-03-25\", \"12:57:00\"):")
measurements = db.readMeasurementsSinceTime("2025-03-25", "12:57:00")
for m in measurements:
    print(m.toString())
#print()
#print("insertMeasurement(1015, 18.9, 3.96, 0.431, 0.247):")
#db.insertMeasurement(1003, 12.5, 4.21, 0.1, 0.0)