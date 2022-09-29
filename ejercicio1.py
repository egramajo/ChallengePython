from math import sqrt
from fastapi import FastAPI


app = FastAPI()



#Se cargan mediante un input las coordenadas de los puntos 

print("Ingrese la coord x del punto 1")
punto1x = int(input())

print("Ingrese la coord y del punto 1")
punto1y = int(input())

print("Ingrese la coord x del punto 2")
punto2x = int(input())

print("Ingrese la coord y del punto 2")
punto2y = int(input())


# Metodo que calcula el valor de la diagonal del rectangulo
def calcularDiagonal():
    diferenciaX = pow(punto2x - punto1x,2)
    diferenciaY = pow(punto2y - punto1y,2)

    diagonal = sqrt(diferenciaX + diferenciaY)
    return diagonal

# Metodo que calcula la altura del rectangulo
def calcularAltura():
    altura = punto2x - punto1x
    return altura

# Metodo que calcula la base del rectangulo
def calcularBase():
    base = punto2y - punto1y
    return base

# Metodo que calcula el area del rectangulo
def calcularArea():
    area = calcularBase() * calcularAltura()
    return area


print("La distancia de la diagonal del rectangulo es: " + str(calcularDiagonal()))
print("La altura del rectangulo es: " + str(calcularAltura()))
print("La base del rectangulo es: "+ str(calcularBase()))
print("El Area del rectangulo es: " + str(calcularArea()))