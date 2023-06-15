from claseDocente import Docente
from claseDocenteInvestigador import DocenteInvestigador
from claseInvestigador import Investigador
from claseNodo import Nodo
from clasePersonal import Personal
from clasePersonaldeApoyo import PersonaldeApoyo

class Lista:
    __comienzo = Nodo
    __actual: Nodo
    __indice: int
    __tope: int

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0

    def agregarElemento(self,elemento):
        nodo = Nodo(elemento)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo

    def insertarElemento(self,elemento,posicion):
        if posicion == 0:
            self.agregarElemento(elemento)
        else:
            i = 0
            aux = self.__comienzo
            anterior = self.__comienzo
            while i < posicion and aux != None:
                anterior = aux
                aux = aux.getSiguiente()
                i = i+1
            if posicion == i:
                nodo = Nodo(elemento)
                anterior.setSiguiente(nodo)
                nodo.setSiguiente(aux)
                self.__tope += 1
            else:
                raise IndexError

    #metodo de la clase ITesorero
    def gastosSueldoPorEmpleado(self, cuil):
        i = 0
        tope = self.__tope
        aux = self.__comienzo
        while i < tope and aux != None:
            if cuil == aux.getDato().getcuil():
                aux.getDato().mostrarsueldo()
                i = tope
            else:
                i=i+1
                aux = aux.getSiguiente()


    #metodos de  la clased IDirector
    def modificarBasico(self,cuil,nuevobasico):
        i = 0
        aux = self.__comienzo
        bandera = False
        while not bandera and aux != None:
            if cuil == aux.getDato().getcuil():
                print("Basico actual:", aux.getDato().getbasico())
                aux.getDato().modificarbasico(nuevobasico)
                print("___Basico cambiado___")
                print("Nuevo Basico:",aux.getDato().getbasico())
                bandera = True
            else:
                aux = aux.getSiguiente()
        if bandera == False:
            print("Agente no encontrado")
        return

    def modificarPorcentajeporcargo(self,cuil,nuevoPorcentaje):
        aux = self.__comienzo
        bandera = False
        while not bandera and aux != None:
            if cuil == aux.getDato().getcuil() and isinstance(aux.getDato(),Docente):
                print("Porcentaje Actual: ",aux.getDato().getporcentaje())
                aux.getDato().cambiarporcentaje(nuevoPorcentaje)
                print("___Porcentaje cambiando___")
                print("Nuevo porcentaje:",aux.getDato().getporcentaje())
                bandera = True

            else:
                aux = aux.getSiguiente()

        if bandera == False:
            print("Docente no encontrado")
        return

    def modificarPorcentajeporcategoria(self,cuil,nuevoPorcentaje):
        aux = self.__comienzo
        bandera = False
        while not bandera and aux != None:
            if cuil == aux.getDato().getcuil() and isinstance(aux.getDato(),Apoyo):
                print("Porcentaje Actual: ",aux.getDato().getporcentaje())
                aux.getDato().cambiarporcentaje(nuevoPorcentaje)
                print("___Porcentaje cambiando___")
                print("Nuevo porcentaje:",aux.getDato().getporcentaje())
                bandera = True
            else:
                aux = aux.getSiguiente()
        if bandera == False:
            print("Agente no encontrado")
        return

    def modificarImporteExtra(self,cuil,nuevoImporteExtra):
        i = 0
        aux = self.__comienzo
        bandera = False
        while not bandera and aux != None:
            if cuil == aux.getDato().getcuil() and isinstance(aux.getDato(),DocenteInvestigador):
                aux.getDato().cambiarimporteextra(nuevoImporteExtra)
                print("___Porcentaje cambiando___")
                bandera = True
            else:
                aux = aux.getSiguiente()
        if bandera == False:
            print("Agente no encontrado")
        return
            
    def getTope(self):
        return self.__tope
        
    def mostrarElemento(self,posicion):
        if isinstance(posicion,int):
            i = 0
            aux = self.__comienzo
            while i < posicion and aux != None:
                aux = aux.getSiguiente()
                i +=1
            if posicion == i:
                print(aux.getDato())
            else:
                raise IndexError
            
    def ordenarPorApellido(self):
        cabeza = self.__comienzo
        cota = None
        k = None
        while k != cabeza:
            k = cabeza
            p = cabeza
            while p.getSiguiente() != cota:
                siguiente = p.getSiguiente()
                siguiente = p.getDato()
                if p.getDato().getApellido() > siguiente().getApellido():
                    aux = p.getSiguiente().getDato()
                    siguiente.setDato(p.getDato())
                    p.setDato(aux)
                    k = p
                else:
                    p = p.getSiguiente()
            cota = k.getSiguiente()

    def listadoPorCarrera(self,carrera):
        if type(carrera) == str:
            i = 0
            aux = self.__comienzo
            tope = self.__tope
            while i < tope and aux != None:
                if isinstance(aux.getDato(),DocenteInvestigador) and aux.getDato().getCarrera() == carrera:
                    print(aux.getDato())
                    aux = aux.getSiguiente()
                    i = i+1
                else:
                    aux = aux.getSiguiente()
                    i = i+1

    def listarDatosAgente(self,area):
        aux = self.__comienzo
        i = 0
        cantInvestigadores = 0
        cantDocentesInv = 0
        tope = self.__tope
        while i < tope and aux != None:
            if isinstance(aux.getDato(),DocenteInvestigador) and aux.getDato().getAreaInvestigacion() == area:
                cantDocentesInv += 1
                aux = aux.getSiguiente()
                i = i+1
            elif isinstance(aux.getDato(),Investigador) and aux.getDato().getAreaInvestigacion() == area:
                cantInvestigadores += 1
                aux = aux.getSiguiente()
                i = i+1
            else:
                aux = aux.getSiguiente()
                i = i+1
        print("Cantidad de docentes investigadores en el area {} es: {}".format(area,cantDocentesInv))
        print("Cantidad de investigadores en el area {} es: {}".format(area,cantInvestigadores))

    def mostrarSueldos(self,categoria):
        i = 0
        tope = self.__tope
        aux = self.__comienzo
        sueldoTotal = 0
        while i < tope and aux != None:
            if isinstance(aux.getDato(),DocenteInvestigador) and aux.getDato().getCategoria() == categoria:
                print(aux.getDato().mostrarDatos())
                print("Importe extra por docencia e investigacion: {}".format(aux.getDato().getImporteExtra()))
                sueldoTotal += aux.getDato().getImporteExtra()
                i += 1
                aux = aux.getSiguiente()
            else:
                i += 1
                aux = aux.getSiguiente()
        print("Total de dinero que la Secretaría de Investigación debe solicitar al Ministerio es: ",sueldoTotal)

    def ordenar(self):
        cabeza = self.__comienzo
        cota = None
        k = None
        while k != cabeza:
            k = cabeza
            p = cabeza
            while p.getSiguiente() != cota:
                if p.getDato().getNombre() > p.getSiguiente().getDato().getNombre():
                    aux = p.getSiguiente().getDato()
                    p.setSiguiente().setDato(p.getDato())
                    p.setDato(aux)
                    k = p
                else:
                    p = p.getSiguiente()
            cota = k.getSiguiente() 

    def obtenerSueldo(self):
        aux = self.__comienzo
        while aux != None:
            aux.getDato()
            aux.getDato().getSueldoBasico()
            aux = aux.getSiguiente()

    def toJSON(self):
        d = dict(
        __class__ = self.__class__.__name__,
        Personal = [nodo.toJSON() for nodo in self]
        )
        return d
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual == self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice +=1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato

