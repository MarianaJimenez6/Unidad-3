from ColeccionInscripcion import ColeccionInscripcion
from ColeccionPersona import ColeccionPersona
from manejadorTalleres import ManejadorTalleres

class Menu:
    __op = 0
    def __init__(self):
        self.__op = 0

    def item1(self,inscripciones):
        cod = input("Ingrese codigo de facultad: ")
        inscripciones.inscribirPersona(cod)

    def item2(self,inscripciones):
        dni = input("Ingrese DNI de la persona: ")
        inscripciones.consultarInscripcion(dni)

    def item3(self,talleres):
        idTaller = input("Ingrese el identificador de un taller: ")
        talleres.consultarInscriptos(idTaller)

    def item4(self,inscripciones):
        dni = input("Ingrese DNI de la persona:")
        inscripciones.registrarPagoDNI(dni)

    def item5(self,inscripciones):
        inscripciones.guardarenArchivo()

    def mostrarMenu(self,inscripciones,personas,talleres):
        if type(inscripciones) == ColeccionInscripcion:
            if type(personas) == ColeccionPersona:
                band = False
                print("-------Menu de opciones-------")
                while not band:
                    print("\n")
                    print("1-  Inscribir una persona en un taller.")
                    print("2- Consultar inscripción: Ingresar el DNI de una persona, si está inscripta mostrar el nombre del taller en el que se inscribió y el monto que adeuda.")
                    print("3- Consultar inscriptos: Ingresar el identificador de un taller y listar los datos de los alumnos que se inscribieron en él.")
                    print("4- Registrar pago: Ingresar el DNI de una persona y registrar el pago (dar al atributo pago el valor True).")
                    print("5- Guardar inscripciones: Generar un nuevo archivo que contenga los siguientes datos de las inscripciones: DNI de la persona, idTaller, fechaInscripcion y pago")
                    print("6- Salir")
                    self.__op = int(input("Seleccione una opcion"))

                    if self.__op == 1:
                        self.item1(inscripciones)

                    elif self.__op == 2:
                        self.item2(inscripciones)

                    elif self.__op == 3:
                        self.item3(talleres)

                    elif self.__op == 4:
                        self.item4(inscripciones)

                    elif self.__op == 5:
                        self.item5(inscripciones)

                    elif self.__op == 6:
                        print("----Menu cerrado----")
                        band = True