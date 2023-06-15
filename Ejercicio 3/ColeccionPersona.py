from clasePersona import Persona

class ColeccionPersona:
    __lista = []

    def __init__(self):
        self.__lista = []
        
    def agregarPersona(self,persona):
        self.__lista.append(persona)