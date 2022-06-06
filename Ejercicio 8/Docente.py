from Personal import Personal


class Docente(Personal):
    __carrera=None
    __cargo=None
    __catedra=None
    __porcencargo=None

    def __init__(self, **kwargs):
        self.__carrera = kwargs["carrera"]
        self.__cargo = kwargs["cargo"]
        self.__catedra = kwargs["catedra"]
        self.__porcencargo = 0
        super().__init__(**kwargs)

    def __str__(self):
        cadena = super().__str__()
        cadena += "Carrera:{} Cargo:{} Catedra:{}".format(self.__carrera,self.__cargo,self.__catedra)
        return cadena

    def getporcentajecargo(self):
        return self.__porcencargo

    def getcarrera(self):
        return self.__carrera

    def getcargo(self):
        return self.__cargo

    def getcatedra(self):
        return self.__catedra

    def getclase(self):
        return "Docente"

    def toJSON(self):
        d = super().toJSON()["__atributos__"]
        d.update(dict(
                carrera=self.__carrera,
                cargo=self.__cargo,
                catedra=self.__catedra,
            ))
        dH = dict(
                __class__=self.__class__.__name__,
                __atributos__=d
            )
        return dH

    def getporcentajeCargo(self):
        if self.__cargo == "simple":
            self.__porcencargo = ((self.setsueldoPersonal()*10)/100)
        elif self.__cargo == "semiexclusivo":
           self.__porcencargo = ((self.setsueldoPersonal()*20)/100)
        elif self.__cargo == "exclusivo":
            self.__porcencargo = ((self.setsueldoPersonal()*50)/100)

    def setsueldoDocente(self):
        return self.setsueldoPersonal() + self.getporcentajecargo()

    def getsueldo(self):
        return self.setsueldoDocente()

    def modificarporcargo(self, nuevopor):
        self.__porcencargo = (self.setsueldoPersonal()*nuevopor)/100
