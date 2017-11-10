
#import SucesionesVarias
#from Videojuegos import Videojuegos # asi se importa una clase: from "Archivo.py" import "clase"
#from Musica import Instrumento
#from Musica import Piano
#from Musica import Trompeta
#from Musica import * -----> Esto lo importa todo
from Ejercicios.Musica import *


# -*- coding: utf-8 -*-

#print(SucesionesVarias.sucesionFibonacci(20))
#print(SucesionesVarias.sucesionPadovan(20))

#TheWitcher3 = Videojuegos("The Witcher 3","CD Projekt Red",2015) #asi se crea un objeto de una clase
#print(TheWitcher3.nombre)
#print(TheWitcher3.publisher)
#print(TheWitcher3.fecha)
#print(TheWitcher3)
#TheWitcher3.jugar()
#print(TheWitcher3)

piano = Piano("Casio","Cuerda Percutida",1695,"Madera",False,88,False)

trompeta = Trompeta("Yamaha","Viento",1607,"Laton",True,"Si bemol",True)

piano.sonar()
trompeta.sonar()
piano.afinar()



