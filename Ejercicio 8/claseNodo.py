from clasePersonal import Personal

class Nodo:
    __personal = None
    __siguiente = None

    def __init__(self,personal):
        self.__personal = personal
        self.__siguiente = None

    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente
    
    def setDato(self,nodo):
        self.__personal = nodo
    
    def getDato(self):
        return self.__personal
    
    def toJSON(self):
        d = dict(
            __class__ = __class__.__name__,
            __atributos__ = dict(
            personal = self.__personal.toJSON()
            )
        )
        return d