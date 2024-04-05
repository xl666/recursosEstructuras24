#Dada una matriz de enteros de F * C dimensiones, regresa la sumatoria de cada una de las columnas
#Ejemplo de entrada
#3,4
#1,2,3,4
#1,2,3,4
#1,2,3,4
#Ejemplo de salida
#3,6,9,12
def leer_matriz(f, c):
    matriz = []
    for fila in range(f):
        ff = []
        for columna in range(c):
            ff.append(int(input()))
        matriz.append(ff)
    return matriz

def sumar_columnas(matriz):
    f = len(matriz)
    c = len(matriz[0])
    res = [0 for _ in range(c)]
    for fila in range(f):
        for columna in range(c):
           res[columna] += matriz[fila][columna]
    return res

def dar_formato(lista):
    lista_cadenas = [str(ele) for ele in lista]
    return ','.join(lista_cadenas)

if __name__ == '__main__':
    f = int(input())
    c = int(input())
    matriz = leer_matriz(f, c)
    print(dar_formato(sumar_columnas(matriz)))