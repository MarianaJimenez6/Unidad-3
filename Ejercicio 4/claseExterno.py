from claseEmpleado import Empleado

class EmpleadoExterno(Empleado):
    __tarea = None
    __fecha_inicio_tarea = None
    __fecha_fin_tarea = None
    __monto_viatico = None
    __costo_obra = None
    __seguro_vida = None

    def __init__(self,dni,nombre,direccion,telefono,tarea,fecha_inicio,fecha_fin,monto,costo,seguro):
        super().__init__(dni,nombre,direccion,telefono)
        self.__tarea = tarea
        self.__fecha_inicio_tarea = fecha_inicio
        self.__fecha_fin_tarea = fecha_fin
        self.__monto_viatico = monto
        self.__costo_obra = costo
        self.__seguro_vida = seguro

    def getTarea(self):
        return self.__tarea
    
    def getFechaInicioTarea(self):
        return self.__fecha_inicio_tarea
    
    def getFechaFinTarea(self):
        return self.__fecha_fin_tarea
    
    def getMontoViatico(self):
        return self.__monto_viatico
    
    def getCostoObra(self):
        return self.__costo_obra
    
    def getSegurodeVida(self):
        return self.__seguro_vida
    
    def calcularSueldo(self):
        sueldo = self.__costo_obra - self.__monto_viatico - self.__seguro_Vida
        return sueldo
    
    def __str__(self):
        return "Tarea: %s, Fecha de inicio de tarea: %s, Fecha de fin de tarea: %s, Monto del viatico: %s, Costo de la obra: %s, Seguro de vida: %s"%(self.__tarea,self.__fecha_inicio_tarea,self.__fecha_fin_tarea,self.__monto_viatico,self.__costo_obra,self.__seguro_vida)