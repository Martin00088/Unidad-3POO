class Aparato:
    __marca=None
    __modelo=None
    __color=None
    __paisFabricacion=None
    __Preciobase=None

    def __init__(self, marca,modelo,color,paisFabricacion,PrecioBase):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__paisFabricacion = paisFabricacion
        self.__PrecioBase = PrecioBase

    def __str__(self):
        return "Marca:{} Modelo:{} Color:{} Pais Fabricacion:{} Precio Base:{}".format(self.__marca, self.__modelo, self.__color, self.__paisFabricacion, self.__PrecioBase)

    def getimporte(self):
        pass

    def getmarca(self):
        return self.__marca

    def getmodelo(self):
        return self.__modelo

    def getcolor(self):
        return self.__color

    def getpfabricacion(self):
        return self.__paisFabricacion

    def getpreciobase(self):
        return self.__PrecioBase

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                marca=self.__marca,
                modelo=self.__modelo,
                color=self.__color,
                paisFabricacion=self.__paisFabricacion,
                PrecioBase=self.__PrecioBase
            )
        )
        return d
