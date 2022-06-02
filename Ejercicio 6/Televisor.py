from Aparato import Aparato


class Televisor(Aparato):
    __Tpantalla=None
    __pulgada=None
    __Tdefinicion=None
    __Cinternet=None

    def __init__(self,marca,modelo,color,paisFabricacion,PrecioBase,Tpantalla,pulgada,Tdefinicion,Cinternet):
        self.__Tpantalla=Tpantalla
        self.__pulgada=pulgada
        self.__Tdefinicion=Tdefinicion
        self.__Cinternet=Cinternet
        super().__init__(marca,modelo,color,paisFabricacion,PrecioBase)

    def __str__(self):
        cadena = super().__str__()
        cadena += " Tipo Pantalla:{} Pulgadas:{} Tipo Definicion:{} Conexion a Internet:{}\n----".format(self.__Tpantalla,self.__pulgada,self.__Tdefinicion,self.__Cinternet)
        return cadena

    def getimporte(self):
        importe = self.getpreciobase()
        if self.__Tdefinicion == "SD":
            importe += (self.getpreciobase()*1)/100
        elif self.__Tdefinicion == "HD":
            importe += (self.getpreciobase()*2)/100
        elif self.__Tdefinicion == "FULL HD":
            importe += (self.getpreciobase()*3)/100
        if self.__Cinternet == True:
            importe += (self.getpreciobase()*10)/100
        return importe

    def gettpantalla(self):
        return self.__Tpantalla

    def getpulgada(self):
        return self.__pulgada

    def gettdefinicion(self):
        return self.__Tdefinicion

    def getcinternet(self):
        return self.__Cinternet

    def toJSON(self):
        d = super().toJSON()["__atributos__"]
        d.update(dict(
                Tpantalla=self.__Tpantalla,
                pulgada=self.__pulgada,
                Tdefinicion=self.__Tdefinicion,
                Cinternet=self.__Cinternet
            ))
        dH = dict(
                __class__=self.__class__.__name__,
                atributos=d
            )
        return dH
