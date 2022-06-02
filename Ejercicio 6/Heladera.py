from Aparato import Aparato


class Heladera(Aparato):
    __Clitros=None
    __Frezzer=None
    __ciclica=None

    def __init__(self, marca, modelo, color, paisFabricacion, PrecioBase, clitros, frezzer, ciclica):
        self.__Clitros=clitros
        self.__Frezzer=frezzer
        self.__ciclica=ciclica
        super().__init__(marca,modelo,color,paisFabricacion,PrecioBase)

    def __str__(self):
        cadena = super().__str__()
        cadena += " Capacidad Litros:{} Frezzer:{} Ciclica:{}\n----".format(self.__Clitros,self.__Frezzer,self.__ciclica)
        return cadena
    def getclitros(self):
        return self.__Clitros

    def getfrezzer(self):
        return self.__Frezzer

    def getciclica(self):
        return self.__ciclica

    def getimporte(self):
        importe = self.getpreciobase()
        if self.__Frezzer == True:
            importe += (self.getpreciobase()* 5)/100
        elif self.__Frezzer == False :
            importe += (self.getpreciobase() * 1)/100
        if self.__ciclica == True:
            importe += (self.getpreciobase() * 10)/100
        return importe

    def toJSON(self):
        d = super().toJSON()["__atributos__"]
        d.update(dict(
                clitros=self.__Clitros,
                frezzer=self.__Frezzer,
                ciclica=self.__ciclica,
            ))
        dH = dict(
                __class__=self.__class__.__name__,
                atributos=d
            )
        return dH
