from claseDirector import IDirector
from claseDocente import Docente
from claseDocenteInvestigador import DocenteInvestigador
from claseInvestigador import Investigador
from clasePersonaldeApoyo import PersonaldeApoyo
from claseLista import Lista
from zope.interface import interface
from zope.interface import implementer

@implementer(IDirector)

class Menu:
    __op = 0

    def __init__(self):
        self.__op = 0

    def item1(self,manejadorDirector: IDirector):
        cuil = input("Ingrese cuil: ")
        sueldoBasico = input("Ingrese nuevo sueldo basico: ")
        manejadorDirector.modificarBasico(cuil,sueldoBasico)
    
    def item2(self,lista,manejadorDirector: IDirector):
        cuil = input("Ingrese cuil: ")
        porcentaje = int(input("Ingrese nuevo porcentaje: "))
        manejadorDirector.modificarPorcentajeporcargo(cuil,porcentaje)

    def item3(self,lista,manejadorDirector: IDirector):
        cuil = input("Ingrese cuil: ")
        porcentaje = int(input("Ingrese nuevo porcentaje: "))
        manejadorDirector.modificarPorcentajeporcategoría(cuil,porcentaje)


    def item4(self,lista,manejadorDirector: IDirector):
        cuil = input("Ingrese cuil: ")
        importe = int(input("Ingrese nuevo importe: "))
        manejadorDirector.modificarImporteExtra(cuil,importe)

    def mostrarMenu(self,lista,opcion):
        if type(lista) == Lista:
                self.__op = opcion

                if self.__op == 1:
                    self.item1(lista)

                elif self.__op == 2:
                    self.item2(lista)

                elif self.__op == 3:
                    self.item3(lista)

                elif self.__op == 4:
                    self.item4(lista)

                elif self.__op == 5:
                    print("-----------Menú cerrado---------")
                    band = False
