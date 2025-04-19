class Measurement:

    def __init__(self, pId: int, pTimestamp: str, pPressureInhPa: float, pTempInC: float, pMagnetFieldInGauss: float, pGyroscopeInDPS: float, pAccellerationInG: float):
        self.setId(pId)
        self.setTimestamp(pTimestamp)
        self.setPressureInhPa(pPressureInhPa)
        self.setTempInC(pTempInC)
        self.setMagnetFieldInGauss(pMagnetFieldInGauss)
        self.setGyroscopeInDPS(pGyroscopeInDPS)
        self.setAccellerationInG(pAccellerationInG)

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

    def getMagnetFieldInGauss(self) -> float:
        return self.magnetFieldInGauss

    def setMagnetFieldInGauss(self, pMagnetFieldInGauss: float):
        self.magnetFieldInGauss: float = pMagnetFieldInGauss

    def getGyroscopeInDPS(self) -> float:
        return self.gyroscopeInDPS

    def setGyroscopeInDPS(self, pGyroscopeInDPS: float):
        self.gyroscopeInDPS: float = pGyroscopeInDPS

    def getAccellerationInG(self) -> float:
        return self.accellerationInG

    def setAccellerationInG(self, pAccellerationInG: float):
        self.accellerationInG: float = pAccellerationInG

    def toString(self) -> str:
        return (self.timestamp + "#" + str(self.id) + "#" +
                str(self.pressureInhPa) + "#" + str(self.tempInC) + "#" +
                str(self.magnetFieldInGauss) + "#" + str(self.gyroscopeInDPS) + "#" +
                str(self.accellerationInG))
