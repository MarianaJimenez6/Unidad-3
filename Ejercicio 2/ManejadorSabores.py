from claseSabor import Sabor
import csv

class ManejaSabores:
    __lista = []

    def __init__(self):
        self.__lista= []

    def agregarSabor(self,sabor1):
        self.__lista.append(sabor1)

    def leerArchivo(self):
        archivo = open('sabores.csv')
        reader = csv.reader(archivo,delimiter=",")
        band = True
        for fila in reader:
            if band:
                band = not band #saltea cabecera
            else:
                id_sabor = fila[0]
                nombre = fila[1]
                ingredientes = fila[2]
                sabor1 = Sabor(id_sabor,nombre,ingredientes)
                self.agregarSabor(sabor1)
        archivo.close()

    def mostrarSabores(self,indice):
        for i in range(len(self.__lista)):
            print(self.__lista[indice[i]].mostrarSabores())

    def buscarSabor(self,indice):
        return self.__lista[indice]

    def mostrarSabor(self,indice):
        print("sabor",self.__lista[indice-1])

