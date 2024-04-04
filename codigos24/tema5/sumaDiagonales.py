
def leer_matriz(f, c):
    matriz = []
    for fila in range(f):
        ff = []
        for columna in range(c):
            ff.append(int(input()))
        matriz.append(ff)
    return matriz

def calcular_suma_diagonal(matriz):
    f = len(matriz)
    c = f # es cuadrada
    res = 0
    for pos in range(c):
        res += matriz[pos][pos]
    return res
      

if __name__ == '__main__':
    f = int(input())
    c = int(input())
    matriz = leer_matriz(f, c)
    print(calcular_suma_diagonal(matriz))
