def crear_matriz(F, C):
    matriz = []
    for _ in range(F):
        fila = []
        for _ in range(C):
            valor = int(input())
            fila.append(valor)
        matriz.append(fila)
    return matriz

def multiplicar_matrices(matriz1, matriz2):
    if len(matriz1[0]) != len(matriz2):
        return "No se puede multiplicar, el número de columnas de la primera matriz no coincide con el número de filas de la segunda matriz."
    resultado = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz2[0])):
            suma = 0
            for k in range(len(matriz2)):
                suma += matriz1[i][k] * matriz2[k][j]
            fila.append(suma)
        resultado.append(fila)
    return resultado

if __name__ == '__main__':
    F1 = int(input("Ingrese el número de filas de la primera matriz: "))
    C1 = int(input("Ingrese el número de columnas de la primera matriz: "))
    matriz1 = crear_matriz(F1, C1)

    F2 = int(input("Ingrese el número de filas de la segunda matriz: "))
    C2 = int(input("Ingrese el número de columnas de la segunda matriz: "))
    matriz2 = crear_matriz(F2, C2)

    resultado = multiplicar_matrices(matriz1, matriz2)
    print("Resultado de la multiplicación de matrices:")
    for fila in resultado:
        print(fila)