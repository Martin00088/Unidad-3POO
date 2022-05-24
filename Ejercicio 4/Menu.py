from ManejadorCalefactor import ManejadorCalefactor


class Menu:
    __instanciaCalefactor = None

    def __init__(self):
        self.__instanciaCalefactor = ManejadorCalefactor()

    def op(self):
        self.__instanciaCalefactor.CargaCG()
        self.__instanciaCalefactor.CargaCE()
        self.__instanciaCalefactor.mostrar()
        posmin=-1
        print("1:Ingresar por teclado el  costo por m3 y cantidad que se estima consumir en m3 y mostrar marca y modelo del calefactor a gas natural de menor costo de consumo.\n2:Ingresar por teclado el costo de el kilowatt/h, la cantidad que se estima consumir por hora y mostrar  marca  y modelo del calefactor eléctrico de menor consumo.\n3:Teniendo en cuenta los dos ítems anteriores, muestre: tipo de calefactor y todos los datos del calefactor de menor consumo.\n")
        opcion = int(input("Ingrese la opcion (finalice con 0)"))
        while opcion != 0:
            if opcion == 1:
                costo = float(input("Ingrese el costo por m3:"))
                cantidad = float(input("Cantidad que se estima consumir en m3:"))
                pos=self.__instanciaCalefactor.item1y2(costo, cantidad)
                print("El de menor consumo es el calefactor de modelo {} y marca {}".format(self.__instanciaCalefactor.getposarr(pos).getmodelo(),self.__instanciaCalefactor.getposarr(pos).getmarca()))
                posmin = pos
            elif opcion == 2:
                costo = float(input("Ingrese el costo del kilowatt/h:"))
                cantidad = float(input("Ingrese la cantidad que se estima a consumir por hora:"))
                pos = self.__instanciaCalefactor.item1y2(costo, cantidad)
                print("El de menor consumo es el calefactor de modelo {} y marca {}".format(self.__instanciaCalefactor.getposarr(pos).getmodelo(),self.__instanciaCalefactor.getposarr(pos).getmarca()))
                if pos == posmin:
                    posmin = pos
            elif opcion == 3:
                print("El tipo es {}".format(self.__instanciaCalefactor.mostrartipo(posmin)))
                print(self.__instanciaCalefactor.mostraritems(posmin))
            else:
                print("La Opcion ingresada no existe")
            opcion=int(input("Ingrese la opcion (finalice con 0)"))

