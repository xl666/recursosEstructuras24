
def suma_diagonal(filas, columnas, matriz):
    if filas != columnas or len(matriz) != filas:
        return None
    
    suma_diagonal = 0 

    for i in range(filas):
        suma_diagonal += matriz[i][i]
    return suma_diagonal

def matrizfinal(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = int(input())
            fila.append(elemento)
        matriz.append(fila)
    return matriz


filas = int(input())
columnas = int(input())
matriz = matrizfinal(filas, columnas) 
resultado = suma_diagonal(filas, columnas, matriz)
print(resultado)
