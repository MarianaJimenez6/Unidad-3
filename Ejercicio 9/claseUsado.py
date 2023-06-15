from claseVehiculo import Vehiculo

class Usado(Vehiculo):
    __patente = None
    __anio = None
    __kilometraje = None

    def __init__(self,modelo,puertas,color,precio,patente,anio,km):
        super().__init__(modelo,puertas,color,precio)
        self.__patente = patente
        self.__anio = anio
        self.__kilometraje = km

    def getPatente(self):
        return self.__patente
    
    def getAnio(self):
        return self.__anio
    
    def getKilometraje(self):
        return self.__kilometraje
    
    def cambiarPrecioBase(self,precio):
        super().cambiarPrecioBase(precio)

    def importeVenta(self):
        precio = self.getPrecioBase() + (self.getPrecioBase()*((2023-self.__anio)/100))
        if self.__kilometraje < 100000:
            precio += precio * 0.2
            precio += precio * 0.10
            print("Precio de venta: ",precio)
        else:
            print("Precio de venta: ",precio)

    def __str__(self):
        return "Modelo: %s, Puertas: %s, Color: %s, Precio: %s, Patente: %s, Anio: %s, Kilometraje: %s "%(super().getModelo(),super().getCantidadPuertas(),super().getColor(),self.getPrecioBase(),self.__patente,self.__anio,self.__kilometraje)

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
            modelo = super().getModelo(),
            puertas = super().getCantidadPuertas(),
            color = super().getColor(),
            precio = self.getPrecioBase(),
            patente = self.__patente,
            anio = self.__anio,
            kilometraje = self.__kilometraje
            )
        )
        return d