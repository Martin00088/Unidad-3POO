from Equipo import Equipo
import csv
import numpy as np


class ManejadorEquipo:
    __cantidad = 0
    __dimension = 5
    __incremento = 5
    __arrayE = None
    __jugador = None

    def __init__(self, dimension=5, incremento=5):
        self.__arrayE = np.empty(dimension, dtype=Equipo)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento

    def agregarEquipo(self, equipo):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arrayE.resize(self.__dimension)
        self.__arrayE[self.__cantidad] = equipo
        self.__cantidad += 1

    def CargaEquipo(self):
        archivo = open("Equipo.csv")
        reader = csv.reader(archivo, delimiter=";")
        bandera=True
        for fila in reader:
            if bandera:
                 bandera = not bandera
            else:
                equipo = Equipo(str(fila[0]), str(fila[1]))
                self.agregarEquipo(equipo)
        archivo.close()

    def getarrayE(self):
        return self.__arrayE

    def getposarrayE(self, pos):
        return self.__arrayE[pos]

    def getnombreE(self, pos):
        return self.__arrayE[pos].getnombre()
