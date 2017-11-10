
def sucesionFibonacci(n):
    
    f0 = 0
    f1 = 1
    fibonacci=[f0,f1]
    for numeros in range(n):
        aux = f0 + f1
        fibonacci.append(aux)
       
        f0 = f1
        f1 = aux

   

def sucesionPadovan(n):
    sucesion = []
    for i in range(n):
        if i == 0 or i == 1 or i == 2:
            sucesion.append(1)
        else:
            valor = sucesion[-2] + sucesion[-3]
            sucesion.append(valor)
    
 
    return sucesion    
        


        
       
    




