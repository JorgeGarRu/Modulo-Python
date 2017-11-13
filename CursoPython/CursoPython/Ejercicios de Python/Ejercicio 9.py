#crea una funcion que dado 3 numeros de un digito (0 a 9 ambos inclusives) devuelva una lista con todas las combinaciones posibles
import itertools
def Permuta(n):
    for elemento in itertools.permutations(n, len(n)):
        print(elemento, end = ' ')

c = [1,2,3]
print(Permuta(c))