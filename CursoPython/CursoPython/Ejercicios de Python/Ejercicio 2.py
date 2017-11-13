#crea una funcion que dada una secuencia de numeros que devuelva la misma secuencia eliminando antes el tercer elemento

def Elimina_Tercer_Elemento1(secuencia):
    del(secuencia[2])
    return secuencia

def Elimina_Tercer_Elemento2(secuencia):
    return secuencia[:2] + secuencia[2:]



n = [1,4,2,3,4,8]

print(Elimina_Tercer_Elemento1(n))
print(Elimina_Tercer_Elemento2(n))