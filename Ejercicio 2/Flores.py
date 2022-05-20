class Flor:
    __numero=None
    __nombre=None
    __color=None
    __descripcion=None

    def __init__(self,num=None,nom=None,col=None,des=None):
        self.__numero = num
        self.__nombre = nom
        self.__color = col
        self.__descripcion = des
        self.__cantidad=None

    def __str__(self):
        return "Numero:{} Nombre:{} Color:{} Descripcion:{}\n".format(self.__numero,self.__nombre,self.__color,self.__descripcion)

    def getNum(self):
        return self.__numero

    def getnombre(self):
        return self.__nombre

    def getCol(self):
        return self.__color

    def getDes(self):
        return self.__descripcion

    def modificarcant(self, cont):
        self.__cantidad = cont

    def getcantidad(self):
        return self.__cantidad
