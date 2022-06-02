from zope.interface import implementer
from Televisor import Televisor
from Heladera import Heladera
from Lavarropa import Lavarropa
from ObjectEncoder import  ObjectEncoder
from Interfaz import Interface
from Lista import Lista

@implementer(Interface)
class ManejadorInterface:
    __lista = None

    def __init__(self):
        self.__lista = Lista()

    def CargaJson(self):
        objeto1 = Heladera("Lg", "FKROA", "Negro", "Argentina", 325000, 2300, True, False)
        objeto2 = Lavarropa("Liliana", "45LDKN", "Blanco", "Argentina", 450000, 4, 2300, 2, "superior")
        objeto3 = Televisor("Hitachi", "IIOER89", "Blanco", "USA", 45400, "LCD", "55.5", "HD", True)
        objeto4 = Televisor("Philips", "IIOER89", "Blanco", "USA", 45400, "LCD", "55.5", "HD", True)
        jsonF = ObjectEncoder()
        d = objeto1.toJSON()
        d1 = objeto2.toJSON()
        d2 = objeto3.toJSON()
        d3 = objeto4.toJSON()
        lista = [d, d1, d2, d3]
        jsonF.guardarJSONArchivo(lista, "Aparatos.json")

    def CargaLista(self):
        jsonF = ObjectEncoder()
        jsonF.decodificarDiccionario(self.__lista)

    def MostrarLista(self):
        self.__lista.listarAparato()

    def insertarElemento(self, elemento, pos):
        if elemento == "Heladera" or "Lavarropa" or "Televisor":
            marca=input("Ingrese la Marca:")
            modelo=input("Ingrese Modelo:")
            color=input("Ingrese Color:")
            PF=input("Ingrese Pais de Fabricacion:")
            PB=float(input("Ingrese Precio Base:"))
            if elemento == "Heladera":
                clitros=input("Ingrese la cantidad de litros:")
                frezzer=bool(input("Ingrese frezzer(True/False):"))
                ciclica=bool(input("Ingrese ciclica(True/False):"))
                H = Heladera(marca,modelo,color,PF,PB,clitros,frezzer,ciclica)
                self.__lista.insertaraparato(H,pos)
            elif elemento == "Lavarropa":
                clavado=input("Ingrese la capacidad de lavado:")
                vcent=input("Ingrese la velocidad de centrifuga:")
                cantpro=input("Ingrese la cantidad de programas:")
                ticar=input("Ingrese el tipo de Carga:")
                L=Lavarropa(marca,modelo,color,PF,PB,clavado,vcent,cantpro,ticar)
                self.__lista.insertaraparato(L,pos)
            elif elemento == "Televisor":
                tipPan=input("Ingrese el tipo de Pantalla:")
                pulgadas=input("Ingrese las pulgadas:")
                TipDef=input("Ingrese el tipo de definicion:")
                ConInt=input("Ingrese Conexion a internet(True/False:")
                T = Televisor(marca,modelo,color,PF,PB,tipPan,pulgadas,TipDef,ConInt)
                self.__lista.insertaraparato(T,pos)
        else:
            print("El aparato ingresado no existe")

    def agregarElemento(self, elemento):
        if elemento == "Heladera" or "Lavarropa" or "Televisor":
            marca=input("Ingrese la Marca:")
            modelo=input("Ingrese Modelo:")
            color=input("Ingrese Color:")
            PF=input("Ingrese Pais de Fabricacion:")
            PB=float(input("Ingrese Precio Base:"))
            if elemento == "Heladera":
                clitros=input("Ingrese la cantidad de litros:")
                frezzer=bool(input("Ingrese frezzer(True/False):"))
                ciclica=bool(input("Ingrese ciclica(True/False):"))
                H = Heladera(marca,modelo,color,PF,PB,clitros,frezzer,ciclica)
                self.__lista.agregarAparato(H)
            elif elemento == "Lavarropa":
                clavado=input("Ingrese la capacidad de lavado:")
                vcent=input("Ingrese la velocidad de centrifuga:")
                cantpro=input("Ingrese la cantidad de programas:")
                ticar=input("Ingrese el tipo de Carga:")
                L=Lavarropa(marca,modelo,color,PF,PB,clavado,vcent,cantpro,ticar)
                self.__lista.agregarAparato(L)
            elif elemento == "Televisor":
                tipPan=input("Ingrese el tipo de Pantalla:")
                pulgadas=input("Ingrese las pulgadas:")
                TipDef=input("Ingrese el tipo de definicion:")
                ConInt=input("Ingrese Conexion a internet(True/False:")
                T = Televisor(marca,modelo,color,PF,PB,tipPan,pulgadas,TipDef,ConInt)
                self.__lista.agregarAparato(T)
        else:
            print("El aparato ingresado no existe")

    def mostrarposAparato(self, pos):
        self.__lista.listarposAparato(pos)

    def mostrarphilips(self):
        self.__lista.listarPhilips()

    def CargaSup(self):
        self.__lista.cargasup()

    def mostraremperesa(self):
        self.__lista.infoempresa()

    def guardarlista(self):
        jsonF = ObjectEncoder()
        self.__lista.guardaJson(jsonF)
