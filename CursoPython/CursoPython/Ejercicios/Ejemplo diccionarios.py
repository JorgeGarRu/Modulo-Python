import random
import collections
#####Ejemplo diccionarios######

#Primera parte: crear una tupla de numeros aleatorios



numero_elementos=30
#for i in range(numero_elementos): #recorre un rango de 10 numeros
#    aleatorio=random.randint(0,50) #
#    lista_numeros.append(aleatorio)

tupla_numeros=tuple(random.randint(0,50) for i in range(numero_elementos)) # esto devuelve lo mismo que el for anterior/se le llama lista por comprension


#print(tupla_numeros)

#Segunda parte: crear un diccionario donde las claves son los numeros y los values seran las veces repetidas

print("Opcion 1:")
diccionario = dict() #forma 1 de hacerlo
for x in tupla_numeros:
    if x in diccionario:
        diccionario[x] +=1
    else:
        diccionario[x] = 1
print(diccionario)

print("Opcion 2:")
diccionario = {x:tupla_numeros.count(x) for x in set(tupla_numeros)} #forma 2 de hacerlo
print(diccionario)

print("Opcion 3:")
diccionario_numeros=dict(collections.Counter(tupla_numeros)) #forma 3 de hacerlo
print(diccionario_numeros)

#Tercera parte: imprimir por consola con el formato
'''
k1->v1
k2->v2
...
'''


for k in diccionario: #forma 1 de hacerlo
    v=diccionario[k]
    print( str(k) + "-> "+ str(v))


[print(str(k) + " -> " + str(diccionario[k])) for k in diccionario] # forma 2 de hacerlo

