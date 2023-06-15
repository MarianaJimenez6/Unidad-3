from claseInscripcion import Inscripcion
from claseTallerCapacitacion import TallerCapacitacion as Taller
import numpy as np

class ColeccionInscripcion:
    __cantidad = 0
    __dimension = 0
    __incremento = 5
    __inscripciones = None
    
    def __init__(self, dimension, incremento=5):
        self.__inscripciones = np.empty(dimension, dtype=Inscripcion)
        self.__cantidad = 0
        self.__dimension = dimension
    def agregarPunto(self, unaInscripcion):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__inscripciones.resize(self.__dimension)
            self.__inscripciones[self.__cantidad]=unaInscripcion
            self.__cantidad += 1

    def inscribirPersona(self,cod):
        pass

    def consultarInscripcion(self,dni): #item2
        #Ingresar el DNI de una persona, si está inscripta,
        # mostrar el nombre del taller en el que se inscribió y el monto que adeuda.
        i = 0
        band = False
        while i < len(self.__inscripciones):
            persona = persona.getPersona()
            if persona.getDNI() == dni:
                self.__inscripciones[i].getTaller().mostrarTalleres()
                if self.__inscripciones[i].getPago() == False:
                    print("Monto adeudado: {}".format(self.__inscripciones[i].getTaller().getMontoInscripcion()))
                    i += 1
                else:
                    print("No adeuda inscripción ")
            else:
                i = i+1

    def registrarPagoDNI(self,dni): #item4
        i=0
        bandera = False
        while i<self.__cantidad:
            persona = self.__arreglo[i].Getpersona()
            if dni == persona.getdni():
                self.__arreglo[i].Gettaller().mostrartaller()
                if self.__arreglo[i].Getpago() == False:
                    print("El mondo adeudado es de :{}".format(self.__arreglo[i].Gettaller().getmontoinscripcion()))
                    i=i+1
                else:
                    print("La persona no Adeuda inscripcion")
                    i=i+1
            else:
                i=i+1

    def guardarenArchivo(self): #item 5
        lista =[]
        for i in range(self.__cantidad):
            lista2 = [self.__arreglo[i].Getpersona().getdni(),self.__arreglo[i].Gettaller().Getcodtaller(),self.__arreglo[i].getfecha(),self.__arreglo[i].Getpago()]
            lista.append(lista2)
            lista2 = []
        np.savetxt("Inscripciones.csv", lista, delimiter =",",fmt ='% s')
        return
        

