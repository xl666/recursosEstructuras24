def multiplicar_matrices_no_cuadradas(matriz1, matriz2):
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
    matriz1 = [[1, 2, 3], [4, 5, 6]]
    matriz2 = [[7, 8], [9, 10], [11, 12]]
    resultado = multiplicar_matrices_no_cuadradas(matriz1, matriz2)
    print("Matriz resultado:")
    for fila in resultado:
        print(fila)