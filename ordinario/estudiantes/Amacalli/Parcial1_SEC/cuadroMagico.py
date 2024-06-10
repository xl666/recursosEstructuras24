def sumaFila(matriz):
    pass

def sumaColumna(matriz):
    pass

def sumadiagonal(matriz):
    pass

if __name__ == '__main__':
    f = int(input())
    c = int(input())

    if c == f:
        matriz = []

        for _ in range(f):
            fila = []
            for _ in range(c):
                fila.append(int(input()))
            matriz.append(fila)

         