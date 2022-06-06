from Docente import Docente
from Investigador import Investigador


class DocenteInvestigador(Docente, Investigador):
    __catincentivos=None
    __impextra=None

    def __init__(self, **kwargs):
        self.__catincentivos = kwargs["cantincentivos"]
        self.__impextra = kwargs["importextra"]
        super().__init__(**kwargs)

    def __gt__(self, other):
        return self.getnombre() > other.getnombre()

    def __str__(self):
        cadena = super().__str__()
        cadena += " Cantidad de Incentivos:{} Importe Extra:{}".format(self.__catincentivos, self.__impextra)
        return cadena

    def getcatincentivos(self):
        return self.__catincentivos

    def getimpextra(self):
        return self.__impextra

    def toJSON(self):
        d = super().toJSON()["__atributos__"]
        d.update(dict(
                cantincentivos=self.__catincentivos,
                importextra=self.__impextra,
            ))
        dH = dict(
                __class__=self.__class__.__name__,
                __atributos__=d
            )
        return dH

    def getsueldoDocInv(self):
        return self.getsueldoDocente() + self.__impextra
