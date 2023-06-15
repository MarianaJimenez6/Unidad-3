from clasePersonal import Personal
from claseDocente import Docente
from claseInvestigador import Investigador

class DocenteInvestigador(Docente,Investigador):
    __categoría_programa_investigación = None
    __importe_extra = None

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.__categoría_programa_investigación = int(kwargs['categoria'])
        self.__importe_extra = int(kwargs['importe'])

    def getCategoriaPrograma(self):
        return self.__categoría_programa_investigación
    
    def getImporteExtra(self):
        return self.__importe_extra
    
    def mostrarDatos(self):
        Personal.mostrarDatos(self)
        print("Docente Investigador")
        
    def mostrarSueldo(self):
        sueldo = super().mostrarSueldo() + self.__importe_extra
        print("sueldo del docente Investigador: ",sueldo)
    
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
            tipoInvestigacion = self.__tipo_investigacion,
            categoria = self.__categoría_programa_investigación,
            importe = self.__importe_extra
            )
        )
        return d
    
    def __str__(self):
        return "categoría en el programa de incentivos de investigación: %s, importe extra por docencia e investigación: %s "%(self.__categoría_programa_investigación,self.__importe_extra)