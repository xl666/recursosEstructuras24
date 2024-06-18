# entrada: un número * numero --> matriz cuadrada
def leer_matriz(filas, columnas):
    matriz = []
    for f in range(filas):
        ff = []
        for c in range(columnas):
            ff.append(int(input()))
        matriz.append(ff)
    return matriz

def suma_diagonal(matriz):
    filas = len(matriz)
    columnas = filas
    res = 0
    for posicion in range(columnas):
        res = res + matriz[posicion][posicion]
    return res

if __name__ == '__main__':
    filas = int(input()) # entrada: un número * numero --> matriz cuadrada
    matriz = leer_matriz(filas, filas)
    print(matriz)
    print(suma_diagonal(matriz))    