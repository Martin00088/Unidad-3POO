from Calefactor import Calefactor


class CalefactorElectrico(Calefactor):
    __Pmaxima = None

    def __init__(self, marca, modelo,pmax):
        self.__Pmaxima = pmax
        super().__init__(marca, modelo)

    def __str__(self):
        return "Marca={} ,Modelo={}, Potencia Maxima={}".format(self.getmarca(),self.getmodelo(),self.__Pmaxima)

    def getPmaxima(self):
        return self.__Pmaxima


