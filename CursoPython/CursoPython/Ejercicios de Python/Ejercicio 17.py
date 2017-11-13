#crea una funcion que dado un diccionario devuelva un diccionario con las claves ordenadas de menos a mayor
import operator
def Ordenar_Diccionario(diccionario):
    
    
    resultado = sorted(diccionario.items(), key=operator.itemgetter(0))
    return resultado

diccionario={1:"pepe",4:"Jose",3:"maria"}

print(Ordenar_Diccionario(diccionario))