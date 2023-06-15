from abc import ABC

class Vehiculo(ABC):
    __modelo = None
    __cantidad_puertas = None
    __color = None
    __precio_base = None

    def __init__(self,modelo,puertas,color,precio):
        self.__modelo = modelo
        self.__cantidad_puertas = puertas
        self.__color = color
        self.__precio_base = precio

    def getModelo(self):
        return self.__modelo
    
    def getCantidadPuertas(self):
        self.__cantidad_puertas

    def getColor(self):
        return self.__color
    
    def getPrecioBase(self):
        return self.__precio_base
    
    def cambiarPrecio(self,precio):
        self.__precio_base = precio

    def toJSON(self):
        pass

