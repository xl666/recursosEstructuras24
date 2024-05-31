def suma_columnas(F, C):
    if F <= 0 or C <= 0:
        return

    matriz = []

    for i in range(F):
        fila = []
        for j in range(C):
            valor = int(input())
            fila.append(valor)
        matriz.append(fila)

    sumas_columnas = [0] * C
    for i in range(F):
        for j in range(C):
            sumas_columnas[j] += matriz[i][j]

    salida = ",".join(map(str, sumas_columnas))
    return salida


F = int(input())
C = int(input())

resultado = suma_columnas(F, C)
print(resultado)
