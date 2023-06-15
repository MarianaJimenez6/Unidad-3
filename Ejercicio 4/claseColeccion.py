from claseEmpleado import Empleado
from claseContratado import EmpleadoContratado as Contratado
from claseExterno import EmpleadoExterno as Externo
from clasePlanta import EmpleadoPlanta as Planta
import csv
import datetime
import numpy as np

class Coleccion:
   __cantidad = 0
   __dimension = 0
   __incremento = 5
   __empleados=None

   def __init__(self, dimension, incremento=5):
      self.__empleados = np.empty(dimension, dtype=Empleado)
      self.__cantidad = 0
      self.__dimension = dimension
   
   def agregarEmpleado(self, unEmpleado):
      if self.__cantidad==self.__dimension:
         self.__dimension+=self.__incremento
         self.__empleados.resize(self.__dimension)
         self.__empleados[self.__cantidad]=unEmpleado
         self.__cantidad += 1

   def cargarPlanta(self):
      archivo = open('planta.csv')
      reader = csv.reader(archivo,delimiter=",")
      band = True
      for fila in reader:
         if band:
            band = not band #saltea cabecera
         else:
            DNI = fila[0]
            nombre = fila[1]
            direccion = fila[2]
            telefono = fila[3]
            sueldoBasico = fila[4]
            antigüedad = fila[5]
            empleadoPlanta= Planta(DNI,nombre,direccion,telefono,sueldoBasico,antigüedad)
            self.agregarEmpleado(empleadoPlanta)
      archivo.close()

   def cargarContratado(self):
      archivo = open('contratados.csv')
      reader = csv.reader(archivo,delimiter=",")
      band = True
      for fila in reader:
         if band:
            band = not band #saltea cabecera
         else:
            DNI = fila[0]
            nombre = fila[1]
            direccion = fila[2]
            telefono = fila[3]
            fecha_inicio_contrato = fila[4]
            fecha_fin_contrato = fila[5]
            horas_trabajadas = fila[6]
            valor_hora = fila[7]
            empleadoContratado= Contratado(DNI,nombre,direccion,telefono,fecha_inicio_contrato,fecha_fin_contrato,horas_trabajadas,valor_hora)
            self.agregarEmpleado(empleadoContratado)
      archivo.close()

   def cargarExterno(self):
      archivo = open('externos.csv')
      reader = csv.reader(archivo,delimiter=",")
      band = True
      for fila in reader:
         if band:
            band = not band #saltea cabecera
         else:
            DNI = fila[0]
            nombre = fila[1]
            direccion = fila[2]
            telefono = fila[3]
            tarea = fila[4]
            fecha_inicio_tarea = fila[5]
            fecha_fin_tarea = fila[6]
            monto_viatico = fila[7]
            costo_obra = fila[8]
            seguro_vida = fila[9]
            empleadoExterno= Contratado(DNI,nombre,direccion,telefono,tarea,fecha_inicio_tarea,fecha_fin_tarea,monto_viatico,costo_obra,seguro_vida)
            self.agregarEmpleado(empleadoExterno)
      archivo.close()

   def mostrarEmpleados(self):
      for empleado in self.__empleados:
         print(self.__empleados[empleado])

   def modificarHoras(self,dni,horas): #item1
      i = 0
      band = False
      while i < len(self.__empleados) and band == False:
         if isinstance(self.__empleados[i],Contratado):
            if self.__empleados[i].getDNI() == dni:
               self.__empleados[i].aumentarHoras(horas)
               horasActualizadas = self.__empleados[i].getHorasTrabajadas()
               band = True
               i = i+1
            else:
               i = i+1
         if i == len(self.__empleados):
            print("No se encontró el empleado con ese DNI ")
         else:
            print("Horas trabajadas actualizadas: ",horasActualizadas)

   def mostrarMonto(self,tarea): #item2
      #Sueldo = costo de la obra - viático- monto del seguro de vida
      i = 0
      while i < len(self.__empleados):
         if isinstance(self.__empleados[i],Externo):
            fecha_actual = datetime.date.today()
            if self.__empleados[i].getTarea() == tarea and self.__empleados[i].getFechaFinTarea() > fecha_actual:
               print(self.__empleados[i])
               costo_obra = self.__empleados[i].getCostoObra()
               viatico = self.__empleados[i].getMontoViatico()
               seguro_vida = self.__empleados[i].getSegurodeVida()
               sueldo = costo_obra - viatico - seguro_vida
               print("Monto a pagar por la tarea realizada: {}".format(sueldo))
            else:
               i = i+1
         else:
            i = i+1

   def ayudaEconomica(self): #item3
      for i in range(len(self.__empleados)):
            sueldo = self.__empleados.calcularSueldo()
            if sueldo < 150000:
               nombre = self.__empleados[i].getNombre()
               direccion = self.__empleados[i].getDireccion()
               dni = self.__empleados[i].getDNI()
               print("Al empleado {} con direccion {} y DNI {} le corresponde la ayuda económica. ".format(nombre,direccion,dni))

   def mostrarSueldo(self):#item4
      for i in range(len(self.__empleados)):
         nombre = self.__empleados[i].getNombre()
         telefono = self.__empleados[i].getTelefono()
         sueldo = self.__empleados[i].calcularSueldo()
         print("\nNombre: {}, Telefono: {}, sueldo: {}".format(nombre,telefono,sueldo))
