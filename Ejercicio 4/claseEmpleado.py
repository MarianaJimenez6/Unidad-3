import abc
from abc import ABC

class Empleado:
    __DNI = None
    __nombre = None
    __direccion = None
    __telefono = None

    def __init__(self,dni,nom,direccion,tel):
        self.__DNI = dni
        self.__nombre = nom
        self.__direccion = direccion
        self.__telefono = tel

    def getDNI(self):
        return self.__DNI
    
    def getNombre(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getTelefono(self):
        return self.__telefono
    
    def calcularSueldo(self):
        pass