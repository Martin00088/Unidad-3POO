from Calefactor import Calefactor


class CalefactorGas(Calefactor):
    __matricula = None
    __calorias = None

    def __init__(self, marca, modelo, matr, cal):
        self.__calorias = cal
        self.__matricula = matr
        super().__init__(marca, modelo)

    def __str__(self):
        return "Marca={} , Modelo={}, Matricula={}, Calorias={}".format(self.getmarca(), self.getmodelo(),self.__matricula,self.__calorias)

    def getcaloria(self):
        return self.__calorias

    def getmatricula(self):
        return self.__matricula
