from Facultad import Facultad
from Carrera import Carrera
import csv


class Manejador:
    __facultades=[]

    def __init__(self):
        self.__facultades = []

    def CargaF(self):
        archivo = open("Facultades.csv")
        reader = csv.reader(archivo, delimiter=",")
        cod = -1
        for fila in reader:
            if int(fila[0]) == cod:
                carr = Carrera(fila[1], fila[2], fila[3], fila[4], fila[5])
                self.__facultades[cod-1].addCarreras(carr)
            else:
                cod = int(fila[0])
                facu = Facultad(cod, fila[1], fila[2], fila[3], fila[4], fila[5])
                self.__facultades.append(facu)
        archivo.close()

    def ListadoCod(self):
        cod = int(input("Ingresar el codigo de facultad:"))
        i = 0
        while i < len(self.__facultades) and cod != self.__facultades[i].getCod():
            i += 1
        if i < len(self.__facultades):
            print("Nombre Facultad:{}".format(self.__facultades[i].getNom()))
            carrera = self.__facultades[i].getCarreras()
            for j in range(len(carrera)):
                print("Nombre de Carrera : {}, Duracion : {}".format(carrera[j].getNombre(), carrera[j].getDur()))
        else:
            print("El codigo de facultad ingresado no existe")

    def ListadoCa(self):
        nom = input("Ingrese el nombre de una carrera:")
        i = 0
        j = 0
        while i < len(self.__facultades):
            carreras = self.__facultades[i].getCarreras()
            while j < len(carreras) and nom != carreras[j].getNombre():
                j += 1
            if j < len(carreras) and i < len(self.__facultades):
                print("Codigo de facultad:{}\nCodigo Carrera:{}\nNombre Facultad:{}\nLocalidad:{}".format(self.__facultades[i].getCod(), j+1, self.__facultades[i].getNom(), self.__facultades[i].getLoc()))
            j = 0
            i += 1
        if i >= len(self.__facultades):
            print("El nombre de carrera ingresado no existe")
