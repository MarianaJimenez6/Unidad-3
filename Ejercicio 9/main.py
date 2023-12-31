'''Ejercicio 6
Descripción del sistema
La concesionaria de automóviles “TuAuto.com” se dedica a la venta de vehículos nuevos y usados. Para ello cuenta con un archivo, "vehiculos.json", con la estructura necesaria para almacenar vehículos nuevos y vehículos usados.    
De cada vehículo desea registrar el modelo (ej. Palio, Focus, etc.), cantidad de puertas, color y el precio base de venta. Los vehículos nuevos son de una misma marca, en cambio los usados pueden ser de cualquier marca, por ello este también es un dato que debe registrar.
Además, para los usados se registrará la patente, el año y el kilometraje.
De un vehículo nuevo también registra la versión (base o full).
El importe de venta de cada vehículo se calcula en función del precio base y de sus características. Para ello se deben considerar las siguientes reglas de negocio:
Importe de venta del vehículo usado es el precio base, menos el 1% por cada año de antigüedad (año actual – año del vehículo), menos el 2% si el kilometraje supera los 100.000. Ambos porcentajes se calculan sobre el precio base.
Importe de venta del vehículo nuevo es el precio base, más 10% por gastos de patentamiento, mas 2% si es full. Ambos porcentajes se calculan sobre el precio base.
El analista del concesionario, le solicita a usted que desarrolle una aplicación, con las siguientes restricciones:    
La colección de vehículos debe implementarse usando una Lista definida por el programador, donde los nodos deberán almacenar vehículos.
La Lista deberá proveer los métodos y atributos necesarios para que sea un iterable, e implementar la     interface del ejercicio anterior.
Para cumplir con lo solicitado por el analista, usted deberá:
a)  Definir la jerarquía de clases correspondiente a la problemática planteada.    
b) Leer y procesar el archivo “vehiculos.json” para almacenar en la Lista los vehículos de la concesionaria.    
c) Implemente un programa que a través de un menú de opciones permita:
1- Insertar un vehículo en la colección en una posición determinada.
2- Agregar un vehículo a la colección.
3- Dada una posición de la Lista: Mostrar por pantalla qué tipo de objeto se encuentra almacenado en dicha posición.
4- Dada la patente de un vehículo usado, modificar el precio base, y luego mostrar el precio de venta.
5- Mostrar todos los datos, incluido el importe de venta, del vehículo más económico.
6- Mostrar para todos los vehículos que la concesionaria tiene a la venta, modelo, cantidad de puertas e importe de venta.
7- Almacenar los objetos de la colección Lista en el archivo “vehiculos.json”.'''

from claseLista import Lista
import json
from claseNuevo import Nuevo
from claseObjectEncoder import ObjectEncoder
from claseUsado import Usado
from menu import Menu
import unittest

class TestVehiculo(unittest.TestCase):
    lista = Lista()
    def setUp(self):
        jsonF = ObjectEncoder()
        diccionario = jsonF.leerArchivoJSON('vehiculos.json')
        self.__lista = jsonF.decodificarDiccionario(diccionario)

    def TestInsertarVehiculoPos0(self):
        elemento = Usado("argo","4","azul",1500,"gol","base")
        pos = 0
        self.__lista.insertarElemento(elemento,pos)
        self.assertEqual(self.__lista.getTope(),5)

    def TestInsertarVehiculoPos2(self):
        elemento = Nuevo("punto","5","blanco",3500,"chevrolet","full")
        pos = 2
        self.__lista.insertarElemento(elemento,pos)
        self.assertEqual(self.__lista.getTope(),5)

    def TestInsertarVehiculoUltimaPos(self):
        elemento = Usado("argo","4","gris",4500,"suran","full")
        pos = self.__lista.getTope
        self.__lista.insertarElemento(elemento,pos)
        self.assertEqual(self.__lista.getTope(),5)

    def Test_agregarElemento(self):
        elemento = Nuevo("punto","4","negro",5000,"fiat","full")
        self.__lista.agregarElemento(elemento)
        self.assertEqual(self.__lista.getTope(),5)
    
    def TestVerificarObjeto(self):
        pos = 2
        objeto = self.__lista.mostrarElemento(pos)
        self.assertEqual(objeto,Nuevo)

    def TestModificarPrecioBase(self):
        vehiculo = self.__lista.buscarMarca("fiat")
        self.assertEqual(vehiculo.getPrecioBase(),5000)

if __name__ == '__main__':
    unittest.main()