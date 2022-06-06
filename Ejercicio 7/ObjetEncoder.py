from pathlib import Path
import json
from Docente import Docente
from Investigador import Investigador
from DocenteInvestigador import DocenteInvestigador
from Personal import Personal


class ObjectEncoder(object):

    def decodificarDiccionario(self, lista):
        d = self.leerJSONArchivo("personal.json")
        for elem in d:
            if '__class__' not in elem:
                print("No se encuentra en la clase")
            else:
                nombreclase = elem['__class__']
                class_ = eval(nombreclase)
                if nombreclase == "Docente":
                    atributos = elem["__atributos__"]
                    D = class_(**atributos)
                    lista.agregarPersonal(D)
                elif nombreclase == "Investigador":
                    atributos = elem["__atributos__"]
                    I = class_(**atributos)
                    lista.agregarPersonal(I)
                elif nombreclase == "DocenteInvestigador":
                    atributos = elem["__atributos__"]
                    DI = class_(**atributos)
                    lista.agregarPersonal(DI)
                else:
                    print("No se puede agregar")

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
