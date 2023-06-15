class Persona:
    __nombre = None
    __direccion = None
    __DNI = None

    def __init__(self,nombre,direccion,dni):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__DNI = dni

    def getNombre(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getDNI(self):
        return self.__DNI
    
    def __str__(self):
        return "\nNombre: %s Direccion: %s DNI: %s"%(self.__nombre,self.__direccion,self.__DNI)