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

    def opgenerales(self):
        self.__lista.mostrarlista()
        print("1:Insertar a agentes a la colección.\n2:Agregar agentes a la colección.\n3:Dada una posición de la lista: Mostrar por pantalla que tipo de agente se encuentra almacenado en dicha posición.\n4:Ingresar por teclado el nombre de una carrera y generar un listado ordenado por nombre con todos los datos de los agentes que se desempeñan como docentes investigadores.\n5:Dada un área de investigación, contar la cantidad de agentes que son docente    investigador, y la cantidad de investigadores que trabajen en ese área.\n6:Recorrer la colección y generar un listado que muestre nombre y apellido, tipo de Agente y sueldo de todos los agentes, ordenado por apellido.\n7:Dada una categoría de investigación (I, II, III, IV o V), leída desde teclado, listar apellido, nombre e importe extra por docencia e investigación, de todos los docentes investigadores que poseen esa categoría, al final del listado deberá mostrar el total de dinero que la Secretaría de Investigación debe solicitar al Ministerio en concepto de importe extra que cobran los docentes investigadores de la categoría solicitada.\n8:Almacenar los datos de todos los agentes en el archivo “personal.json”    ")
        opcion = int(input("Ingrese la opcion (finalice con 0):"))
        while opcion != 0:
            if opcion == 1:
                pos = (int(input("Ingrese la posicion de la lista:")))
                tipo = input("Ingrese el tipo de personal(Docente/Investigador/DocenteInvestigador):")
                if tipo == "Docente":
                    personal = Docente(cuil=input("ingrese el Cuil:"), apellido=input("Ingrese el Apellido:"), nombre=input("Ingrese el Nombre:"), sueldobasico=float(input("Ingrese el Sueldo Basico:")), antiguedad=input("Ingrese la Antiguedad:"), carrera=input("Ingrese Carrera:"), cargo=input("Ingrese el cargo:"), catedra=input("Ingrese catedra:"))
                    self.__lista.insertarPersonal(personal, pos)
                elif tipo == "Investigador":
                    personal = Investigador(cuil=input("ingrese el Cuil:"), apellido=input("Ingrese el Apellido:"), nombre=input("Ingrese el Nombre:"), sueldobasico=float(input("Ingrese el Sueldo Basico:")), antiguedad=input("Ingrese la Antiguedad:"), areainvestigacion=input("Ingrese el area de Investigacion:"), tipinvestigacion=input("Ingrese el tipo de Investigador"))
                    self.__lista.insertarPersonal(personal, pos)
                elif tipo == "DocenteInvestigador":
                    personal = DocenteInvestigador(cuil=input("ingrese el Cuil:"), apellido=input("Ingrese el Apellido:"), nombre=input("Ingrese el Nombre:"), sueldobasico=float(input("Ingrese el Sueldo Basico:")), antiguedad=input("Ingrese la Antiguedad:"),carrera=input("Ingrese Carrera:"),cargo=input("Ingrese el cargo:"),catedra=input("Ingrese catedra:"),areainvestigacion=input("Ingrese el area de Investigacion:"),tipinvestigacion=input("Ingrese el tipo de Investigador"),cantincentivos=input("Ingrese la cantidad de inscentivos:"), importextra=input("Ingrese el importe extra:"))
                    self.__lista.insertarPersonal(personal, pos)

            elif opcion == 2:

                tipo=input("Ingrese el tipo de personal(Docente/Investigador/DocenteInvestigador):")
                if tipo == "Docente":
                    personal = Docente(cuil=input("ingrese el Cuil:"), apellido=input("Ingrese el Apellido:"),nombre=input("Ingrese el Nombre:"),sueldobasico=float(input("Ingrese el Sueldo Basico:")),antiguedad=input("Ingrese la Antiguedad:"),carrera=input("Ingrese Carrera:"),cargo=input("Ingrese el cargo:"),catedra=input("Ingrese catedra:"))
                    self.__lista.agregarPersonal(personal)
                elif tipo == "Investigador":
                    personal = Investigador(cuil=input("ingrese el Cuil:"), apellido=input("Ingrese el Apellido:"),nombre=input("Ingrese el Nombre:"),sueldobasico=float(input("Ingrese el Sueldo Basico:")),antiguedad=input("Ingrese la Antiguedad:"),areainvestigacion=input("Ingrese el area de Investigacion:"),tipinvestigacion=input("Ingrese el tipo de Investigador"))
                    self.__lista.agregarPersonal(personal)
                elif tipo == "DocenteInvestigador":
                    personal = DocenteInvestigador(cuil=input("ingrese el Cuil:"), apellido=input("Ingrese el Apellido:"),nombre=input("Ingrese el Nombre:"),sueldobasico=float(input("Ingrese el Sueldo Basico:")),antiguedad=input("Ingrese la Antiguedad:"),carrera=input("Ingrese Carrera:"),cargo=input("Ingrese el cargo:"),catedra=input("Ingrese catedra:"),areainvestigacion=input("Ingrese el area de Investigacion:"),tipinvestigacion=input("Ingrese el tipo de Investigador"),cantincentivos=input("Ingrese la cantidad de inscentivos:"),importextra=input("Ingrese el importe extra:"))
                    self.__lista.agregarPersonal(personal)
                else:
                    print("No se puede agregar a la lista")

            elif opcion == 3:
                self.__lista.mostrarposlista(int(input("Ingrese la posicion de la lista:")))

            elif opcion == 4:
                carrera = input("Ingrese el nombre de una carrera:")
                self.__lista.listadoordenado(carrera)

            elif opcion == 5:
                areaI = input("Ingrese un area de Investigacion:")
                self.__lista.contarAgentes(areaI)

            elif opcion == 6:
                self.__lista.mostrarOrdenado()

            elif opcion == 7:
                categoria = input("Ingrese una Categoria(I, II, III, IV o V):")
                self.__lista.mostrarcat(categoria)

            elif opcion == 8:
                jsonF = ObjectEncoder()
                self.__lista.guardaJson(jsonF)

            else:
                print("La Opcion ingresada no existe")
            print("1:Insertar a agentes a la colección.\n2:Agregar agentes a la colección.\n3:Dada una posición de la lista: Mostrar por pantalla que tipo de agente se encuentra almacenado en dicha posición.\n4:Ingresar por teclado el nombre de una carrera y generar un listado ordenado por nombre con todos los datos de los agentes que se desempeñan como docentes investigadores.\n5:Dada un área de investigación, contar la cantidad de agentes que son docente    investigador, y la cantidad de investigadores que trabajen en ese área.\n6:Recorrer la colección y generar un listado que muestre nombre y apellido, tipo de Agente y sueldo de todos los agentes, ordenado por apellido.\n7:Dada una categoría de investigación (I, II, III, IV o V), leída desde teclado, listar apellido, nombre e importe extra por docencia e investigación, de todos los docentes investigadores que poseen esa categoría, al final del listado deberá mostrar el total de dinero que la Secretaría de Investigación debe solicitar al Ministerio en concepto de importe extra que cobran los docentes investigadores de la categoría solicitada.\n8:Almacenar los datos de todos los agentes en el archivo “personal.json”")
            opcion = int(input("Ingrese la opcion (finalice con 0):"))

    def CargaJson(self):
        objeto1 = Docente(cuil="43344334", apellido="Gonzalez",nombre="Martin",sueldobasico=20000,antiguedad=10,carrera="LCC",cargo="Suplente",catedra="POO")
        objeto2 = Investigador(cuil="45343543", apellido="Laciar", nombre="Joaquin", sueldobasico=30000, antiguedad=20, areainvestigacion="Informatica", tipinvestigacion="Robotica")
        objeto3 = DocenteInvestigador(cuil="4344343", apellido="Fuentes", nombre="Jazmin", sueldobasico=40000, antiguedad=4,carrera="LCC", cargo="semiexclusivo", catedra="POO", areainvestigacion="Informatica", tipinvestigacion="Robotica", cantincentivos="I", importextra=5000)
        objeto4 = DocenteInvestigador(cuil="4344243", apellido="Fuentes", nombre="Aguero", sueldobasico=40000, antiguedad=4,carrera="LCC", cargo="simple", catedra="POO", areainvestigacion="Informatica", tipinvestigacion="Robotica", cantincentivos="I", importextra=5000)
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

    def opTesorero(self):
        print("0:EXIT\n1:Acceder a los gastos que la universidad tiene en concepto de sueldos, para ello, dado un número de documento, podrá consultar el gasto de sueldos para el agente al que pertenece dicho número de documento.")
        op = int(input("Ingrese una opcion:"))
        while op != 0:
            if op == 1:
                cuil = input("Ingrese un cuil:")
                self.__lista.gastosSueldoPorEmpleado(cuil)
            else:
                print("El codigo ingresado no existe")
            op = int(input("Ingrese una opcion:"))

    def opDirector(self):
        print("0:EXIT\n1:modificarBasico\n2:modificarPorcentajeporcargo\n3:modificarPorcentajeporcategoría\n4:modificarImporteExtra")
        op = int(input("Ingrese una opcion:"))
        while op != 0:
            if op == 1:
                nuevob = float(input("Ingrese un nuevo basico:"))
                cuil = input("Ingrese un cuil:")
                self.__lista.modificarBasico(cuil, nuevob)
            elif op == 2:
                nuevop = float(input("Ingrese un nuevo Porcentaje:"))
                cuil = input("Ingrese un cuil:")
                self.__lista.modificarPorcentajeporcargo(cuil, nuevop)
            elif op == 3:
                nuevop = float(input("Ingrese un nuevo Porcentaje:"))
                cuil = input("Ingrese un cuil:")
                self.__lista.modificarPorcentajeporcategoria(cuil, nuevop)
            elif op == 4:
                nuevoimp = float(input("Ingrese un nuevo Importe Extra:"))
                cuil = input("Ingrese un cuil:")
                self.__lista.modificarImporteExtra(cuil, nuevoimp)
            else:
                print("El codigo ingresado no existe")

            print("0:EXIT\n1:modificarBasico\n2:modificarPorcentajeporcargo\n3:modificarPorcentajeporcategoría\n4:modificarImporteExtra")
            op = int(input("Ingrese una opcion:"))
