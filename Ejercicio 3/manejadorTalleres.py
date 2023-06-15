from claseTallerCapacitacion import TallerCapacitacion
from claseInscripcion import Inscripcion
import csv
import numpy as np

class ManejadorTalleres:
   __cantidad = 0
   __dimension = 0
   __incremento = 5
   __talleres=None

   def __init__(self, dimension, incremento=5):
      self.__talleres = np.empty(dimension, dtype=TallerCapacitacion)
      self.__cantidad = 0
      self.__dimension = dimension
   
   def agregarTaller(self, unTaller):
      if self.__cantidad==self.__dimension:
         self.__dimension+=self.__incremento
         self.__talleres.resize(self.__dimension)
         self.__talleres[self.__cantidad]=unTaller
         self.__cantidad += 1

   def leerTalleres(self):
      archivo = open('Talleres.csv')
      reader = csv.reader(archivo,delimiter=",")
      band = True
      for fila in reader:
         if band:
            band = not band #saltea cabecera
         else:
            idTaller = fila[0]
            nombre = fila[1]
            vacantes = fila[2]
            montoInscripcion = fila[3]
            unTaller= TallerCapacitacion(idTaller,nombre,vacantes,montoInscripcion)
            self.agregarTaller(unTaller)
      archivo.close()

   def mostrarTalleres(self):
      for i in range(len(self.__talleres)):
         print(self.__talleres[i])

   def inscribirPersona(self,persona,fecha,arregloInscripciones):
      self.mostrarDatos()
      codigoTaller = int(input("Elija el codigo del taller a inscribirse: "))
      pago = False
      if self.__arreglo[codigoTaller-101].Getvacantes() == 0:
         print("No hay vancantes para el taller elejido")
      else:
         unainscripcion = Inscripcion(fecha,pago,persona,self.__arreglo[codigoTaller-101])
         arregloInscripciones.guardainscripcion(unainscripcion)
         self.__arreglo[codigoTaller-101].nuevainscripcion(unainscripcion)
         self.__arreglo[codigoTaller-101].modificarvacante()

   def consultarInscriptos(self,idTaller): #3
      i = 0
      bandera = False
      while i < self.__cantidad and bandera == False:
         taller = self.__talleres[i]
         if idTaller == taller.getIdTaller():
            taller.mostrarPersonas()
            bandera = True
         i = i+1

