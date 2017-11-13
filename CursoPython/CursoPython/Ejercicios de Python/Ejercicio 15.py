#Crea una funcion que dada una lista de numeros devuelva una lista con los numeros ordenados de menor a mayor

def Ordenar_Lista(lista):

    lista_nueva = sorted(lista)#el sorted devuelve una lista ordenada de menor a mayor de la lista dada
    return lista_nueva

lista = [3,2,4,5,1]
print(Ordenar_Lista(lista))
