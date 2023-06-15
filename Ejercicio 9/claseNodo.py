from claseNuevo import Nuevo
from claseVehiculo import Vehiculo
import json

class Nodo:
    __vehiculo = None
    __siguiente = None

    def __init__(self,vehiculo):
        self.__vehiculo = vehiculo
        self.__siguiente = None

    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente

    def getDato(self):
        return self.__vehiculo
    
    def toJSON(self):
        d = dict(
        __class__ = self.__class__.__name__,
        __atributos__ = dict(
        vehiculo = self.__vehiculo.toJSON()
        ))
        return d