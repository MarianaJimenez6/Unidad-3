from clasePersonal import Personal

class Investigador(Personal):
    __area_investigacion = None
    __tipo_investigacion = None

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.__area_investigacion = kwargs['area']
        self.__tipo_investigacion = kwargs['tipo']

    def getAreaInvestigacion(self):
        return self.__area_investigacion
    
    def getTipoInvestigacion(self):
        return self.__tipo_investigacion
    
    def __str__(self):
        return "Area de investigacion: %s, Tipo de investigacion: %s"%(self.__area_investigacion,self.__tipo_investigacion)
    
    def toJSON(self):
        d = dict(
            __class__ = __class__.__name__,
            __atributos__ = dict(
            cuil = super().getCuil(),
            apellido = super().getApellido(),
            nombre = super().getNombre(),
            sueldo = super().getSueldoBasico(),
            antigüedad = super().getAntigüedad(),
            areaInvestigacion = self.__area_investigacion,
            tipoInvestigacion = self.__tipo_investigacion
            )
        )
        return d