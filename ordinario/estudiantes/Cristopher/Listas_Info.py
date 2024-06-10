#Listas Ordenadas, lineales, Mutables

#Usar copy pues si se hace N_Lista = lista se esta usando la misma direccion
#de memoria y cualquier cambia que haga a la nueva tambien afecta a la original

lista = [1,2,3,4,5]
N_lista = lista.copy()

#Metodo
lista = [1,2,3,4,5]

#Agregar elemento al final
lista.append(6)

#Mostar el numero de veces que se repite un elemento
lista.count(3)

#Muestra la posicion de la primera aparicion de un elementoç
lista.index(4)

#Elimina la primera aparicion de un elemento
lista.remove(6)

#Devuelve y elimina el ultimo elemento 
lista.pop()

#Poner un elemento en una posicion especifica
lista.insert(0,-1)

#Ordena alfabeticamente
lista.sort()

#Eliminar toda la lista
lista.clear()

#Encontrar el numero màs grade de una lista
max(lista)

#Sumar elementos de la lista
sum(lista)

#Ordenar
sorted(lista)

#Invertir
reversed(lista)

#Intercalar
salida = []
    for i in range(len(lista)):
        salida[len(salida):] = [lista[0]]
        salida[len(salida):] = [lista2[0]]
    
    return salida

#----------------------------Matrices-----------------------------
#Crear Matriz
filas = int(input())
columnas = int(input())
matriz = []

for n in range(filas):
    matriz.append([int(input()) for n in range(columnas)])

#Sacar longitud de filas y columnas
filas = len(Matriz)
columans = len(Matriz[0])

#Recorrer Matriz (varìa depenediendo del caso)
for i in range(filas):
    for j in range(columnas):
        print(i,j) #Por ejemplo
