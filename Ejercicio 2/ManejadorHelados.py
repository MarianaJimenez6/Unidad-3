from claseHelado import Helado

class ManejaHelados:
    __lista = []

    def __init__(self):
        self.__lista = []

    def registrarHelado(self,gramos,cantidad,codigo,listaSabores): #item1
        print("-----Registrar helado-----")
        precio = self.preciosHelados(cantidad)
        lista= self.EleccionSabores(listaSabores)
        unHelado = Helado(cantidad,precio,lista)
        self.__lista.append(unHelado)

    def preciosHelados(self,cantidad):
        pass

    def saboresMasPedidos(self,listaSabores): #item2
        indices = list(enumerate(listaSabores))
        indices.sort(key=lambda x: x[1],reverse=True)
        i = 0
        ind = []
        while i < 5:
            ind.append(indices[i][0])
            i = i+1
        return ind

    def totalGramos(self,listaSabores,cod): #item3
        i = 0
        j = 0
        acum = 0
        while i < len(self.__lista):
            listaSab = self.__lista[i].getSabores()
            while j < len(listaSab):
                if listaSab[j].getCodigo() == cod:
                    sabores = len(listaSab)
                    gramos = self.__lista[i].getGramos()/sabores
                    acum += gramos
                    j = j+1
                else:
                    j = j+1
            i = i+1
            j = 0
        listaSab.mostrarSabor(cod)
        print("Gramos vendidos totales: ",acum)

    def saboresporTamanio(self,tamanio): # item4
        pass
        

    def totalRecaudado(self): #item5
        acum = 0
        for i in range(len(self.__lista)):
            precio = self.__lista.getPrecio(i)
            acum = acum + precio
        print("Total recaudado por los helados: ",acum)
