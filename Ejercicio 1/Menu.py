from Manejador import Manejador


class Menu:
    __opcion=None

    def __init__(self, op):
        self.__opcion = op

    def menuop(self):
        if self.__opcion == 1:
            i = Manejador()
            i.CargaF()
            i.ListadoCod()
        elif self.__opcion == 2:
            i = Manejador()
            i.CargaF()
            i.ListadoCa()
        else:
            print("La opcion ingresada no existe")
