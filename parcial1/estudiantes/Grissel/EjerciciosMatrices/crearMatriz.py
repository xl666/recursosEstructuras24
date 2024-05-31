def crear_matriz(F, C):
    matriz = []
    for _ in range(F):
        fila = []
        for _ in range(C):
            valor = int(input())
            fila.append(valor)
        matriz.append(fila)
    return matriz

if __name__ == '__main__':
    F = int(input("Ingrese el número de filas de la matriz: "))
    C = int(input("Ingrese el número de columnas de la matriz: "))
    matriz = crear_matriz(F, C)
    print("Matriz:")
    for fila in matriz:
        print(fila)