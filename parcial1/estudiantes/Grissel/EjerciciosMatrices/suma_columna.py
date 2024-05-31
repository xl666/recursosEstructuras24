def crear_matriz(F, C):
    matriz = []
    for _ in range(F):
        fila = [int(x) for x in input().split()]
        matriz.append(fila)
    return matriz

def suma_columnas(matriz):
    sumas = [0] * C
    for fila in matriz:
        for j in range(len(fila)):
            sumas[j] += fila[j]
    return sumas

if __name__ == '__main__':
    F = int(input())
    C = int(input())
    matriz = crear_matriz(F, C)
    resultado = suma_columnas(matriz)
    print(', '.join(str(num) for num in resultado))
