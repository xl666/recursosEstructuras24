def obtener_interseccion(lista1, lista2):
    interseccion = []
    for elemento in lista1:
        if elemento in lista2 and elemento not in interseccion:
            interseccion.append(elemento)
    interseccion.sort()
    return interseccion

N = int(input())
M = int(input())

lista1 = [int(input()) for _ in range(N)]
lista2 = [int(input()) for _ in range(M)]

resultado = obtener_interseccion(lista1, lista2)
print(resultado)
