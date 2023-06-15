import json
from zope.interface import implementer
from claseNodo import Nodo
from claseInterfaz import Ejercicio6Interface
from claseNuevo import Nuevo
from claseUsado import Usado

@implementer(Ejercicio6Interface)
class Lista:
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0

    def __init__(self):
        self.__comienzo = None
        self.__actual = None

    def agregarElemento(self,vehiculo):
        if isinstance(vehiculo,object):
            nodo = Nodo(vehiculo)
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo = nodo
            self.__actual = nodo
            self.__tope +=1
        else:
            raise AttributeError
        
    def insertarElemento(self,elemento,pos):
        if pos == 0:
            self.agregarElemento(elemento)
        else:
            i = 0
            aux = self.__comienzo 
            anterior = self.__comienzo 
            while i < pos and aux != None:
                anterior = aux
                aux = aux.setSiguiente()
                i = i+1
            if pos == i:
                nodo = Nodo(elemento)
                anterior.setSiguiente(nodo)
                nodo.setSiguiente(aux)
                self.__tope += 1
            else:
                raise IndexError
            
    def getTope(self):
        return self.__tope
    
    def mostrarElemento(self,pos):
        if isinstance(pos,int):
            i = 0
            aux = self.__comienzo
            while i < pos and aux != None:
                aux = aux.setSiguiente()
                i += 1
            if pos == i:
                print("El elemento que está en la posición {} es: {}".format(i+1,aux.getDato().__class__.__name__))
            else:
                raise IndexError
            
    def buscarMarca(self,patente):
        if isinstance(patente,str):
            bandera = False
            aux = self.__comienzo
            while bandera == False and aux != None:
                if isinstance(aux.getDato(),Usado):
                    if aux.getDato().getPatente() == patente:
                        bandera = True
                        precio = int(input("Indique nuevo precio de venta: "))
                        aux.getDato().cambiarPrecioBase(precio)
                        aux.getDato().importeVenta()
                    else:
                        aux = aux.setSiguiente()
                else:
                    aux = aux.setSiguiente()
        else:
            print("Parametro ingresado incorrecto ")

    def economico(self):
        min = 999999
        aux = self.__comienzo
        retorno = None
        while aux != None:
            if aux.getDato().importeVenta() < min:
                min = aux.getDato().importeVenta()
                retorno = aux.getDato()
            aux = aux.setSiguiente()
        return retorno

    def toJSON(self):
        d = dict(
            __class__= self.__class__.__name__,
            Vehiculo = [Nodo.toJSON() for Nodo in self] 
        )
        return d
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.setSiguiente()
            return dato
