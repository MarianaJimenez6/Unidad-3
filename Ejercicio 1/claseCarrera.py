
class Carrera:
    __codigo = None
    __nombre = None
    __fecha_inicio = None
    __duracion = None
    __titulo = None

    def __init__(self,codigo,nombre,fecha,duracion,titulo):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__fecha_inicio = fecha
        self.__duracion = duracion
        self.__titulo = titulo

    def __str__(self):
        return "Codigo: {}, Nombre: {}, Fecha de inicio: {}, Duracion: {}, Titulo: {}".format(self.__codigo,self.__nombre,self.__fecha_inicio,self.__duracion,self.__titulo)

    def getCodigoCarrera(self):
        return self.__codigo
    
    def getNombreCarrera(self):
        return self.__nombre
    
    def getFecha(self):
        return self.__fecha_inicio
    
    def getDuracion(self):
        return self.__duracion
    
    def getTitulo(self):
        return self.__titulo