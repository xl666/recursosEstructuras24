Paises = ["Mexico",  "Estados Unidos", "Canada", "Chile"]
Paises.insert(3, "Brasil") #inserta  un elemento en una posicion especificada
Paises.insert(0,"Japon") 
Paises.remove("Canada")#elimina el elemento que coincide con el parametro indicado
print ("peru" in Paises) #Busca  si existe el elemento "Peru" en la lista de paises y devuelve True o False
print(Paises)
print (len(Paises)) #Devuelve la cantidad de elementos en la lista de paises
Paises.clear()#Vacía la lista de países
print (Paises)