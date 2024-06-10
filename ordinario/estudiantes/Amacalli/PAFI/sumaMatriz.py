def suma(matriz, matriz2):
    f = len(matriz)
    c = len(matriz[0])
    
    mtriz2 = []
    for fila in range(f):
        mtriz2.append([])
        for columna in range(f):
            mtriz2[fila].append(matriz2[fila][columna] + matriz[fila][columna])
    """
    for i in range(f):
        aux = [] * c
        mtriz2.append(aux)
    for i in range(f):
        for j in range(c):
            mtriz2[i][j] = matriz[i][j] + matriz2[i][j]

    """
    return mtriz2  


matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(suma(matriz, matriz2))