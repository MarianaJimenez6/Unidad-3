class TallerCapacitacion:
    __idTaller = None
    __nombre = None
    __vacantes = None
    __montoInscripcion = None
    __lista = []

    def __init__(self,idTaller,nom,vacantes,monto):
        self.__idTaller = idTaller
        self.__nombre = nom
        self.__vacantes = vacantes
        self.__montoInscripcion = monto
        self.__lista = []

    def getIdTaller(self):
        return self.__idTaller
    
    def getNombre(self):
        return self.__nombre
    
    def getVacantes(self):
        return self.__vacantes
    
    def getMontoInscripcion(self):
        return self.__montoInscripcion
    
    def nuevaInscripcion(self,inscripcion):
        self.__lista.append(inscripcion)

    def modificarVacante(self):
        self.__vacantes -= 1
    
    def mostrarPersonas(self):
        i = 0
        while i < len(self.__lista):
            persona = self.__lista[i].getPersona()
            print(persona)
            i = i+1
    
    def __str__(self):
        return "Id de Taller: %s, Nombre: %s, Vacantes: %s, Monto de la inscripcion: %s"%(self.__idTaller,self.__nombre,self.__vacantes,self.__montoInscripcion)
    
