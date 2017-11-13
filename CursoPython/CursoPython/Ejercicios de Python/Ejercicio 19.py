#crea una funcion que dado un numero n genere un diccionario de 1 a n(inclusive) donde cada clave sea x (siendo x cada numevo de 1 a n) y el valor sea x^2

def Genera_Diccionario(n):
    dic = {x:x**2 for x in range(1,n)} #diccionario por compresion
    return dic

print(Genera_Diccionario(10))
