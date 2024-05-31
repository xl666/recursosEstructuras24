def llenar_matriz(f, c):
    matriz = []
    for filas in range(f):
        ff = []
        for columnas in range(c):
            ff.append(int(input()))
        matriz.append(ff)
    return matriz

def sumar_diagonal(matriz):
    f = len(matriz)
    c = f
    suma = 0
    for posicion in range(c):
        suma = suma + matriz[posicion][posicion]
    return suma
            
if __name__ == '__main__':
    f = int(input())
    c = int(input())
    matriz = llenar_matriz(f, c)
    print(sumar_diagonal(matriz))