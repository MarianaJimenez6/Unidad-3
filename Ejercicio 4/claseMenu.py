from claseColeccion import Coleccion

class Menu:
    __op = 0

    def __init__(self):
        self.__op = 0

    def item1(self,empleados):
        dni = input("Ingrese DNI del empleado: ")
        horas = input("Indique cantidad de horas trabajadas: ")
        empleados.modificarHoras(dni,horas)
    
    def item2(self,empleados):
        tarea = input("Indique una tarea no finalizada: ")
        empleados.mostrarMonto(tarea)
    
    def item3(self,empleados):
        print("Empleados a los que se les otorga ayuda económica: ")
        empleados.ayudaEconomica()
    
    def item4(self,empleados):
        print("Sueldo de los empleados: ")
        empleados.mostrarSueldo()
    
    def mostrarMenu(self,empleados):
        if type(empleados) == Coleccion:
            band = True
            print("-------Menu de opciones-------")
            while band == True:
                print("\n")
                print("1- Registrar horas: Ingresar el DNI de un empleado y la cantidad de horas trabajadas en el día de la fecha e incrementar la cantidad de las horas trabajadas del empleado.")
                print("2- Total de tarea: Dada una tarea mostrar el monto a pagar para ella. Solo se consideran las tareas que no han finalizado.")
                print("3- Ayuda Económica: La empresa dará una ayuda solidaria a los empleados cuyo sueldo sea inferior a $150000; listar nombre, dirección y DNI de los empleados que les corresponde la ayuda.")
                print("4- Calcular sueldo: Mostrar nombre, teléfono y sueldo a cobrar de todos los empleados.")
                print("5- Salir. ")
                self.__op = int(input("Seleccione una opcion: "))

                if self.__op == 1:
                    self.item1(empleados)

                elif self.__op == 2:
                    self.item2(empleados)

                elif self.__op == 3:
                    self.item3(empleados)

                elif self.__op == 4:
                    self.item4(empleados)

                elif self.__op == 5:
                    print("-----------Menú cerrado---------")
                    band = False
