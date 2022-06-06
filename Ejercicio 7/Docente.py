from Personal import Personal


class Docente(Personal):
    __carrera=None
    __cargo=None
    __catedra=None

    def __init__(self, **kwargs):
        self.__carrera = kwargs["carrera"]
        self.__cargo = kwargs["cargo"]
        self.__catedra = kwargs["catedra"]
        super().__init__(**kwargs)

    def __str__(self):
        cadena = super().__str__()
        cadena += "Carrera:{} Cargo:{} Catedra:{}".format(self.__carrera,self.__cargo,self.__catedra)
        return cadena

    def getcarrera(self):
        return self.__carrera

    def getcargo(self):
        return self.__cargo

    def getcatedra(self):
        return self.__catedra

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

    def getsueldoDocente(self):
        sueldo = self.sueldoPersonal()
        if self.__cargo == "simple":
            sueldo + ((sueldo*10)/100)
        elif self.__cargo == "semiexclusivo":
            sueldo + ((sueldo*20)/100)
        elif self.__cargo == "exclusivo":
            sueldo + ((sueldo*50)/100)
        return sueldo
