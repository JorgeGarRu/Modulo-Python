

#file = open("prueba.txt",'w')#abrimos un archivo de texto("el nombre del archivo que queramos abrir/crear","w para escribir")
#file.write("Hola que tal\n")
#file.write("Esta es la segunda linea")
#file.close()

file=open("prueba.txt","r") #para leer el archivo
print(file.read())
file.close