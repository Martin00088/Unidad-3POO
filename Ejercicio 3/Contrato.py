class Contrato:
    __Finicio = None
    __Ffin = None
    __Pmensual = None
    __equipo = None
    __jugador = None

    def __init__(self, ini, fin, mes, jugador=None, equipo=None):
        self.__Finicio = ini
        self.__Ffin = fin
        self.__Pmensual = mes
        self.__equipo = equipo
        self.__jugador = jugador

    def __str__(self):
        return "Fecha Inicio:{} Fecha Fin:{} Pago Mensual:{} Equipo:{} Jugador:{}".format(self.__Finicio, self.__Ffin, self.getffin(), self.__equipo, self.__jugador)

    def getfinicio(self):
        return self.__Finicio

    def getffin(self):
        return self.__Ffin

    def getpmensual(self):
        return self.__Pmensual

    def getequipoC(self):
        return self.__equipo

    def setequipoC(self, equipo):
        self.__equipo = equipo

    def setjugadorC(self, jugador):
        self.__jugador = jugador

    def getjugadorE(self):
        return self.__jugador
