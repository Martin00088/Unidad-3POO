class Jugador:
    __nombre = None
    __dni = None
    __Cnatal = None
    __Porigen = None
    __Fnaci = None
    __equipo = None

    def __init__(self, dni, nom , cna, pori, fnac):
        self.__nombre = nom
        self.__dni = dni
        self.__Cnatal = cna
        self.__Porigen = pori
        self.__Fnaci = fnac

    def __str__(self):
        return "Nombre:{} DNI:{} Ciudad Natal:{} Pais Origen:{} Fecha Nacimiento:{}".format(self.__nombre,self.__dni,self.__Cnatal,self.__Porigen,self.__Fnaci)

    def getnombre(self):
        return self.__nombre

    def getdni(self):
        return self.__dni

    def getcnatal(self):
        return self.__Cnatal

    def getporigen(self):
        return self.__Porigen

    def getfnacimiento(self):
        return self.__Fnaci

