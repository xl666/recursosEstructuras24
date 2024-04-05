# CÓDIGO GÉNERICO ---> podemos tomarlo para el examen 
def leer_matriz(F, C):
    matriz = []
    for fila in range(F):
        ff = []
        for columna in range (C):
            ff.append(int(input()))
        matriz.append(ff)
    return matriz

def calcular_suma_diagonal(matriz):
    F = len(matriz)
    C = F #ES CUADRADA
    res = 0
    for pos in range(C):
        res += matriz[pos][pos]
    return res

if __name__ == '__main__':
    F = int(input())
    C = int(input()) 
    matriz = leer_matriz(F, C)
    print(calcular_suma_diagonal(matriz))