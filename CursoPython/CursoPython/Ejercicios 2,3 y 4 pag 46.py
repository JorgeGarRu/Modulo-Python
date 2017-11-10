#ejercicio 2
#agenda_personal ={
#    "Quedar con Ana":"09:00",
#    "Ir al taller":"19:00",
#    "Almorzar con Alba":"15:00",
#    "Reunion con Jose":"9:30"
#    }


#print(agenda_personal)

#ejercicio 3
def formato(diccionario):
   

    for k,v in diccionario.items():
        print(v + "->" + k)
    



#ejercicio 4

def imprime(diccionario1):
    file=open("ejercicio4.txt","w")
    file.write(str(diccionario1))
    file.close


agenda_personal ={ 
   "Quedar con Ana":"09:00",    "Ir al taller":"19:00",    "Almorzar con Alba":"15:00",
   "Reunion con Jose":"9:30"
   }




