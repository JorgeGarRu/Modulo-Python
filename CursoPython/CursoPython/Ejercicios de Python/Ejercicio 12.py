#crea una funcion que dada una secuencia de numeros devuelva la multiplicacion de todos sus elementos
import math
def Devuelve_Multiplicacion(lista):
    acum = 1
    for x in lista:
        #acum = acum * x
        acum *= x
    return acum
    

lista = [3,3]

print(Devuelve_Multiplicacion(lista))
