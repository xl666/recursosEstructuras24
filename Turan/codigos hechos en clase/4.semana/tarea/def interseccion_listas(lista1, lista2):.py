def interseccion_listas(lista1, lista2):
    # Convertimos las listas en conjuntos para eliminar repeticiones
    set1 = set(lista1)
    set2 = set(lista2)
    # Obtenemos la intersección de los conjuntos
    interseccion = set1.intersection(set2)
    # Convertimos la intersección de nuevo en lista y la ordenamos
    interseccion_ordenada = sorted(list(interseccion))
    return interseccion_ordenada

# Leer entrada
N = int(input())
M = int(input())

lista1 = list(map(int, input().split(", ")))
lista2 = list(map(int, input().split(", ")))

# Obtener intersección
resultado = interseccion_listas(lista1, lista2)

# Imprimir resultado
print(resultado)