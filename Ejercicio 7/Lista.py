from Nodo import Nodo
from Docente import Docente
from Investigador import Investigador
from DocenteInvestigador import DocenteInvestigador
from PersonalApoyo import PersonalApoyo
from Personal import Personal

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

    def agregarPersonal(self, personal):
        nodo = Nodo(personal)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo

    def listarAparato(self):
        aux = self.__comienzo
        while aux != None:
            print(aux.getDato())
            aux = aux.getSiguiente()

    def listarposPersonal(self, pos):
        cont = 0
        aux = self.__comienzo
        while aux != None and cont != pos:
            cont += 1
            aux = aux.getSiguiente()
        if cont == pos:
            print(aux.getDato())
        else:
            print("La posicion ingresada no esta cargada")

    def insertarPersonal(self,personal, pos):
        aux = self.__comienzo
        cont = 0
        if pos == 0:
            nuevonodo = Nodo(personal)
            nuevonodo.setSiguiente(aux)
            self.__comienzo = nuevonodo
        else:
            while aux != None and (pos-1) != cont:
                aux = aux.getSiguiente()
                cont += 1
            if (pos-1) == cont:
                nuevonodo = Nodo(personal)
                nuevonodo.setSiguiente(aux.getSiguiente())
                aux.setSiguiente(nuevonodo)
            else:
                print("No se puede insertar en esa posicion")

    def guardaJson(self, objectEncoder):
        lista = []
        cabeza = self.__comienzo
        while cabeza != None:
            aux = cabeza.getDato()
            dicc = aux.toJSON()
            lista.append(dicc)
            cabeza = cabeza.getSiguiente()
        objectEncoder.guardarJSONArchivo(lista, "PersonalNuevo.json")
        print("Archivo (PersonalNuevo.json) guardado")

    def mostrarlista(self):
        aux = self.__comienzo
        while aux is not None:
            print(aux.getDato())
            aux = aux.getSiguiente()

    def mostrarposlista(self, pos):
        cont = 0
        aux = self.__comienzo
        while aux is not None and cont != pos:
            cont += 1
            aux = aux.getSiguiente()
        if cont == pos:
            print(aux.getDato())
        else:
            print("La posicion ingresada no esta cargada")

    def listadoordenado(self, carrera):
        aux = self.__comienzo
        listadi = []
        while aux is not None:
            if isinstance(aux.getDato(), DocenteInvestigador) and carrera == aux.getDato().getcarrera():
                listadi.append(aux.getDato())
            aux = aux.getSiguiente()
        longitud = len(listadi)
        for i in range(longitud):
            for j in range(longitud - 1):
                k = j + 1
                if listadi[j] > listadi[k]:
                    listadi[k], listadi[j] = listadi[j], listadi[k]
        for j in range(longitud):
            print(listadi[j])

    def contarAgentes(self, areaI):
        contDI = 0
        contI = 0
        aux = self.__comienzo
        while aux is not None:
            if isinstance(aux.getDato(), DocenteInvestigador) and areaI == aux.getDato().getainvestigacion():
                contDI += 1
            elif isinstance(aux.getDato(), Investigador) and areaI == aux.getDato().getainvestigacion():
                contI += 1
            aux = aux.getSiguiente()
        print("La cantidad de Agentes DocentesInvestigadores son {}".format(contDI))
        print("La cantidad de Agentes Investigadores son {}".format(contI))

    def mostrarOrdenado(self):
        aux = self.__comienzo
        listadi = []
        while aux is not None:
            listadi.append(aux.getDato())
            aux = aux.getSiguiente()

        longitud = len(listadi)
        for i in range(longitud):
            for j in range(longitud - 1):
                k = j + 1
                if listadi[k] < listadi[j]:
                    listadi[k], listadi[j] = listadi[j], listadi[k]

        for i in range(longitud):
            if isinstance(listadi[i], DocenteInvestigador):
                print("Nombre:{},Apellido:{} Tipo de Agente:Docente Investigador Sueldo:{}".format(listadi[i].getnombre(), listadi[i].getapellido(), listadi[i].getsueldoDocInv()))
            elif isinstance(listadi[i], Docente):
                print("Nombre:{}, Apellido:{} Tipo de Agente:Docente, Sueldo:{}".format(listadi[i].getnombre(), listadi[i].getapellido(), listadi[i].getsueldoDocente()))
            elif isinstance(listadi[i], Investigador):
                print("Nombre:{}, Apellido:{}, Tipo de Agente:Investigador, Sueldo:{}".format(listadi[i].getnombre(), listadi[i].getapellido(),listadi[i].sueldoInvestigador()))
            elif isinstance(listadi[i], PersonalApoyo):
                print("Nombre:{} Apellido:{} Tipo de Agente:Personal de Apoyo ,Sueldo:{}".format(listadi[i].getnombre(), listadi[i].getapellido(), listadi[i].sueldoPerApoyo()))

    def mostrarcat(self, categoria):
        aux = self.__comienzo
        total = 0
        while aux is not None:
            if isinstance(aux.getDato(), DocenteInvestigador) and aux.getDato().getcatincentivos() == categoria:
                print("Apellido:{} Nombre:{} ImporteExtra:{}".format(aux.getDato().getapellido(), aux.getDato().getnombre(), aux.getDato().getimpextra()))
                total += aux.getDato().getimpextra()
            aux = aux.getSiguiente()
        print("Total de dinero a solicitar es:{} $".format(total))

    def guardaJson(self, objectEncoder):
        lista = []
        cabeza = self.__comienzo
        while cabeza is not None:
            aux = cabeza.getDato()
            dicc = aux.toJSON()
            lista.append(dicc)
            cabeza = cabeza.getSiguiente()
        objectEncoder.guardarJSONArchivo(lista, "NUEVOpersonal.json")
        print("Archivo (NUEVOpersonal.json) guardado")
