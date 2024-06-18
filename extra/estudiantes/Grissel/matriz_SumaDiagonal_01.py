def suma_diagonal(matriz):
    filas = len(matriz)
    columnas = filas
    res = 0
    for posicion in range(columnas):
        res = res + matriz[posicion][posicion]
    return res
    
def leer_matriz(filas, columnas):
    matriz = []
    for f in range(filas):
        ff = []
        for c in range(columnas):
            ff.append(int(input()))
        matriz.append(ff)
    return matriz

if __name__ == '__main__':
    filas = int(input())
    columnas = int(input())
    matriz = leer_matriz(filas, columnas) #entrada: filas y columnas --> matriz cuadrada o no
    print(suma_diagonal(matriz))