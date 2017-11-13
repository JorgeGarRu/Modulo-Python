#Crea una funcion que simule el juego de Piedra, papel o Tijeras


def Piedra_Papel_Tijeras():
    jugador1 = input("Jugador 1, ¿Cuál es tu elección?")
    jugador2 = input("Jugador 2, ¿Cuál es tu eleccion?")

   
    if jugador1 != jugador2:

        if(jugador1 == "piedra" and jugador2 == "tijeras") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijeras" and jugador2 == "papel"):
            print("Gana el jugador 1")
            
        else:
            print("Gana el jugador 2")
        
        
    else:
        print("Empate")

    

Piedra_Papel_Tijeras()



