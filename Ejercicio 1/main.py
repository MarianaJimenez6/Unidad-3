'''Ejercicio 1
Composición
Usted es el programador de una empresa de software. 
El analista le ha entregado la siguiente parte del diagrama de clases del nuevo software que están desarrollando.
A. Implemente las clases del diagrama anterior.
B. Defina una clase ManejaFacultades que permita manejar las 5 facultades que posee la UNSJ.
C. Implemente un programa principal que permita:
a. Cargar los datos de las facultades en una instancia de la clase ManejaFacultades. Para esto debe considerar que la UNSJ ha provisto un archivo 'Facultades.csv' con los datos de las facultades. 
Este archivo presenta la siguiente estructura lógica: en una línea están los datos de la Facultad y a continuación, una línea por cada carrera con sus respectivos datos (repitiendo como primer dato, el código de Facultad). Esto se repite para cada facultad.
D. A través de un menú de opciones implementar las siguientes funcionalidades:
1. Ingresar el código  de una facultad y mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad.
2.  Dado el nombre de una carrera, mostrar código (se conforma con número de código de Facultad y código de carrera), nombre y localidad de la facultad donde esta se dicta.'''

from claseMenu import Menu
from manejadorFacultades import ManejaFacultades

if __name__ == '__main__':
    menu1 = Menu()
    facultades = ManejaFacultades()
    facultades.leerArchivo()
    facultades.mostrarDatos()
    menu1.mostrarMenu(facultades)