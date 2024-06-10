#Diccionario
#Manera de recorrer un diccionario con un for
    #for i,j in diccionario.items():
        #print(i,j)

#Manera de crear diccionarios personalizados con comprension
#diccionario = {input():input() for _ in range(3)}

#-------------------------Metodos-------------------------
usuarios = {0:'Mario', 1:'Luigi',2:'Jonas'}
r_usuarios = usuarios.copy()

#Acceder a los valores 
usuarios.values()

#Accededer a las llaves
usuarios.keys()

#Eliminar item del diccionario
usuarios.pop(1)

#Eliminar el ultimo item
usuarios.popitem()

#Obtener un valor en espicifico
usuarios.get(1)

#Buscar un elemento y si no lo encuentra lo crea
usuarios.setdefault(7,'Nuevo')

#Borrar diccionario
usuarios.clear()

#Acualizar un diccionario
usuarios.update({'1':'Hola','2':'Adios'})

ordenado = sorted(usuarios.items())
