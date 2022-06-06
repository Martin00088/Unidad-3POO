from Manejador import Manejador


class Menu:
    __instanciaManejador=None

    def __init__(self):
        self.__instanciaManejador = Manejador()
        self.__instanciaManejador.CargaJson()
        self.__instanciaManejador.CargaLista()

    def op(self):
        self.__instanciaManejador.opgenerales()

    def tesorero(self):
        self.__instanciaManejador.opTesorero()

    def director(self):
        self.__instanciaManejador.opDirector()
