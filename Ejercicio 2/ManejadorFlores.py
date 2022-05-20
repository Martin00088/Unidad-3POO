from Flores import Flor
import numpy as np
import csv


class ManejadorFlores:
    __array = []
    __incremento = None
    __dimension = None
    __cantidad = None

    def __init__(self, dimension=1, incremento=5):
        self.__array = np.empty(dimension, dtype=Flor)
        self.__dimension = dimension
        self.__incremento = incremento
        self.__cantidad = 0

    def agregaflor(self, flor):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__array.resize(self.__dimension)
        self.__array[self.__cantidad] = flor
        self.__cantidad += 1

    def CargaF(self):
        archivo = open("Flores.csv")
        reader = csv.reader(archivo, delimiter=",")
        for fila in reader:
            numero = fila[0]
            nombre = fila[1]
            color = fila[2]
            descripc = fila[3]
            flor = Flor(numero, nombre, color, descripc)
            self.agregaflor(flor)

    def mostrar(self):
        for i in range(len(self.__array)):
            print(self.__array[i])

    def getFlor(self, numero):
        return self.__array[numero-1]

    def getflores(self):
        return self.__array
