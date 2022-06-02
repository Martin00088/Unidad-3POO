from Aparato import Aparato


class Lavarropa(Aparato):
    __Caplavado=None
    __Vcentrifuga=None
    __CantProg=None
    __TipCarga=None

    def __init__(self,marca,modelo,color,paisFabricacion,PrecioBase,Caplavado,Vcentrifuga,CantPrograma,TipCarga):
        self.__Caplavado=Caplavado
        self.__Vcentrifuga=Vcentrifuga
        self.__CantProg=CantPrograma
        self.__TipCarga=TipCarga
        super().__init__(marca,modelo,color,paisFabricacion,PrecioBase)

    def __str__(self):
        cadena = super().__str__()
        cadena += " Capacidad de lavado:{} Velocidad Centrifugado:{} Cantidad de Programas:{} Tipo de Carga:{}\n----".format(self.__Caplavado,self.__Vcentrifuga,self.__CantProg,self.__TipCarga)
        return cadena

    def getimporte(self):
        importe = self.getpreciobase()
        if self.__Caplavado <= 5:
            importe += (self.getpreciobase()*1)/100
        elif self.__Caplavado > 5:
            importe += (self.getpreciobase()*3)/100
        return importe

    def getClavado(self):
        return self.__Caplavado

    def getVcentrifuga(self):
        return self.__Vcentrifuga

    def getCantProg(self):
        return self.__CantProg

    def getTcarga(self):
        return self.__TipCarga

    def toJSON(self):
        d = super().toJSON()["__atributos__"]
        d.update(dict(
                Caplavado=self.__Caplavado,
                Vcentrifuga=self.__Vcentrifuga,
                CantPrograma=self.__CantProg,
                TipCarga=self.__TipCarga
            ))
        dH = dict(
                __class__=self.__class__.__name__,
                atributos=d
            )
        return dH
