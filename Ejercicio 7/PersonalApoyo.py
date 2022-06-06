from Personal import Personal


class PersonalApoyo(Personal):
    __categoria=None

    def __init__(self, **kwargs):
        self.__categoria = kwargs["categoria"]
        super().__init__(**kwargs)

    def __str__(self):
        cadena = super().__str__()
        cadena += "Categoria:{}".format(self.__categoria)
        return cadena

    def getcategoria(self):
        return self.__categoria

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


    def sueldoPerApoyo(self):
        sueldo = self.sueldoPersonal()
        if self.__categoria >= 1 and self.__categoria <= 10:
            sueldo + ((sueldo*10)/100)
        elif self.__categoria >= 11 and self.__categoria <= 20:
            sueldo + ((sueldo*20)/100)
        elif self.__categoria >= 21 and self.__categoria <= 22:
            sueldo + ((sueldo*30)/100)
        return sueldo
