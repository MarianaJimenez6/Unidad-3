import json
from pathlib import Path
from claseDocente import Docente
from claseDocenteInvestigador import DocenteInvestigador
from claseInvestigador import Investigador
from claseLista import Lista
from clasePersonal import Personal
from clasePersonaldeApoyo import PersonaldeApoyo

class ObjectEncoder(object):
    
    def decodificarDiccionario(self,d):
        retorno = None
        if '__class__' not in d:
            retorno = d
        else:
            class_name = d['__class__']
            class_ = eval(class_name)
            if class_name == 'Lista':
                agente = d['Personal']
                unAgente = agente[0]
                manejadorLista = class_()
                for i in range(len(agente)):
                    unAgente= agente[i]
                    class_name=unAgente.pop('__class__')
                    class_=eval(class_name)
                    atributos=unAgente['__atributos__']
                    unPunto=class_(**atributos)
                    manejadorLista.agregarPersonal(unAgente)
                    retorno = manejadorLista
        return retorno
    
    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close() 

    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario
        
    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)
