from Contrato import Contrato
import numpy as np


class ManejadorContrato:
    __cantidad = 0
    __dimension = 5
    __incremento = 5
    __arrayC = None

    def __init__(self, dimension=1, incremento=5):
        self.__arrayC = np.empty(dimension, dtype=Contrato)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento

    def agregarContrato(self, contrato):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arrayC.resize(self.__dimension)
        self.__arrayC[self.__cantidad] = contrato
        self.__cantidad += 1

    def mostrarcontrato(self):
        for i in range(self.__cantidad):
            print(self.__arrayC[i])

    def CargaContrato(self, arrayE, listaJ):
        for i in range(len(listaJ)):
            Finicio = input("Ingrese una fecha de inicio de contrato para el jugador {}".format(listaJ[i].getnombre()))
            Ffin = input("Ingrese una fecha de finalizacion de contrato para el jugador {}".format(listaJ[i].getnombre()))
            Pago = float(input("Ingrese pago mensual para el jugador".format(listaJ[i].getnombre())))
            equipo = input("Ingrese el equipo en el que va estar ")
            j = 0
            while j < len(arrayE) and equipo != arrayE[j].getnombre():
                j += 1
            if j < len(arrayE):
                contrato = Contrato(Finicio, Ffin, Pago)
                contrato.setequipoC(arrayE[j])
                contrato.setjugadorC(listaJ[i])
                self.agregarContrato(contrato)
                print("-------------")
            else:
                contrato = Contrato(Finicio, Ffin, Pago)
                contrato.setequipoC(None)
                contrato.setjugadorC(None)
                self.agregarContrato(contrato)
                print("El equipo ingresado no existe")
                print("-------------")

    def consJContratado(self, dni):
        i = 0
        while i < len(self.__arrayC) and (self.__arrayC[i].getjugadorE.getdni() != dni or self.__arrayC[i].getjugadorE() == None):
            i += 1
        if i < len(self.__arrayC):
            if self.__arrayC[i].getjugadorE.getnombre() == None:
                print("Este jugador no esta contratado")
            else:
                print("Nombre del equipo:{} , Fecha de Finalizacion:{}".format(self.__arrayC[i].getequipoC.getnombre(), self.__arrayC[i].getequipoC.getffin()))
        else:
            print("El DNI ingresado no existe")

    def getarrayC(self):
        return self.__arrayC

    def getposarrayC(self, pos):
        return self.__arrayC[pos]
