from pathlib import Path
import json
from Heladera import Heladera
from Lavarropa import Lavarropa
from Televisor import Televisor



class ObjectEncoder(object):

    def decodificarDiccionario(self, lista):
        d = self.leerJSONArchivo("Aparatos.json")
        for elem in d:
            if '__class__' not in elem:
                print("No se encuentra en la clase")
            else:
                nombreclase = elem['__class__']
                class_ = eval(nombreclase)
                if nombreclase == "Heladera":
                    atributos = elem["atributos"]
                    H = class_(**atributos)
                    lista.agregarAparato(H)
                elif nombreclase == "Televisor":
                    atributos = elem["atributos"]
                    T = class_(**atributos)
                    lista.agregarAparato(T)
                else:
                    atributos = elem["atributos"]
                    L = class_(**atributos)
                    lista.agregarAparato(L)

    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()

    def leerJSONArchivo(self, archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario = json.load(fuente)
            fuente.close()
        return diccionario

    def convertirADiccionario(self, elem):
        return json.loads(elem.toJSON())
