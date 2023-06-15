from claseLista import Lista
from claseNuevo import Nuevo
from claseObjectEncoder import ObjectEncoder
from claseUsado import Usado


class Menu:
    __op = 0
    def __init__(self):
        self.__op = 0

    def item1(self,facultades):
        cod = input("Ingrese codigo de facultad: ")
        facultades.buscarCodigo(cod)

    def item2(self,facultades):
        nom = input("Ingrese nombre de carrera: ")
        facultades.buscarCarrera(nom)
    
    def mostrarMenu(self,lista,):
        if type(facultades) == ManejaFacultades:
            band = False
            print("-------Menu de opciones-------")
            while not band:
                print("\n")
                print("1- Para el código ingresado de una facultad, mostrar nombre de la facultad,y nombre  y duración de las carreras que se dictan en esa facultad.")
                print("2- Para el nombre ingresado de una carrera, mostrar código, nombre y localidad de la facultad donde esta se dicta.")
                print("3- c. Obtener un listado de alumnos ordenado: por el año que cursan y alfabéticamente por apellido y nombre (ambos de menor a mayor). ")
                print("3- Salir")
                self.__op = int(input("Seleccione una opcion: "))

                if self.__op == 1:
                    self.item1(facultades)
                    
                elif self.__op == 2:
                    self.item2(facultades)

                elif self.__op == 3:
                    self.item3(facultades)
                    
                elif self.__op == 4:
                    print("----Menu cerrado----")
                    band = True