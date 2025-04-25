class Measurement:

    def __init__(self, pId: int, pTimestamp: str, pPressureInhPa: float, pTempInC: float, pHumidityInPerc: float, pMagnetFieldXInGauss: float, pMagnetFieldYInGauss: float, pMagnetFieldZInGauss: float, pGyroscopeXInRadPS: float, pGyroscopeYInRadPS: float, pGyroscopeZInRadPS: float, pAccellerationXInMS2: float, pAccellerationYInMS2: float, pAccellerationZInMS2: float):
        self.setId(pId)
        self.setTimestamp(pTimestamp)
        self.setPressureInhPa(pPressureInhPa)
        self.setTempInC(pTempInC)
        self.setHumidityInPerc(pHumidityInPerc)
        self.setMagnetFieldXInGauss(pMagnetFieldXInGauss)
        self.setMagnetFieldYInGauss(pMagnetFieldYInGauss)
        self.setMagnetFieldZInGauss(pMagnetFieldZInGauss)
        self.setGyroscopeXInRadPS(pGyroscopeXInRadPS)
        self.setGyroscopeYInRadPS(pGyroscopeYInRadPS)
        self.setGyroscopeZInRadPS(pGyroscopeZInRadPS)
        self.setAccellerationXInMS2(pAccellerationZInMS2)
        self.setAccellerationYInMS2(pAccellerationYInMS2)
        self.setAccellerationZInMS2(pAccellerationXInMS2)

    def getId(self) -> int:
        return self.id

    def setId(self, pId: int):
        self.id: int = pId

    def getTimestamp(self) -> str:
        return self.timestamp

    def setTimestamp(self, pTimestamp: str):
        self.timestamp: str = pTimestamp

    def getPressureInhPa(self) -> float:
        return self.pressureInhPa

    def setPressureInhPa(self, pPressureInhPa: float):
        self.pressureInhPa: float = pPressureInhPa

    def getTempInC(self) -> float:
        return self.tempInC

    def setTempInC(self, pTempInC: float):
        self.tempInC: float = pTempInC

    def getHumidityInPerc(self) -> float:
        return self.humidityInPerc

    def setHumidityInPerc(self, pHumidityInPerc: float):
        self.humidityInPerc: float = pHumidityInPerc

    def getMagnetFieldXInGauss(self) -> float:
        return self.magnetFieldXInGauss

    def setMagnetFieldXInGauss(self, pMagnetFieldXInGauss: float):
        self.magnetFieldXInGauss: float = pMagnetFieldXInGauss

    def getMagnetFieldYInGauss(self) -> float:
        return self.magnetFieldYInGauss

    def setMagnetFieldYInGauss(self, pMagnetFieldYInGauss: float):
        self.magnetFieldYInGauss: float = pMagnetFieldYInGauss

    def getMagnetFieldZInGauss(self) -> float:
        return self.magnetFieldZInGauss

    def setMagnetFieldZInGauss(self, pMagnetFieldZInGauss: float):
        self.magnetFieldZInGauss: float = pMagnetFieldZInGauss

    def getGyroscopeXInRadPS(self) -> float:
        return self.gyroscopeXInRadPS

    def setGyroscopeXInRadPS(self, pGyroscopeXInRadPS: float):
        self.gyroscopeXInRadPS: float = pGyroscopeXInRadPS

    def getGyroscopeYInRadPS(self) -> float:
        return self.gyroscopeYInRadPS

    def setGyroscopeYInRadPS(self, pGyroscopeYInRadPS: float):
        self.gyroscopeYInRadPS: float = pGyroscopeYInRadPS

    def getGyroscopeZInDPS(self) -> float:
        return self.gyroscopeZInDPS

    def setGyroscopeZInRadPS(self, pGyroscopeZInRadPS: float):
        self.gyroscopeZInRadPS: float = pGyroscopeZInRadPS

    def getAccellerationXInMS2(self) -> float:
        return self.accellerationXInMS2

    def setAccellerationXInMS2(self, pAccellerationXInMS2: float):
        self.accellerationXInMS2: float = pAccellerationXInMS2

    def getAccellerationYInMS2(self) -> float:
        return self.accellerationYInMS2

    def setAccellerationYInMS2(self, pAccellerationYInMS2: float):
        self.accellerationYInMS2: float = pAccellerationYInMS2

    def getAccellerationZInMS2(self) -> float:
        return self.accellerationZInMS2

    def setAccellerationZInMS2(self, pAccellerationZInMS2: float):
        self.accellerationZInMS2: float = pAccellerationZInMS2

    def toString(self) -> str:
        return (self.timestamp + "#" + str(self.id) + "#" +
                str(self.pressureInhPa) + "#" + str(self.tempInC) + "#"+ str(self.humidityInPerc) + "#" +
                str(self.magnetFieldXInGauss) + "#" + str(self.magnetFieldYInGauss) + "#" + str(self.magnetFieldZInGauss) + "#" +
                str(self.gyroscopeXInRadPS) + "#" + str(self.gyroscopeYInRadPS) + "#" + str(self.gyroscopeZInRadPS) + "#" +
                str(self.accellerationXInMS2) + "#" + str(self.accellerationYInMS2) + "#" + str(self.accellerationZInMS2))
    def toRemote(self) -> str:
        return ("mess#"+str(self.tempInC)+"#"+str(self.pressureInhPa)+"#"+str(self.humidityInPerc)+"#"+"dist")
