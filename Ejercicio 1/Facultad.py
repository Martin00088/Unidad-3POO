class Facultad:

    __codfac=None
    __Nombre=None
    __direc=None
    __Locali=None
    __Telef=None
    __carrera=None

    def __init__(self, cod, nom, dire, loc1, loc2, tel):
        self.__codfac = cod
        self.__Nombre = nom
        self.__direc = dire
        self.__Locali = loc1 + ", " + loc2
        self.__Telef = tel
        self.__carrera = []

    def getCod(self):
        return self.__codfac

    def getNom(self):
        return self.__Nombre

    def getDirec(self):
        return self.__direc

    def getLoc(self):
        return self.__Locali

    def getTel(self):
        return self.__Telef

    def getCarreras(self):
        return self.__carrera

    def addCarreras(self, carrera):
        self.__carrera.append(carrera)

