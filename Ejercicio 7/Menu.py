from Manejador import Manejador
import os


class Menu:
    __instanciaManejador=None

    def __init__(self):
        self.__instanciaManejador = Manejador()

    def op(self):
        self.__instanciaManejador.CargaJson()
        self.__instanciaManejador.CargaLista()
        self.__instanciaManejador.MostrarLista()
        print("1:Insertar a agentes a la colección.\n2:Agregar agentes a la colección.\n3:Dada una posición de la lista: Mostrar por pantalla que tipo de agente se encuentra almacenado en dicha posición.\n4:Ingresar por teclado el nombre de una carrera y generar un listado ordenado por nombre con todos los datos de los agentes que se desempeñan como docentes investigadores.\n5:Dada un área de investigación, contar la cantidad de agentes que son docente    investigador, y la cantidad de investigadores que trabajen en ese área.\n6:Recorrer la colección y generar un listado que muestre nombre y apellido, tipo de Agente y sueldo de todos los agentes, ordenado por apellido.\n7:Dada una categoría de investigación (I, II, III, IV o V), leída desde teclado, listar apellido, nombre e importe extra por docencia e investigación, de todos los docentes investigadores que poseen esa categoría, al final del listado deberá mostrar el total de dinero que la Secretaría de Investigación debe solicitar al Ministerio en concepto de importe extra que cobran los docentes investigadores de la categoría solicitada.\n8:Almacenar los datos de todos los agentes en el archivo “personal.json”    ")
        opcion = int(input("Ingrese la opcion (finalice con 0):"))
        while opcion != 0:
            os.system('cls')
            if opcion == 1:
                self.__instanciaManejador.InsertarLista(int(input("Ingrese la posicion de la lista:")))
                self.__instanciaManejador.MostrarLista()
            elif opcion == 2:
                self.__instanciaManejador.AgregarLista()
                self.__instanciaManejador.MostrarLista()
            elif opcion == 3:
                self.__instanciaManejador.MostrarposLista(int(input("Ingrese la posicion de la lista:")))
            elif opcion == 4:
                carrera=input("Ingrese el nombre de una carrera:")
                self.__instanciaManejador.listadoOrdenado(carrera)
            elif opcion == 5:
                areaI = input("Ingrese un area de Investigacion:")
                self.__instanciaManejador.ContarAgentes(areaI)
            elif opcion == 6:
                self.__instanciaManejador.MostrarOrdenado()
            elif opcion == 7:
                cat = input("Ingrese una Categoria(I, II, III, IV o V):")
                self.__instanciaManejador.listarCategoria(cat)
            elif opcion == 8:
                self.__instanciaManejador.GuardarArchivo()
            else:
                print("La Opcion ingresada no existe")
            print("1:Insertar a agentes a la colección.\n2:Agregar agentes a la colección.\n3:Dada una posición de la lista: Mostrar por pantalla que tipo de agente se encuentra almacenado en dicha posición.\n4:Ingresar por teclado el nombre de una carrera y generar un listado ordenado por nombre con todos los datos de los agentes que se desempeñan como docentes investigadores.\n5:Dada un área de investigación, contar la cantidad de agentes que son docente    investigador, y la cantidad de investigadores que trabajen en ese área.\n6:Recorrer la colección y generar un listado que muestre nombre y apellido, tipo de Agente y sueldo de todos los agentes, ordenado por apellido.\n7:Dada una categoría de investigación (I, II, III, IV o V), leída desde teclado, listar apellido, nombre e importe extra por docencia e investigación, de todos los docentes investigadores que poseen esa categoría, al final del listado deberá mostrar el total de dinero que la Secretaría de Investigación debe solicitar al Ministerio en concepto de importe extra que cobran los docentes investigadores de la categoría solicitada.\n8:Almacenar los datos de todos los agentes en el archivo “personal.json”")
            opcion=int(input("Ingrese la opcion (finalice con 0):"))
            os.system('cls')
