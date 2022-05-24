import numpy as np
from Calefactor import Calefactor
from CalefactorGas import CalefactorGas
from CalefactorElectrico import CalefactorElectrico
import csv


class ManejadorCalefactor:
    __array = None
    __dimension = None

    def __init__(self):
        self.__array = np.empty(0, dtype=Calefactor)

    def agregarCalefactor(self, calefactor):
        self.__array = np.append(self.__array, calefactor)

    def CargaCG(self):
        archivo = open("calefactor-a-gas.csv")
        reader = csv.reader(archivo, delimiter=";")
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                calefactor = CalefactorGas(fila[0], fila[1], fila[2], fila[3])
                self.agregarCalefactor(calefactor)

    def CargaCE(self):
        archivo = open("calefactor-electrico.csv")
        reader = csv.reader(archivo, delimiter=";")
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                calefactor = CalefactorElectrico(fila[0], fila[1], fila[2])
                self.agregarCalefactor(calefactor)

    def getArray(self):
        return self.__array

    def mostrar(self):
        for i in range(len(self.__array)):
            print(self.__array[i])

    def item1y2(self, costo, cantidad):
        minimo = -1
        pos = -1
        for i in range(len(self.__array)):
            if type(self.__array[i]) is CalefactorElectrico:
                gasto = (float(self.__array[i].getPmaxima())/1000) * cantidad * costo
                if gasto < minimo:
                    minimo = gasto
                    pos = i
            else:
                gasto = (float(self.__array[i].getcaloria())/1000) * cantidad * costo
                if gasto < minimo:
                    minimo = gasto
                    pos = i
        return pos

    def mostraritems(self,posmin):
        print(self.__array[posmin])

    def mostrartipo(self,posmin):
        retorna = None
        if type(self.__array[posmin]) is CalefactorElectrico:
            retorna = "Calefactor Electrico"
        else:
            retorna = "Calefactor a Gas"
        return retorna

    def getposarr(self, pos):
        return self.__array[pos]

