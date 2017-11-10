from math import pi
def ValorNormalizado(a):

    if(a>=0 and a <=100):
    
        return a/100
    else:
        return "El valor debe estar en 0 y 100"

numero = int(input("Introduce un numero:"))

print(ValorNormalizado(numero))


#Devolver el area del triangulo
def areaTriangulo(base,altura):
    return (base*altura)/2

base = int(input("Introduce la base del triangulo: "))
altura = int(input("introduce la altura del triangulo: "))

print(areaTriangulo(base,altura))

#devolver el area del circulo

def areaCirculo(radio):
    return pi*(radio**2)

radio = int(input("Introduce el radio del circulo: "))
print(areaCirculo(radio))

#devolver una lista de rango [a,b] solo con los valores pares

def rangoPar(a,b):

    # return [x for x in range(a,b) if x%2 == 0] ...Otra forma de hacerlo
    lista =list( i for i in range(a,b) if i%2==0)
    return lista

print(rangoPar(1,21))