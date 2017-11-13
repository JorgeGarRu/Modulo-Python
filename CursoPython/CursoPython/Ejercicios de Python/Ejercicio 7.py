#crea una funcion que devuelva una lista con el primer y ultimo elemento de una lista dada

def Lista_PrimeryUltimo(lista):
    lista1=[]

    
    lista1.append(lista[0])
    lista1.append(lista[-1])
    return lista1

lista2 = [1,4,5,6,8,9,10]

print(Lista_PrimeryUltimo(lista2))
