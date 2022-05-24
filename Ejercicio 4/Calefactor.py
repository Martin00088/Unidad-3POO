class Calefactor:
    __marca = None
    __modelo = None

    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    def getmarca(self):
        return self.__marca

    def getmodelo(self):
        return self.__modelo

