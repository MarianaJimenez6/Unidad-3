from clasePersonal import Personal

class Docente(Personal):
    __carrera = None
    __cargo = None
    __catedra = None

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.__carrera = kwargs['carrera']
        self.__cargo = kwargs['cargo']
        self.__catedra = kwargs['catedra']

    def getCarrera(self):
        return self.__carrera
    
    def getCargo(self):
        return self.__cargo
    
    def getCatedra(self):
        return self.__catedra
    
    def mostrarDatos(self):
        super().mostrarDatos()
        print("Docente ")
    
    def mostrarSueldo(self):
        antigüedad = (self.getSueldoBasico() * ((self.getAntigüedad() / 5)*5)) / 100
        sueldoBasico = self.getSueldoBasico() + antigüedad
        if self.__cargo == 'simple':
            sueldoBasico += self.getSueldoBasico() + 0.10
        elif self.__cargo == 'semiexclusivo':
            sueldoBasico += self.getSueldoBasico() + 0.20
        elif self.__cargo == 'exclusivo':
            sueldoBasico += self.getSueldoBasico() + 0.50
        print("Sueldo basico de Docente: ",sueldoBasico)
        return sueldoBasico

    def toJSON(self):
        d = dict(
            __class__ = __class__.__name__,
            __atributos__ = dict(
            cuil = super().getCuil(),
            apellido = super().getApellido(),
            nombre = super().getNombre(),
            sueldo = super().getSueldoBasico(),
            antigüedad = super().getAntigüedad(),
            carrera = self.__carrera,
            cargo = self.__cargo,
            catedra = self.__catedra
            )
        )
        return d

    def __str__(self):
        return "Carrera en la que dicta clases: %s, Cargo: %s, Catedra: %s"%(self.__carrera,self.__cargo,self.__catedra)
    