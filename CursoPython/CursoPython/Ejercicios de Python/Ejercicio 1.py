#crea una funcion que dada una secuencia de numeros determine si todos los numeros son diferente entre ellos. 
#Tiene que devolver True o False

def digitos_distintos1(secuencia1):
    
    secuencia2=list(set(secuencia1))#con el set conseguimos que se elimine de la secuencia1, los elementos repetidos
    if len(secuencia1) != len(secuencia2):#entonces comparamos sus longitudes, para ver si al pasar a set, se ha eliminado algunos elementos
        return False
    else:
        return True

def digitos_distintos2(secuencia1):

    conjunto=set(secuencia1) #otra forma mas corta de hacerlo
    return len(secuencia1) == len(conjunto)
   
def digitos_distintos3(secuencia1):#otra forma
    distintos =[]

    for e in secuencia1:
        if e not in distintos:
            distintos.append(e)
        else:
            return False
    return True


n = [3,4,4,5,5]

print(digitos_distintos1(n))

print(digitos_distintos3(n))
        
