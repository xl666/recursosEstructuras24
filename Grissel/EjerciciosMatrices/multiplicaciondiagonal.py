def crear_matriz_cuadrada(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            valor = int(input())
            fila.append(valor)
        matriz.append(fila)
    return matriz

def multiplicar_en_diagonal(matriz, factor):
    for i in range(len(matriz)):
        matriz[i][i] *= factor
    return matriz

if __name__ == '__main__':
    n = int(input("Ingrese el tamaño de la matriz cuadrada: "))
    matriz = crear_matriz_cuadrada(n)
    print("Matriz original:")
    for fila in matriz:
        print(fila)

    factor = int(input("Ingrese el valor para multiplicar en la diagonal: "))
    resultado = multiplicar_en_diagonal(matriz, factor)

    print("Matriz después de la multiplicación en diagonal:")
    for fila in resultado:
        print(fila)
