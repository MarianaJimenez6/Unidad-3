class Sabor:
    __id_sabor = None
    __nombre_sabor = None
    __ingredientes = None

    def __init__(self,id_sabor,nombre,ingredientes):
        self.__id_sabor = id_sabor
        self.__nombre_sabor = nombre
        self.__ingredientes = ingredientes

    def mostrarSabores(self):
        print("Id del sabor: {}, Ingredientes: {}, Nombre del sabor: {}".format(self.__id_sabor,self.__ingredientes,self.__nombre_sabor))

    def getIdSabor(self):
        return self.__id_sabor
    
    def getIngredientes(self):
        return self.__ingredientes
    
    def getNombreSabor(self):
        return self.__nombre_sabor