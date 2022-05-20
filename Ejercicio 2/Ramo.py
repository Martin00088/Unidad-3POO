class Ramo:
    __tamano=None

    def __init__(self, tam):
        self.__tamano = tam
        self.__flores = []

    def __str__(self):
        retorno= "Tamaño:{}\n".format(self.__tamano)
        for i in range(len(self.__flores)):
            retorno += "Flor:{}".format(self.__flores[i])
        return retorno

    def getTam(self):
        return self.__tamano

    def addFlor(self, flor):
        self.__flores.append(flor)

    def getFlores(self):
        return self.__flores

    def getFlorlis(self, numero):
        return self.__flores[numero]

    def contadorflor(self, numero):
        cont = 0
        for i in range(len(self.__flores)):
            if self.__flores[i].getNum() == numero:
                cont += 1
        return cont
