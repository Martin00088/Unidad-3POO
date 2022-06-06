from Docente import Docente
from Investigador import Investigador
from DocenteInvestigador import DocenteInvestigador
from ObjetEncoder import ObjectEncoder
from Interfaz import Interface
from zope.interface import implementer
from Lista import Lista


@implementer(Interface)
class Manejador:
    __lista = None

    def __init__(self):
        self.__lista = Lista()

    def CargaJson(self):
        objeto1 = Docente(cuil="43344334",apellido="Gonzalez",nombre="Martin",sueldobasico=20000,antiguedad=10,carrera="LCC",cargo="Suplente",catedra="POO")
        objeto2 = Investigador(cuil="45343543", apellido="Laciar", nombre="Joaquin", sueldobasico=30000, antiguedad=20, areainvestigacion="Informatica", tipinvestigacion="Robotica")
        objeto3 = DocenteInvestigador(cuil="4344343", apellido="Fuentes", nombre="Jazmin", sueldobasico=40000, antiguedad=4,carrera="LCC", cargo="semiexclusivo", catedra="POO", areainvestigacion="Informatica", tipinvestigacion="Robotica", cantincentivos="I", importextra=5000)
        objeto4 = DocenteInvestigador(cuil="4344343", apellido="Fuentes", nombre="Aguero", sueldobasico=40000, antiguedad=4,carrera="LCC", cargo="simple", catedra="POO", areainvestigacion="Informatica", tipinvestigacion="Robotica", cantincentivos="I", importextra=5000)
        jsonF = ObjectEncoder()
        d = objeto1.toJSON()
        d1 = objeto2.toJSON()
        d2 = objeto3.toJSON()
        d3 = objeto4.toJSON()
        lista = [d, d1, d2, d3]
        jsonF.guardarJSONArchivo(lista, "personal.json")

    def CargaLista(self):
        jsonF = ObjectEncoder()
        jsonF.decodificarDiccionario(self.__lista)

    def MostrarLista(self):
        self.__lista.mostrarlista()

    def InsertarLista(self, pos):
        tipo=input("Ingrese el tipo de personal(Docente/Investigador/DocenteInvestigador):")
        if tipo =="Docente":
            personal=Docente(cuil=input("ingrese el Cuil:"),apellido=input("Ingrese el Apellido:"),nombre=input("Ingrese el Nombre:"),sueldobasico=float(input("Ingrese el Sueldo Basico:")),antiguedad=input("Ingrese la Antiguedad:"),carrera=input("Ingrese Carrera:"),cargo=input("Ingrese el cargo:"),catedra=input("Ingrese catedra:"))
            self.__lista.insertarPersonal(personal, pos)
        elif tipo == "Investigador":
            personal=Investigador(cuil=input("ingrese el Cuil:"),apellido=input("Ingrese el Apellido:"),nombre=input("Ingrese el Nombre:"),sueldobasico=float(input("Ingrese el Sueldo Basico:")),antiguedad=input("Ingrese la Antiguedad:"),areainvestigacion=input("Ingrese el area de Investigacion:"),tipinvestigacion=input("Ingrese el tipo de Investigador"))
            self.__lista.insertarPersonal(personal, pos)
        elif tipo == "DocenteInvestigador":
            personal = DocenteInvestigador(cuil=input("ingrese el Cuil:"),apellido=input("Ingrese el Apellido:"),nombre=input("Ingrese el Nombre:"),sueldobasico=float(input("Ingrese el Sueldo Basico:")),antiguedad=input("Ingrese la Antiguedad:"),carrera=input("Ingrese Carrera:"),cargo=input("Ingrese el cargo:"),catedra=input("Ingrese catedra:"),areainvestigacion=input("Ingrese el area de Investigacion:"),tipinvestigacion=input("Ingrese el tipo de Investigador"),cantincentivos=input("Ingrese la cantidad de inscentivos:"), importextra=input("Ingrese el importe extra:"))
            self.__lista.insertarPersonal(personal, pos)

    def AgregarLista(self):
        tipo=input("Ingrese el tipo de personal(Docente/Investigador/DocenteInvestigador):")
        if tipo =="Docente":
            personal=Docente(cuil=input("ingrese el Cuil:"), apellido=input("Ingrese el Apellido:"),nombre=input("Ingrese el Nombre:"),sueldobasico=float(input("Ingrese el Sueldo Basico:")),antiguedad=input("Ingrese la Antiguedad:"),carrera=input("Ingrese Carrera:"),cargo=input("Ingrese el cargo:"),catedra=input("Ingrese catedra:"))
            self.__lista.agregarPersonal(personal)
        elif tipo == "Investigador":
            personal=Investigador(cuil=input("ingrese el Cuil:"), apellido=input("Ingrese el Apellido:"),nombre=input("Ingrese el Nombre:"),sueldobasico=float(input("Ingrese el Sueldo Basico:")),antiguedad=input("Ingrese la Antiguedad:"),areainvestigacion=input("Ingrese el area de Investigacion:"),tipinvestigacion=input("Ingrese el tipo de Investigador"))
            self.__lista.agregarPersonal(personal)
        elif tipo == "DocenteInvestigador":
            personal = DocenteInvestigador(cuil=input("ingrese el Cuil:"), apellido=input("Ingrese el Apellido:"),nombre=input("Ingrese el Nombre:"),sueldobasico=float(input("Ingrese el Sueldo Basico:")),antiguedad=input("Ingrese la Antiguedad:"),carrera=input("Ingrese Carrera:"),cargo=input("Ingrese el cargo:"),catedra=input("Ingrese catedra:"),areainvestigacion=input("Ingrese el area de Investigacion:"),tipinvestigacion=input("Ingrese el tipo de Investigador"),cantincentivos=input("Ingrese la cantidad de inscentivos:"),importextra=input("Ingrese el importe extra:"))
            self.__lista.agregarPersonal(personal)
        else:
            print("No se puede agregar a la lista")

    def MostrarposLista(self, pos):
        self.__lista.mostrarposlista(pos)

    def listadoOrdenado(self, carrera):
        self.__lista.listadoordenado(carrera)

    def ContarAgentes(self, areaI):
        self.__lista.contarAgentes(areaI)

    def MostrarOrdenado(self):
        self.__lista.mostrarOrdenado()

    def listarCategoria(self, categoria):
        self.__lista.mostrarcat(categoria)

    def GuardarArchivo(self):
        jsonF = ObjectEncoder()
        self.__lista.guardaJson(jsonF)
