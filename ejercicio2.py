from math import sqrt
from fastapi import FastAPI


app = FastAPI()


# Se define la clase Punto
class Punto():
    # Se crea el constructor
    def __init__(self, coordX, coordY):
        if coordX == '':
            self.coordX = 0
        else:
            self.coordX = coordX
        if  coordY == '':
            self.coordY = 0
        else:
            self.coordY = coordY

    # Metodo que muestra en que cuadrante esta ubicado el punto
    def cuadrante(self):
        coordenadaX = int(self.coordX)
        coordenadaY = int(self.coordY) 
        if coordenadaX >= 0 and coordenadaY >= 0:
            mensaje = "Cuadrante 1."
        elif coordenadaX <= 0 and coordenadaY >= 0:
            mensaje = "Cuadrante 2."
        elif coordenadaX <= 0 and coordenadaY <= 0:
            mensaje = "Cuadrante 3."
        else:
            mensaje = "Cuadrante 4."
        return mensaje


    # Metodo que formatea el punto dandole un formato ( , )
    def __str__(self):
        
        return '({},{})'.format(self.coordX, self.coordY)


# Se cargan los valores del punto
x = input("Ingrese el valor de X: ")
y = input("Ingrese el valor de Y: ")

punto = Punto(x,y)

print("El punto esta ubicado en el " + punto.cuadrante())


# Se cargan los valores del punto
x2 = input("Ingrese el valor de X: ")
y2 = input("Ingrese el valor de Y: ")

punto2 = Punto(x2,y2)


# Metodo que calcula el vector que une los puntos
def calcularVector():
    
    vx = int(punto2.coordX) - int(punto.coordX)
    vy = int(punto2.coordY) - int(punto.coordY)
    punto3 = Punto(vx,vy)
    return print("El vector que une los 2 puntos es: " + punto3.__str__())


# Metodo que calcula la distancia entre los 2 puntos
def calcularDistancia():
    v1 = pow(int(punto2.coordX) - int(punto.coordX),2)
    v2 = pow(int(punto2.coordY) - int(punto.coordY),2)

    diferencia = sqrt(v1 + v2)
    return diferencia


calcularVector()
print("La distancia entre los 2 puntos es: " + str(calcularDistancia()))