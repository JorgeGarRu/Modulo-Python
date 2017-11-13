#crea una funcion que dadas dos listas devuelva otra que contenga solo los elementos que tienen en comun

def Elementos_Comunes(lista1,lista2):
    lista3 = []
    for x in lista1:
        for y in lista2:
            if x == y:
                lista3.append(x)
    return lista3

lista1 = [1,2,3,4]
lista2 = [1,5,3,8]

print(Elementos_Comunes(lista1,lista2))
