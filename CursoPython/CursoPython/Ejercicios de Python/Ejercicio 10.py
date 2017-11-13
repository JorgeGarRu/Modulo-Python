#crea una funcion que dada una frase devuelva un diccionario con el numero de veces que aparece cada caracter
import collections
def Devuelve_Diccionario(frase):
    frase = list(frase)
    diccionario_numeros=dict(collections.Counter(frase)) #metodo que cuenta las repeticiones de los elementos de una lista
    return diccionario_numeros

def Devuelve_Diccionario1(frase):
    diccionario = {x:frase.count(x) for x in set(frase)} #forma 2 de hacerlo
    return diccionario

frase = "hola que tal"

print(Devuelve_Diccionario(frase))
print(Devuelve_Diccionario1(frase))


