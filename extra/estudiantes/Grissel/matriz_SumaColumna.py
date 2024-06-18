def leer_matriz(filas, columnas):
    matriz = []
    for f in range(filas):
        ff = []
        for c in range(columnas):
            ff.append(int(input()))
        matriz.append(ff)
    return matriz

def sumar_columnas(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    res = [0 for _ in range(columnas)]
    for f in range(filas):
        for c in range(columnas):
           res[c] += matriz[f][c]
    return res

def dar_formato(lista):
    lista_cadenas = [str(ele) for ele in lista]
    return ','.join(lista_cadenas)

if __name__ == '__main__':
    filas = int(input())
    columnas = int(input())
    matriz = leer_matriz(filas, columnas)
    print(dar_formato(sumar_columnas(matriz)))