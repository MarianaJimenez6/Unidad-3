class Personal:
    __cuil = None
    __apellido = None
    __nombre = None
    __sueldoBasico = None
    __antigüedad = None

    def __init__(self,**kwargs):
        self.__cuil = kwargs['cuil']
        self.__apellido = kwargs['apellido']
        self.__nombre = kwargs['nombre']
        self.__sueldoBasico = int(kwargs['sueldoBasico'])
        self.__antigüedad = int(kwargs['antigüedad'])

    def getCuil(self):
        return self.__cuil
    
    def getApellido(self):
        return self.__apellido
    
    def getNombre(self):
        return self.__nombre
    
    def getSueldoBasico(self):
        return self.__sueldoBasico
    
    def getAntigüedad(self):
        return self.__antigüedad
    
    def mostrarDatos(self):
        return "Nombre: %s, Apellido: %s"%(self.__nombre,self.__apellido)
    
    def mostrarSueldo(self):
        pass
    
    def __str__(self):
        return "Cuil: %s, Apellido: %s, Nombre: %s, Sueldo basico: %s, Antigüedad: %s"%(self.__cuil,self.__apellido,self.__nombre,self.__sueldoBasico,self.__antigüedad)
    