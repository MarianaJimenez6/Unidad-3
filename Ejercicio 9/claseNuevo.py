from claseVehiculo import Vehiculo

class Nuevo(Vehiculo):
    __marca = 'Toyota'
    __version = None

    def __init__(self,modelo,puertas,color,precio,marca,version):
        super().__init__(modelo,puertas,color,precio)
        self.__marca = marca
        self.__version = version

    def getMarca(self):
        return self.__marca
    
    def getVersion(self):
        return self.__version
    
    def importeVenta(self):
        precioBase = (self.getPrecioBase() * 0.10)+self.getPrecioBase()
        if self.__version == 'full':
            precioBase += self.getPrecioBase() * 0.02
            print("Precio base: ",precioBase)
        else:
            print("Precio base: ",precioBase)

    def getPrecioBase(self):
        return super().getPrecioBase()
    
    def __str__(self):
        return "Modelo: %s, Puertas: %s, Color: %s, Precio: %s, Marca: %s, Version: %s "%(super().getModelo(),super().getCantidadPuertas(),super().getColor(),self.getPrecioBase(),self.__marca,self.__version)
    
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
            modelo = super().getModelo(),
            puertas = super().getCantidadPuertas(),
            color = super().getColor(),
            precio = self.getPrecioBase(),
            marca = self.__marca,
            version = self.__version
            )
        )
        return d