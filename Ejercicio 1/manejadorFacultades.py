from claseCarrera import Carrera
from claseFacultad import Facultad
import csv

class ManejaFacultades:
    __lista = []
    def __init__(self):
        self.__lista = []


    def leerArchivo(self):
        archivo = open('Facultades.csv')
        reader = csv.reader(archivo,delimiter=",")
        band = True
        for fila in reader:
            if band:
                band = not band #saltea cabecera
            else:
                if ("facultad" in fila[1].lower()):
                    codigo = fila[0]
                    nombre = fila[1]
                    direccion = fila[2]
                    localidad = fila[3]
                    telefono = fila[4]
                    unaFacultad = Facultad(codigo,nombre,direccion,localidad,telefono)
                    self.__lista.append(unaFacultad)
                    indice = int(fila[0])
                elif ("facultad" not in fila[1].lower()):
                    codigo = fila[0]
                    nombre = fila[1]
                    fecha_inicio = fila[2]
                    duracion = fila[3]
                    titulo = fila[4]
                    unaCarrera = Carrera(codigo,nombre,fecha_inicio,duracion,titulo)
                    self.__lista[indice-1].agregarcarrera(unaCarrera)
        archivo.close()

    def mostrarDatos(self):
        for i in range(len(self.__lista)):
            print("\n",self.__lista[i])

#Ingresar el código  de una facultad y mostrar nombre de la facultad, nombre  
# y duración de cada una de las carreras que se dictan en esa facultad.
    def buscarCodigo(self,cod):
        i = 0
        band = False
        while i < len(self.__lista) and band == False:
            if self.__lista[i].getCodigoFacultad() == cod:
                print("\nNombre de la facultad : %s \n"%(self.__lista[i].getNombreFacultad()))
                self.__lista[i].mostrarCarreras()
                band = True
            else:
                i = i+1

#Para el nombre ingresado de una carrera, mostrar código,
# nombre y localidad de la facultad donde esta se dicta.
    def buscarCarrera(self,nom):
        i = 0
        j = 0
        band = False
        while i < len(self.__lista)and band == False:
            listaCarreras = self.__lista[i].getNombredelaCarrera()
            while j < len(listaCarreras) and band == False:
                if listaCarreras[i].getNombredelaCarrera() == nom:
                    print("\n Código de la facultad: %s"%(self.__lista[i].getCodigoFacultad()))
                    print("Nombre de la facultad: %s"%(self.__lista[i].getNombreFacultad()))
                    print("Localidad de la facultad: %s"%(self.__lista[i].getDireccion()))
                    bandera = True
                else:
                    j = j+1
            i = i + 1
            j = 0 
            
    def __str__(self):
        for i in range(len(self.__lista)):
            print(self.__lista[i])