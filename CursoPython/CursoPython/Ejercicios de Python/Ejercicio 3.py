#crea una funcion que dado un numero devuelva una lista con todos los divisores de ese numero
def Devuelve_Divisores(numero):
    divisores=[]
    for i in range(1,int(numero/2)+1): #como el maximo divisor de un numero siempre será la mitad de ese numero,recorremos solos hasta su mitad. 
        if numero%i == 0:              #y en el caso de ser un numero impar, se sabe que su maximo divisor será la tercera parte del numero
            divisores.append(i)
    return divisores

n = 51
print(Devuelve_Divisores(n))
