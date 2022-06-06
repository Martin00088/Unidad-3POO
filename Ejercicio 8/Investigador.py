from Personal import Personal


class Investigador(Personal):
    __areainves=None
    __tipinves=None

    def __init__(self, **kwargs):
        self.__areainves = kwargs["areainvestigacion"]
        self.__tipinves = kwargs["tipinvestigacion"]
        super().__init__(**kwargs)

    def __str__(self):
        cadena = super().__str__()
        cadena += "Area Investigacion:{} Tipo de Investigacion:{}".format(self.__areainves,self.__tipinves)
        return cadena

    def getainvestigacion(self):
        return self.__areainves

    def gettipinves(self):
        return self.__tipinves

    def getclase(self):
        return "Investigador"

    def toJSON(self):
        d = super().toJSON()["__atributos__"]
        d.update(dict(
                areainvestigacion=self.__areainves,
                tipinvestigacion=self.__tipinves,
            ))
        dH = dict(
                __class__=self.__class__.__name__,
                __atributos__=d
            )
        return dH

    def sueldoInvestigador(self):
        return self.setsueldoPersonal()

