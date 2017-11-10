from math import pi #asi se importa el numero pi
from datetime import datetime, date, time, timedelta
numero1=3 
print(numero1)
numero2=3.5
print(numero2)
suma = numero1+numero2
print(suma)
#Asi se pone los comentarios
'''
y asi se pone comentarios mas tochos
'''
#para saber de que tipo es una variable se usa el comando type(variable)

#IF
if True:
    print("if")

    

#en python no existen los arrays, lo que existen son las listas y las tuplas.
#las tuplas son inmutables, cuando se crea, no se puede añadir y eliminar elementos, pero se pueden recorrer
#las listas son mutables, pero no se pueden recorrer

mi_lista = [1,3,4,5] #asi se crea una lista


if 2 in mi_lista:
    print("En la lista hay un 2")
else:
    print("No hay un 2")

print(mi_lista[1])#imprimir el elemento de la lista en la posicion 1
mi_lista.append(6) #añadir un valor en la lista

print(len(mi_lista))#imprimir longitud de la lista

#For
for elemento in mi_lista:
    print(elemento)

año = "1992"

print(type(año)) #para saber el tipo de variable, en este caso es un string
print(type(int(año)))#para hacer un casting de string a int.

print(pi)

#ejercicio 1
meses = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Octubre","Noviembre","Diciembre")

print(meses)

print("Introduce un numero:")
numero_introducido = int(input()) #lo que metamos lo pasamos a int
if(numero_introducido >= 1 and numero_introducido <= len(meses)):
   print(meses[numero_introducido - 1])
else:
   print("Error")

   #ejercico 2
  
lista = []
valor=True

while(valor):
    print("Introduce otro numero:")
    numero = int(input())

    if(numero is not 0):
        lista.append(numero)
        print(lista)
    else:
        valor = False

#ejercicio 3

tupla = (1,2,2,2,5)

numero1 = int(input("Introduce el ultimo numero: "))

cont = 0
for elemento in tupla:
   
    if numero1 is elemento:
        cont = cont + 1

print("Se repite " + str(cont) + " veces")

#ejercicio 4

tupla2 = (2,3,5,1)

print(str(min(tupla2)) + " y " + str(max(tupla2)))

#diccionarios
mi_diccionario = { 
    1: "lunes",
    2: "martes"
    }

print(mi_diccionario[1])

#####Ejemplo diccionarios######

#Primera parte: crear una tupla de numeros aleatorios



#Segunda parte: crear un diccionario donde las claves son los numeros y los values seran las veces repetidas


#Tercera parte: imprimir por consola 
