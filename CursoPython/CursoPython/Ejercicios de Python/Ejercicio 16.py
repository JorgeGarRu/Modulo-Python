#crea una funcion que dada una lista devuelva una copia de la misma desordenada aleatoriamente
import random
def Desordenar_Aleatoriamente(lista):
    random.shuffle(lista)
    return lista
                                
lista = [3,5,2]

print(Desordenar_Aleatoriamente(lista))