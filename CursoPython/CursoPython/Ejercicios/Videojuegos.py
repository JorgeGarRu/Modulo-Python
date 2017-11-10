import random
class Videojuegos: #crear una clase

    #Miembros/ no es obligatorio declarar los miembros


    #constructores
    def __init__(self,nombre,publisher,fecha,jugado):# el primer parametro siempre tiene que ser self
        self.nombre = "" #los self actuan como los this en c#
        self.publisher = ""
        self.fecha = 0
        self.jugado = False
    
    
    
    def __init__(self,nombre,publisher,fecha):# el primer parametro siempre tiene que ser self
        self.nombre = nombre #los self actuan como los this en c#
        self.publisher = publisher
        self.fecha = fecha
        self.jugado = False


    def valorarlo(self): #los metodos que se creen , siempre llevaran el self por parametro
        return random.randint(0,10)

    def jugar(self):
        self.jugado = True

    def __str__(self): #es como el To String de c#
        s = "Nombre: " + self.nombre + "\n" + "Publisher: " + self.publisher + "\n" + "Fecha: " + str(self.fecha) +"\n" + "Jugado?:" + str(self.jugado)
        return s