from clasePersona import Persona
from claseTallerCapacitacion import TallerCapacitacion

class Inscripcion:
    __fecha_inscripcion = None
    __pago = None
    __persona = object
    __taller = object

    def __init__(self,fecha,pago,persona,taller):
        self.__fecha_inscripcion = fecha
        self.__pago = pago
        self.__persona = persona
        self.__taller = taller

    def getFechaInscripcion(self):
        return self.__fecha_inscripcion
    
    def getPago(self):
        return self.__pago
    
    def getPersona(self):
        return self.__persona
    
    def getTaller(self):
        return self.__taller
    
    def cambiarPago(self):
        self.__pago = True
    
    def cambiarPagoPersona(self):
        self.__persona.cambiarPago()
    
    def __str__(self):
        cadena = 'Fecha de inscripcion: '+self.__fecha_inscripcion+'\n'
        cadena += 'Pago: '+self.__pago+'\n'
        cadena += str(self.__persona)
        cadena += str(self.__taller)
        return cadena