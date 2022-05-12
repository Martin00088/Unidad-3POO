class Carrera:
    __codigo = None
    __Nombre = None
    __Fecha_ini = None
    __Duracion = None
    __titulo = None

    def __init__(self,cod=None,nombre=None,fech=None , dur=None , tit=None):
        self.__codigo = cod
        self.__Nombre = nombre
        self.__Fecha_ini = fech
        self.__Duracion = dur
        self.__titulo = tit

    def getCod(self):
        return self.__codigo

    def getNombre(self):
        return self.__Nombre

    def getFechaI(self):
        return self.__Fecha_ini

    def getDur(self):
        return self.__Duracion

    def getTit(self):
        return self.__titulo
