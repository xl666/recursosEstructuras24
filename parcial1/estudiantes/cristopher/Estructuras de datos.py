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

#Diccionarios
#   No ordenados
#   Heterogeneos
#   Mutable

#              En caso de que se repita la key tomara la ultima posicion 
diccionario = {1:'uno', 2:'dos'}
diccionario[3] = 'Tres'
print(diccionario)
