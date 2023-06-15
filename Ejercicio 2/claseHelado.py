from claseSabor import Sabor

class Helado:
    __gramos = None
    __precio = None
    __sabor = list

    def __init__(self,gramos,precio,sabor = None):
        self.__gramos = gramos
        self.__precio = precio
        if sabor != None:
            self.addSabor(sabor,1)

    def addSabor(self,sabor,cantidad):
        for i in range(cantidad):
            self.__sabor.append(sabor)

    def __str__(self):
        print("Gramos: {}, Precio: {}".format(self.__gramos,self.__precio))

    def getPrecio(self):
        return self.__precio
    
    def getGramos(self):
        return self.__gramos