#crea una funcion que dados 3 diccionarios devuelva diccionario unificado(no debe haber claves repetidas entre los diccionarios de entrada)

def Diccionario_Unificado(dic1,dic2,dic3):
    dic4 = {}
    dic4.update(dic1)
    dic4.update(dic2)
    dic4.update(dic3)
    return dic4

dic1={1:"pepe",2:"Jose",3:"maria"}
dic2={4:"pepe",5:"Jose",6:"maria"}
dic3={7:"pepe",8:"Jose",9:"maria"}

print(Diccionario_Unificado(dic1,dic2,dic3))