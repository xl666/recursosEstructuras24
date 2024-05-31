#Diccionario
#Manera de recorrer un diccionario con un for
    #for i,j in datos.items():
        #print(i,j)

#manera de crear un diccionario personalizado
    #n_elementos = int(input())
    #Diccionario = {}

    #for i in range(n_elementos):
        #llave = input()
        #Diccionario[llave] = input()


users = {0: 'Mario', 1:'Luigi', 2:'James'}
r_users = users.copy() #Crea una copia pero los id siguen apuntando alos originales
print(users.values())
print(users.keys())
users.pop(1) #elimina un item en el diccionario
users.popitem() #elimina el ultimo item
print(users)
print(r_users.get(1))
print(r_users.setdefault(2, '???')) #Busca un elemento y si no lo encuentra lo crea
print(users.clear())
print(r_users.items())
users.update({'1': 'Hola','2':'Como estas?'}) #Actualizar un diccionario
print(users)
users |= {1:2, 3:4, 5:6}
print(users)

#string
name = input()

#Obtains the lenght of a string 
print(len(name))

#Obtains the position of a character 
print(name.find('i'))

#Obtains the last apparence of a character
print(name.rfind('s'))

#Incluye una mayuscula al inicio 
print(name.capitalize())

#Pasa toda la cadena a mayusculas
print(name.upper())

#Pasa a minusculas la caena 
print(name.lower())

#Verifica si son numeros
print(name.isdigit())

#Verifica si son caracteres 
print(name.isalpha())

#Count de number of apparences of a character 
print(name.count('s'))

#Change a character in a string
nuevo_nombre = name.replace('c',"p")
print(nuevo_nombre)

#quita espacios al inicio o al final
print(name.strip())

#Cada palabra se convierte en un objeto de una lista
print(name.split('c'))

#Sirve para añadir placeholders
print('Hola mi nombre es {name}'.format(name = 'cris'))

#Devuelve true si termina con el caracter
print(name.endswith('s'))

#Devuelve true si empieza con el caracter
print(name.startswith('c'))

#Sirve para pasaar caracteres a lista
print(''.join(name))

#Listas
#       Ordenadas 
#       Hetereogéneas
#       Mutables

#Usar copy pues si hago  N_lista = lista se esta usando la misma direccion de memoria y cualquier cambio que haga a la nueva también afectara a la orignal
lista = []
N_lista = lista.copy()
lista = [29,True,45.67,"Hola"]
lista[2] = 'Hola' #Cambiar un elemento en un indice especifico 

#Metodos
lista_nueva = [1,2,3,4,5] 
lista_nueva.append(3) #Agrega un elemento al final 

print(lista_nueva.count(3)) #Muestra el numero de veces que se repite un elemento

print(lista_nueva.index(4)) #Muestra la posicion de la primera aparicion de un elemento

lista_nueva.remove(3) #Elimina la primera aparición de un elemento

#Para añadir a la lista
lista_nueva.append('ice cream')

#para remover
lista_nueva.remove('ice cream')

#remueve el ultimo elemento
lista_nueva.pop()

#cambiar elementos
lista_nueva.insert(0,'cake')

#ordena alfabeticamente 
#lista_nueva.sort()

#ELimina toda la lista
lista_nueva.clear()

#Encontrar el numero más grande en una lista
l = [1,2,3,4,5]
print(max(l))

#Crea una copia de la lista
print(l)
m = l.copy()
print(m)

#Tupla
#       Ordenada
#       Heterogenea
#       No mutable 

tupla = ('Hola',True,False)
print(tupla)

#Conjunto también conocidos como sets
#       No ordenados
#       Heterogeneos 
#       Mutables
#       Sin repeticion 
print(set([5,4,3,2,1]))
print(set((1,2,3,4,5)))
print(set('12345.65'))

conjunto = set([1,2,3,4,5])
conjunto.add(6)
conjunto.remove(1)

conjunto2 = set([5,4,7,8,2])
conjunto3 = set([3,4,5,2,3])
print(conjunto2.intersection(conjunto3))

my_list = [1, 2, 3, 3, 4, 5, 5]
my_set = set(my_list)
print(my_set)