from claseCarrera import Carrera

class Facultad:
    __codigo = None
    __nombre = None
    __direccion = None
    __localidad = None
    __telefono = None
    __carrera = list

    def __init__(self,codigo,nombre,direccion,localidad,telefono):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telefono = telefono
        self.__carrera = []

    '''def __del__(self):
        print("---Borrando carreras---")
        del self.__carrera''' 

    def __str__(self):
        cadena="Codigo: {}, Nombre: {}, Direccion: {}, Localidad: {}, Telefono: {}".format(self.__codigo,self.__nombre,self.__direccion,self.__localidad,self.__telefono)
        for i in range(len(self.__carrera)):
            cadena += "\nDatos de carrera: \n {}".format(self.__carrera[i])
        return cadena
    
    def mostrarCarreras(self):
        cadena = ''
        for i in range(len(self.__carrera)):
            cadena += "\nDatos de carrera: \n {}".format(self.__carrera[i])
        return cadena

    def getCodigoFacultad(self):
        return self.__codigo
    
    def getNombreFacultad(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getTelefono(self):
        return self.__telefono
    
    def getNombredelaCarrera(self):
        return self.__carrera.getNombreCarrera()
    
    def agregarcarrera(self,carrera):
        self.__carrera.append(carrera)
    
