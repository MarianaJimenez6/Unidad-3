from claseEmpleado import Empleado

class EmpleadoContratado(Empleado):
    __fecha_inicio_contrato = None
    __fecha_fin_contrato = None
    __horas_trabajadas = None
    __valor_hora = 50

    def __init__(self,dni,nombre,direccion,telefono,fecha_inicio,fecha_fin,horas,valorhora):
        super().__init__(dni,nombre,direccion,telefono)
        self.__fecha_inicio_contrato = fecha_inicio
        self.__fecha_fin_contrato = fecha_fin
        self.__horas_trabajadas = horas
        self.__valor_hora = valorhora

    def getFechaInicioContrato(self):
        return self.__fecha_inicio_contrato
    
    def getFechaFinContrato(self):
        return self.__fecha_fin_contrato
    
    def getHorasTrabajadas(self):
        return self.__horas_trabajadas
    
    def getValorHora(self):
        return self.__valor_hora
    
    def aumentarHoras(self,horas):
        self.__horas_trabajadas += horas

    def calcularSueldo(self):
        sueldo = self.__horas_trabajadas * self.__valor_hora
        return sueldo
    
    def __str__(self):
        return "Fecha de inicio de contrato: %s, Fecha de fin de contrato: %s, Horas trabajadas: %s, Valor de hora: %s "%(self.__fecha_inicio_contrato,self.__fecha_fin_contrato,self.__horas_trabajadas,self.__valor_hora)
    