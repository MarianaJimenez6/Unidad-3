from claseHelado import Helado
from claseSabor import Sabor

class Menu:
    __op = 0

    def __init__(self):
        self.__op = 0

    def item1(self,helados,sabores):
        print("Helados en gramos: ")
        print("100 gramos")
        print("150 gramos")
        print("250 gramos")
        print("500 gramos")
        print("1000 gramos")
        gramos = input("Seleccione los gramos: ")
        cantidad = int(input("Ingrese cantidad de sabores: "))
        codigo = int(input("Ingrese el código del sabor: "))
        helados.registrarHelado(gramos,cantidad,codigo,sabores)
    
    def item2(self,helados,sabores):
        helados.saboresMasPedidos(sabores)
    
    def item3(self,helados,sabores):
        cod = int(input("Ingrese codigo de helado para buscar: "))
        helados.totalGramos(sabores,cod)
    
    def item4(self,helados):
        tipoHelado = input("Ingrese tipo de helado: ")
        helados.saboresporTamanio(tipoHelado)
    
    def item5(self,helados):
        helados.totalRecaudado()
    
    def mostrarMenu(self,helados,sabores):
        if type(helados) == Helado:
            if type(sabores) == Sabor:
                band = False
                print-("----------Menu de opciones---------")
                while band == False:
                    print("1. Registrar un helado vendido")
                    print("2. Mostrar el nombre de los 5 sabores de helado más pedidos.")
                    print("3. Para un número de sabor ingresado, estimar el total de gramos vendidos.")
                    print("4. Para un tipo de helado ingresado  por teclado, mostrar los sabores vendidos en ese tamaño")
                    print("5. Determinar el importe total recaudado por la heladería, por cada tipo de helado.")
                    print("6. Salir.")
                    self.__op = int(input("Seleccione opcion: "))

                    if self.__op == 1:
                        self.item1(helados)
                    elif self.__op == 2:
                        self.item2(helados,sabores)           
                    elif self.__op == 3:
                        self.item3(helados,sabores)              
                    elif self.__op == 4:
                        self.item4(helados)
                    elif self.__op == 5:
                        self.item5(helados)
                    elif self.__op == 6:
                        print("-------Menu cerrado------")
                        band = True
                    else:
                        print("Opcion incorrecta. ")
