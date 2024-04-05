def suma_diagonal_matriz(F, C, matriz):
    if F != C:
        return
    suma = 0

    for i in range(F):
        suma += matriz[i][i]

    return suma


F = int(input())
C = int(input())

matriz = []
print()
for i in range(F):
    fila = []
    for j in range(C):
        elemento = int(input())
        fila.append(elemento)
    matriz.append(fila)

resultado = suma_diagonal_matriz(F, C, matriz)
if isinstance(resultado, int):
    print(resultado)
else:
    print(resultado)
