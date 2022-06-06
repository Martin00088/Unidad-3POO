from zope.interface import Interface


class Interfaz(Interface):

    def insertarElemento(self, elemento, pos):
        pass

    def agregarElemento(self, elemento):
        pass

    def mostrarElemento(self):
        pass


