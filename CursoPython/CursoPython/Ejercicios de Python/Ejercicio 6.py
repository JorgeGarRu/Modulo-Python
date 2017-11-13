#crea un juego que dado un numero , adivine un numero aleatorio 

import random

def Numero_Secreto():
    numero_secret = int(random.randint(1,10))
    o= True
    while(o):
        numero_elegido = int(input("Elige un numero entre 1 y 10, ambos inclusives"))
        if numero_elegido != numero_secret:

        
            if (numero_elegido < numero_secret):
                print("Demasiado bajo")
            else:
                print("demasiado alto")
        else:
            print("Acertastes")
            o = False


Numero_Secreto()