# - - - Declaración de una lista
numeros = [1, 2, 3, 4, 5]

# - - - Acceder a elementos de la lista
print(numeros[0])  # Imprime el primer elemento de la lista (índice 0)
print(numeros[2])  # Imprime el tercer elemento de la lista (índice 2)

# - - - Modificar elementos de la lista
numeros[0] = 10  # Modifica el primer elemento de la lista
print(numeros)   # Imprime la lista modificada: [10, 2, 3, 4, 5]

# - - - Agregar elementos al final de la lista:
numeros.append(6)  # Agrega el número 6 al final de la lista
print(numeros)     # Imprime la lista actualizada: [10, 2, 3, 4, 5, 6]

# - - - Eliminar elementos de la lista por valor:
numeros.remove(3)  # Elimina el elemento 3 de la lista
print(numeros)     # Imprime la lista actualizada: [10, 2, 4, 5, 6]

# - - - Eliminar elementos de la lista por índice:
del numeros[0]  # Elimina el primer elemento de la lista
print(numeros)  # Imprime la lista actualizada: [2, 4, 5, 6]

# - - - Longitud de la lista
print(len(numeros))  # Imprime la longitud de la lista

# - - - Iteración sobre una lista
for numero in numeros:
    print(numero)  # Imprime cada elemento de la lista en una línea separada

# - - - Reversión de una lista:
numeros.reverse()  # Invierte el orden de los elementos en la lista
print(numeros)     # Imprime la lista invertida

# - - - Ordenamiento de una lista:
numeros.sort()  # Ordena los elementos de la lista de forma ascendente
print(numeros)  # Imprime la lista ordenada