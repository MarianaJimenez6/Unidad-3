from clasePersonal import Personal

class PersonaldeApoyo(Personal):
    __categoria = None

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.__categoria = kwargs['categoria']

    def getCategoria(self):
        return self.__categoria
    
    def __str__(self):
        return "Categoria: %s"%(self.__categoria)
    
    def mostrarSueldo(self):
        antigüedad = (self.getSueldoBasico() * ((self.getAntigüedad() / 5)*5)) / 100
        sueldoBasico = self.getSueldoBasico() + antigüedad + (self.getSueldoBasico() * 0.10)
        print("Sueldo de personal de apoyo: ",sueldoBasico)
    
    def toJSON(self):
        d = dict(
            __class__ = __class__.__name__,
            __atributos__ = dict(
            cuil = super().getCuil(),
            apellido = super().getApellido(),
            nombre = super().getNombre(),
            sueldo = super().getSueldoBasico(),
            antigüedad = super().getAntigüedad(),
            categoria = self.__categoria
            )
        )
        return d