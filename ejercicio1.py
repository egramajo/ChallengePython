from math import sqrt
from fastapi import FastAPI


app = FastAPI()


def validar(dato, tipos):
  for tipo in tipos:
    try:
      return tipo(dato)
    except ValueError:
      pass
  return None


print("Ingrese la coord x del punto 1")
punto1x = int(input())
validar(punto1x, (int, float, complex))
print("Ingrese la coord y del punto 1")
punto1y = int(input())
validar(punto1y, (int, float, complex))
print("Ingrese la coord x del punto 2")
punto2x = int(input())
validar(punto2x, (int, float, complex))
print("Ingrese la coord y del punto 2")
punto2y = int(input())
validar(punto2y, (int, float, complex))


def calcularDiagonal():
    diferenciaX = pow(punto2x - punto1x,2)
    diferenciaY = pow(punto2y - punto1y,2)

    diagonal = sqrt(diferenciaX + diferenciaY)
    return diagonal


def calcularAltura():
    altura = punto2x - punto1x
    return altura

def calcularBase():
    base = punto2y - punto1y
    return base


def calcularArea():
    area = calcularBase() * calcularAltura()
    return area


print("La distancia de la diagonal del rectangulo es: " + str(calcularDiagonal()))
print("La altura del rectangulo es: " + str(calcularAltura()))
print("La base del rectangulo es: "+ str(calcularBase()))
print("El Area del rectangulo es: " + str(calcularArea()))