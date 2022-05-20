from Ramo import Ramo


class ManejadorRamos:
    __lista = []

    def __init__(self):
        self.__lista = []

    def setRamo(self, listaflor):
        tamano = int(input("Ingrese un tamaño de ramo(finalizar con 0) 1=chico, 2=mediano y 3=grande :"))
        if tamano > 0 and tamano < 4:
            r = Ramo(tamano)
            numflor = int(input("Ingrese el numero de una flor (terminar con 0):"))
            while numflor != 0:
                r.addFlor(listaflor.getFlor(numflor))
                numflor = int(input("Ingrese otro numero de una flor (terminar con 0):"))
            self.__lista.append(r)
        else:
            print("El tamaño ingresado no es valido")

    def mostrarramo(self):
        for i in range(len(self.__lista)):
            print(self.__lista[i])

    def getlista(self):
        return self.__lista

    def getposlista(self,pos):
        return self.__lista[pos]

    def mostrarmaximos(self):
        for i in range(len(self.__lista)):
            flores = self.__lista[i].getFlores()
            datos = {}
            for flor in flores:
                if flor.getnombre() not in datos:
                    datos[flor.getnombre()] = 1
                else:
                    datos[flor.getnombre()] += 1
            datos = sorted(datos.items(), key=lambda x:x[1], reverse=True) #lambda ordena a partir de las componente del diccionario
            try:
                print("----5 Flores mas pedidas para el ramo {} de tamaño: {}----".format(i+1, self.__lista[i].getTam()))
                for i in range(5):
                    print("Top: {}, Nombre: {}, Cantidad: {}".format(i+1, datos[i][0], datos[i][1]))
            except Exception:
                print("Al parecer no hay 5 tipos de flores distintas en este ramo, por lo tanto no es posible realizar el top de manera correcta")
