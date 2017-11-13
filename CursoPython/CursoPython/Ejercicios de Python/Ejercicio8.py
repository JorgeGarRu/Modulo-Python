#crea una funcion que dada una frase(con mas de 2 palabras) devuelva otra frase con las palabras en orden inverso

def Orden_Inverso1(list): #forma 1 de hacerlo
    if len(list)==1:
        return list
    else:
        return list[-1]+Orden_Inverso1(list[:-1])

def Orden_Inverso2(list):#forma 2 de hacerlo
    return list[::-1]


frase = "hola que pasa como estas"

print(Orden_Inverso1(frase))

print(Orden_Inverso2(frase))
