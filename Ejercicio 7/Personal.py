class Personal:
    __cuil=None
    __apellido=None
    __nombre=None
    __suelbasico=None
    __antiguedad=None

    def __init__(self, **kwargs):
        self.__cuil = kwargs["cuil"]
        self.__apellido = kwargs["apellido"]
        self.__nombre = kwargs["nombre"]
        self.__suelbasico = kwargs["sueldobasico"]
        self.__antiguedad = kwargs["antiguedad"]

    def __str__(self):
        return  "Cuil:{} Apellido:{} Nombre:{} Sueldo Basico:{} Antiguedad:{}".format(self.__cuil,self.__apellido,self.__nombre,self.__suelbasico,self.__antiguedad)

    def __lt__(self, other):
        return self.__apellido < other.__apellido

    def getcuil(self):
        return self.__cuil

    def getapellido(self):
        return self.__apellido

    def getnombre(self):
        return self.__nombre

    def getsbasico(self):
        return self.__suelbasico

    def getantiguedad(self):
        return self.__antiguedad

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=self.__cuil,
                apellido=self.__apellido,
                nombre=self.__nombre,
                sueldobasico=self.__suelbasico,
                antiguedad=self.__antiguedad,
            )
        )
        return d

    def sueldoPersonal(self):
        return self.__suelbasico + ((self.__antiguedad*100)/self.__suelbasico)
