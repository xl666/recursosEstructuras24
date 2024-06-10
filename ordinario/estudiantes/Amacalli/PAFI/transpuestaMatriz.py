def transpuesta(matriz):
    f = len(matriz)
    c = len(matriz[0])
    #mtriz2 = [0 for _ in range(c)]
    mtriz2 = []
    for fila in range(f):
        mtriz2.append([])
        for columna in range(f):
            mtriz2[fila].append(matriz[columna][fila])
    return mtriz2
"""
    for i in range(c):
        aux = [0] * f
        mtriz.append(aux)
    for i in range(f):
        for j in range(c):
            mtriz2[j][i] = matriz[i][j]
    return mtriz2
"""

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpuesta(matriz))
