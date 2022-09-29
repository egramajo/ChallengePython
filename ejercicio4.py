from fastapi import FastAPI


app = FastAPI()

# Creacion de SuperClase Vehiculo
class Vehiculo():
    color = ""
    ruedas = ""
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas


    def __str__(self):
        return 'Color:{}, {} ruedas.'.format(self.color, self.ruedas)


# Creacion clase Carro que hereda sus atributos de la clase Vehiculo
class Carro(Vehiculo):
   
    def __init__(self, color, ruedas,velocidad,cilindraje):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindraje = cilindraje

    def __str__(self):
        return 'Color: {}, {} Km/h, {} ruedas, {} cc.'.format(self.color, self.velocidad, self.ruedas, self.cilindraje)

a = Carro("azul", 2,  200, 1700)

        
# Creacion clase Camioneta que hereda sus atributos de la clase Carro
class Camioneta(Carro):
    def __init__(self, color, ruedas, velocidad, cilindraje, carga):
        super().__init__(color, ruedas, velocidad, cilindraje)
        self.carga = carga

    def __str__(self):
        return 'Color: {}, {} Km/h, {} ruedas, {} cc, {} Kg de carga.'.format(self.color, self.velocidad, self.ruedas, self.cilindraje, self.carga)

c = Camioneta("Rojo", 4,  220, 2200, 2000)


# Creacion clase Bicicleta que hereda sus atributos de la clase Vehiculo
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

# Creacion clase Motocicleta que hereda sus atributos de la clase Bicicleta
class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindraje):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindraje = cilindraje


class ListaVehiculos():
    vehiculos = []

    def __init__ (self, vehiculos=[]):
        self.vehiculos = vehiculos


    # Metodo para agregar videojuegos a la lista.
    def agregar(self, v):
        self.vehiculos.append(v)

    # Metodo para mostrar esos videojuegos.
    def mostrar(self):
        for v in self.vehiculos:
            print(v)

    
    def catalogar(self, ruedas):
        cantidadR = 0
        cantidadV = 0
        for v in self.vehiculos:
            if v.ruedas == ruedas:
                cantidadV = cantidadV + 1
                cantidadR = cantidadR + v.ruedas
        return print("Se han encontrado {} vehículos con {} ruedas: ".format(cantidadV,cantidadR))      


auto = Carro("Rojo",4,120,1200)
auto2 = Carro("Rojo",4,120,1200)
bici = Bicicleta("Azul",2,"deportiva")
c = ListaVehiculos()

c.agregar(auto)
c.agregar(auto2)
c.agregar(bici)
c.catalogar(4)