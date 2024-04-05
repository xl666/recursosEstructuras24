def crear_matriz_cuadrada(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            valor = int(input())
            fila.append(valor)
        matriz.append(fila)
    return matriz

def multiplicar_diagonal(matriz):
    resultado = 1
    for i in range(len(matriz)):
        resultado *= matriz[i][i]
    return resultado

if __name__ == '__main__':
    n = int(input("Ingrese el tamaño de la matriz cuadrada: "))
    matriz = crear_matriz_cuadrada(n)
    print("Matriz:")
    for fila in matriz:
        print(fila)

    resultado = multiplicar_diagonal(matriz)
    print("Resultado de la multiplicación en diagonal:", resultado)
