from Personal import Personal


class PersonalApoyo(Personal):
    __categoria = None
    __porcecateg = None

    def __init__(self, **kwargs):
        self.__categoria = kwargs["categoria"]
        self.__porcecateg = None
        super().__init__(**kwargs)

    def __str__(self):
        cadena = super().__str__()
        cadena += "Categoria:{}".format(self.__categoria)
        return cadena

    def getporcentajecat(self):
        return self.__porcecateg

    def getcategoria(self):
        return self.__categoria

    def getclase(self):
        return "Personal de Apoyo"

    def toJSON(self):
        d = super().toJSON()["__atributos__"]
        d.update(dict(
                categoria=self.__categoria,
            ))
        dH = dict(
                __class__=self.__class__.__name__,
                __atributos__=d
            )
        return dH

    def porceCategoria(self):
        sueldo = self.setsueldoPersonal()
        if self.__categoria >= 1 and self.__categoria <= 10:
            self.__porcecateg = ((sueldo*10)/100)
        elif self.__categoria >= 11 and self.__categoria <= 20:
            self.__porcecateg = ((sueldo*20)/100)
        elif self.__categoria >= 21 and self.__categoria <= 22:
            self.__porcecateg = ((sueldo*30)/100)

    def getsueldo(self):
        return self.setsueldoPersonal() + self.getporcentajecat()

    def modificarporcategoria(self,nuevopor):
        self.__porcecateg = (self.setsueldoPersonal()*nuevopor)/100
