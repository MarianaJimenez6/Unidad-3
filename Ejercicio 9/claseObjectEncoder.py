import json
from pathlib import Path
from claseLista import Lista
from claseNuevo import Nuevo
from claseUsado import Usado

class ObjectEncoder(object):
    def decodificarDiccionario(self,d):
        resultado = None
        if '__class__' not in d:
            resultado = d
        else:
            class_name = d['__class__']
            class_ = eval(class_name)
            if class_name == 'Lista':
                vehiculo = d['Vehiculo']
                unVehiculo = vehiculo[0]
                manejadorLista = class_()
                for i in range(len(vehiculo)):
                    unVehiculo = vehiculo[i]
                    class_name = unVehiculo.pop('__class__')
                    class_ = eval(class_name)
                    atributos = unVehiculo['__atributos__']
                    unVehiculo2 =class_(**atributos)
                    manejadorLista.agregarVehiculo(unVehiculo2)
                    resultado = manejadorLista
                return resultado
    
    def guardarArchivoJSON(self,diccionario,archivo):
        with Path(archivo).open("w",encoding="UTF-8") as destino:
            json.dump(diccionario,destino,indent = 4)
            destino.close()

    def leerArchivoJSON(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            return diccionario
        
    def convertirTextoADiccionario(self,texto):
        return json.loads(texto)