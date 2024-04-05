def suma_diagonal(matriz):
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][i]
    return suma

if __name__ == "__main__":
    F, C = map(int, input().split(','))
    matriz = []
    for _ in range(F):
        fila = list(map(int, input().split(',')))
        matriz.append(fila)
        resultado = suma_diagonal(matriz)
        print(resultado)






