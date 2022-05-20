from ManejadorRamos import ManejadorRamos
from ManejadorFlores import ManejadorFlores

class Menu:
    __instanciaRamos = None
    __instanciaFlor = None

    def __init__(self):
        self.__instanciaRamos = ManejadorRamos()
        self.__instanciaFlor = ManejadorFlores()

    def menuOp(self):
        print("0:Exit\n1:Registrar un ramo vendido (instancia de la clase ramo), solicitando las flores que lo que se pondrán en el ramo.\n2:Mostrar el nombre de las 5 flores  más pedidas en un ramo, considerando todos los ramos vendidos.\n4:Ingresar por teclado un tipo de ramo y mostrar las flores vendidas en ese tamaño considerando todos los ramos vendidos.")
        op = int(input("Ingrese un numero de opcion:"))
        self.__instanciaFlor.CargaF()
        while op != 0:
            if op == 1:
                self.__instanciaRamos.setRamo(self.__instanciaFlor)
                self.__instanciaRamos.mostrarramo()
            elif op == 2:
                self.__instanciaRamos.mostrarmaximos()

            elif op == 3:

            else:
                print("La opcion ingresada No existe")
            print("-------\n0:Exit\n1:Registrar un ramo vendido (instancia de la clase ramo), solicitando las flores que lo que se pondrán en el ramo.\n2:Mostrar el nombre de las 5 flores  más pedidas en un ramo, considerando todos los ramos vendidos.\n4:Ingresar por teclado un tipo de ramo y mostrar las flores vendidas en ese tamaño considerando todos los ramos vendidos.")
            op = int(input("Ingrese un numero de opcion:"))
