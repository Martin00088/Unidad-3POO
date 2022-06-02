from Manejador import ManejadorInterface


class Menu:
    __instanciaManejador=None

    def __init__(self):
        self.__instanciaManejador = ManejadorInterface()

    def op(self):
        self.__instanciaManejador.CargaJson()
        self.__instanciaManejador.CargaLista()
        self.__instanciaManejador.MostrarLista()
        print("1:Insertar un aparato en la colección en una posición determinada.\n2:Agregar un aparato a la colección (solicitar el tipo de aparato, y luego los datos que correspondan).\n3:Dada una posición de la Lista: Mostrar por pantalla qué tipo de objeto se encuentra almacenado en dicha posición.\n4: Mostrar la cantidad de heladeras, lavarropas y televisores cuya marca sea phillips.\n5:Mostrar la marca de todos los lavarropas que tienen carga superior .\n6:Mostrar para todos los aparatos que la empresa tiene a la venta, marca, país de fabricación e importe de venta.\n7:Almacenar los objetos de la colección Lista en el archivo “aparatoselectronicos.json”.")
        opcion = int(input("Ingrese la opcion (finalice con 0):"))
        while opcion != 0:
            if opcion == 1:
                elemento=input("Ingrese el tipo de elemento(Heladera/Televisor/Lavarropa):")
                pos = int(input("Ingrese la posicion en la que va a estar:"))
                self.__instanciaManejador.insertarElemento(elemento, pos)
                self.__instanciaManejador.MostrarLista()
            elif opcion == 2:
                elemento=input("Ingrese el tipo de elemento(Heladera/Televisor/Lavarropa):")
                self.__instanciaManejador.agregarElemento(elemento)
                self.__instanciaManejador.MostrarLista()
            elif opcion == 3:
                pos = int(input("Ingrese la posicion a mostrar:"))
                self.__instanciaManejador.mostrarposAparato(pos)
            elif opcion == 4:
                self.__instanciaManejador.mostrarphilips()
            elif opcion == 5:
                self.__instanciaManejador.CargaSup()
            elif opcion == 6:
                self.__instanciaManejador.mostraremperesa()
            elif opcion == 7:
                self.__instanciaManejador.guardarlista()
            else:
                print("La Opcion ingresada no existe")
            print("----\n1:Insertar un aparato en la colección en una posición determinada.\n2:Agregar un aparato a la colección (solicitar el tipo de aparato, y luego los datos que correspondan).\n3:Dada una posición de la Lista: Mostrar por pantalla qué tipo de objeto se encuentra almacenado en dicha posición.\n4: Mostrar la cantidad de heladeras, lavarropas y televisores cuya marca sea phillips.\n5:Mostrar la marca de todos los lavarropas que tienen carga superior .\n6:Mostrar para todos los aparatos que la empresa tiene a la venta, marca, país de fabricación e importe de venta.\n7:Almacenar los objetos de la colección Lista en el archivo “aparatoselectronicos.json”.")
            opcion = int(input("Ingrese la opcion (finalice con 0):"))
