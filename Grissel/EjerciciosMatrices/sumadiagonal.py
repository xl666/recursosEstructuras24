def crear_matriz(F, C):
    matriz = []
    for _ in range(F):
        fila = []
        for _ in range(C):
            valor = int(input())
            fila.append(valor)
        matriz.append(fila)
    return matriz
#- - - - - - - - - - - - - - - - - - - 
def suma_diagonal(matriz):
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][i]
    return suma
# - - - - - - - - - - - - - - - - - - 
F = int(input())
C = int(input())
matriz = crear_matriz(F, C)
resultado = suma_diagonal(matriz)
print(resultado)