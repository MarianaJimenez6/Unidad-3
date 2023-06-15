from claseDocente import Docente
from claseDocenteInvestigador import DocenteInvestigador
from claseInvestigador import Investigador
from clasePersonaldeApoyo import PersonaldeApoyo
from claseLista import Lista

class Menu:
    __op = 0

    def __init__(self):
        self.__op = 0

    def item1(self,lista,jsonF):
        posicion = int(input("Posicion en la que se desea guardar al nuevo agente: "))
        print("Agente a guardar: Investigador ")
        dic = { 'cuil' : '241112552','apellido' : 'Gomez', 'nombre':'Sonia','sueldoBasico': '80000','antigüedad': '6',
            'areaInvestigacion': 'Informatica', 'tipoInvestigacion': 'academico'}
        unAgente = Investigador(**dic)
        try:
            lista.insertarElemento(unAgente,posicion)
        except IndexError:
            print("Posicion ingresada erronea")

    
    def item2(self,lista,jsonF):
        print("1- Docente")
        print("2- Docente Investigador")
        print("3- Investigador")
        print("4- Personal de Apoyo")
        opcionAgente = int(input("Seleccione tipo de agente a agregar a la coleccion: "))
        if opcionAgente == 1:
            dic = {'cuil' : '31222525','apellido' : 'Villanueva', 'nombre':'Patricio','sueldoBasico': '90000','antigüedad': '15',
            'carrera': 'LCC', 'cargo': 'Titular', 'catedra': 'Programacion procedural'}
            unAgente = Docente(**dic)
            lista.agregarElemento(unAgente)

        elif opcionAgente == 2:
            dic = {'cuil' : '28777541','apellido' : 'Zarate', 'nombre':'Amalia','sueldoBasico': '90000','antigüedad': '7',
            'carrera': 'Biologia', 'cargo' : 'JTP', 'catedra':'Biologia 2','areaInvestigacion': 'Ciencias', 'tipoInvestigacion': 'academico'
            }
            unAgente = DocenteInvestigador(**dic)
            lista.agregarElemento(unAgente)

        elif opcionAgente == 3:
            dic = {'cuil' : '12554898','apellido' : 'Arancibia', 'nombre':'Sara','sueldoBasico': '100000','antigüedad': '20',
            'areaInvestigacion': 'Ciencias', 'tipoInvestigacion': 'academico'
            }
            unAgente = Investigador(**dic)
            lista.agregarElemento(unAgente)

        elif opcionAgente == 4:
            dic = {'cuil' : '34255522','apellido' : 'Gutierrez', 'nombre':'Fernando','sueldoBasico': '60000','antigüedad': '12',
            'categoria': '2'
            }
            unAgente = PersonaldeApoyo(**dic)
            lista.agregarElemento(unAgente)

        else:
            print("Opcion incorrecta ")
    
    def item3(self,lista,jsonF):
        pos = int(input("Ingrese la posicion para indicar el tipo de agente que se encuentra ahi"))
        try:
            lista.mostrarElemento(pos)
        except IndexError:
            print("Posicion no valida: numero incorrecto o no contiene agente")

    def item4(self,lista,jsonF):
        carrera = input("Ingrese una carrera")
        lista.ordenar()
        lista.listadoPorCarrera(carrera)

    def item5(self,lista,jsonF):
        try:
            lista.listarDatosAgente("informatica")
        except IndexError:
            print("No hay agentes en el area de informatica")

    def item6(self,lista,jsonF):
        lista.ordenarPorApellido()
        lista.obtenerSueldo()

    def item7(self,lista,jsonF):
        categoria = int("Elija categoria: I, II, III, IV, V")
        lista.mostrarSueldos(categoria)

    def item8(self,lista,jsonF):
        d = lista.toJSON()
        jsonF.guardarJSONArchivo(d,'personal.json')

    def item9(self,lista,jsonF):
        for dato in lista:
            print(dato)
    
    def mostrarMenu(self,lista,jsonF):
        if type(lista) == Lista:
            band = True
            print("-------Menu de opciones-------")
            while band == True:
                print("\n")
                print("1- Insertar a agentes a la colección. ")
                print("2- Agregar agentes a la colección. ")
                print("3- Dada una posición de la lista: Mostrar por pantalla que tipo de agente se encuentra almacenado alli. ")
                print("4- Ingresar por teclado el nombre de una carrera y mostrar los datos ordenados de los agentes que son docentes investigadores. ")
                print("5- Dada un area de investigación, contar a los docentes investigadores y los investigadores que trabajen en ese área. ")
                print("6- Generar un listado que muestre nombre y apellido, tipo de Agente y sueldo de todos los agentes, ordenado por apellido.")
                print("7- Dada una categoría de investigación, mostrar el total de dinero que la Secretaría de Investigación debe solicitar al Ministerio para cubrir el importe extra de esos docentes investigadores")
                print("8- Almacenar los datos de todos los agentes en el archivo “personal.json”. ")
                print("9- Mostrar los datos generados. ")
                print("10- Salir.")
                self.__op = int(input("Seleccione una opcion: "))

                if self.__op == 1:
                    self.item1(lista,jsonF)

                elif self.__op == 2:
                    self.item2(lista,jsonF)

                elif self.__op == 3:
                    self.item3(lista,jsonF)

                elif self.__op == 4:
                    self.item4(lista,jsonF)
                
                elif self.__op == 5:
                    self.item5(lista,jsonF)

                elif self.__op == 6:
                    self.item6(lista,jsonF)

                elif self.__op == 7:
                    self.item7(lista,jsonF)

                elif self.__op == 8:
                    self.item8(lista,jsonF)

                elif self.__op == 9:
                    self.item9(lista,jsonF)

                elif self.__op == 10:
                    print("-----------Menú cerrado---------")
                    band = False
