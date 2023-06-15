from claseEmpleado import Empleado

class EmpleadoPlanta(Empleado):
    __sueldoBasico = None
    __antigüedad = None

    def __init__(self,dni,nombre,direccion,telefono,sueldo,antigüedad):
        super().__init__(dni,nombre,direccion,telefono)
        self.__sueldoBasico = sueldo
        self.__antigüedad = antigüedad

    def getSueldoBasico(self):
        return self.__sueldoBasico 
    
    def getAntigüedad(self):
        return self.__antigüedad
    
    def calcularSueldo(self):
        sueldo = (self.__sueldoBasico+ (self.__sueldoBasico*0.1)* self.__antigüedad)
        return sueldo
    
    def __str__(self):
        return "Sueldo basico: %s, Antigüedad: %s "%(self.__sueldoBasico,self.__antigüedad)

