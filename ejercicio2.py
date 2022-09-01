from math import sqrt
from fastapi import FastAPI


app = FastAPI()

x = input("Ingrese el valor de X: ")
y = input("Ingrese el valor de Y: ")


class Punto():
    coordX = 0
    coordY = 0



    def __init__(self, coordX, coordY):
        self.coordX = coordX
        self.coordY = coordY


    def refactorizado(self):
        print(
            "El punto esta ubicado en los puntos: ({},{}) ".format(self.coordX,self.coordY))



punto = Punto(x,y)

punto.refactorizado()
