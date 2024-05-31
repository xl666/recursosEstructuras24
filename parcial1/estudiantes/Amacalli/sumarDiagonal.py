def sumarDiagonal(matriz):
    suma = 0
    for f in range(len(matriz)):
        suma += matriz[f][f]
    return suma

if __name__ == '__main__':
    f = int(input())
    c = int(input())

    if c == f:
        matriz = []
        for mf  in range(f):
            fila = []
            for mc in range(c):
                fila.append(int(input()))
            matriz.append(fila)
        print(sumarDiagonal(matriz))