from Nodo import Nodo
from Televisor import Televisor
from Heladera import Heladera
from Lavarropa import Lavarropa

class Lista:
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0

    def __init__(self):
        self.__comienzo = None
        self.__actual = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
        return dato

    def agregarAparato(self, aparato):
        nodo = Nodo(aparato)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo

    def listarAparato(self):
        aux = self.__comienzo
        while aux != None:
            print(aux.getDato())
            aux = aux.getSiguiente()

    def listarposAparato(self, pos):
        cont = 0
        aux = self.__comienzo
        while aux != None and cont != pos:
            cont += 1
            aux = aux.getSiguiente()
        if cont == pos:
            print(aux.getDato())
        else:
            print("La posicion ingresada no esta cargada")

    def insertaraparato(self, aparato, pos):
        aux = self.__comienzo
        cont = 0
        if pos == 0 :
            nuevonodo = Nodo(aparato)
            nuevonodo.setSiguiente(aux)
            self.__comienzo = nuevonodo
        else:
            while aux != None and (pos-1) != cont:
                aux = aux.getSiguiente()
                cont += 1
            if (pos-1) == cont:
                nuevonodo = Nodo(aparato)
                nuevonodo.setSiguiente(aux.getSiguiente())
                aux.setSiguiente(nuevonodo)
            else:
                print("No se puede insertar en esa posicion")

    def listarPhilips(self):
        aux = self.__comienzo
        contH=0
        contT=0
        contL=0
        while aux != None:
            if aux.getDato().getmarca() == "Philips" and isinstance(aux.getDato(), Heladera):
                contH += 1
            elif aux.getDato().getmarca() == "Philips" and isinstance(aux.getDato(), Televisor):
                contT += 1
            elif aux.getDato().getmarca() == "Philips" and isinstance(aux.getDato(), Lavarropa):
                contL += 1
            aux = aux.getSiguiente()
        print("Hay {} Heladeras, {} Televisores , {} Lavarropas  de marca Philips".format(contH,contT,contL))

    def cargasup(self):
        aux = self.__comienzo
        while aux != None:
            if (isinstance(aux.getDato(), Lavarropa)) and aux.getDato().getTcarga() == "superior":
                print(aux.getDato().getmarca())
            aux = aux.getSiguiente()

    def infoempresa(self):
        aux = self.__comienzo
        while aux != None:
            print("Marca:{}, Pais de Fabricacion:{} , Importe de venta:{}\n---------".format(aux.getDato().getmarca(), aux.getDato().getpfabricacion(), aux.getDato().getimporte()))
            aux = aux.getSiguiente()

    def guardaJson(self, objectEncoder):
        lista = []
        cabeza = self.__comienzo
        while cabeza != None:
            aux = cabeza.getDato()
            dicc = aux.toJSON()
            lista.append(dicc)
            cabeza = cabeza.getSiguiente()
        objectEncoder.guardarJSONArchivo(lista, "aparatoselectronicos.json")
        print("Archivo (aparatoselectronicos.json) guardado")
