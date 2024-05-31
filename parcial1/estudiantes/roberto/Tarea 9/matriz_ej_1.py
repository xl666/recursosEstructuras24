def ingresar_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            #ingresar valores de la matriz
            valor = int(input())
            fila.append(valor)
        matriz.append(fila)
    return matriz

def sumar_diagonal_principal(matriz):
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][i]
    return suma
#ingresar numero de filas
filas = int(input())
#ingresar numero de columnas
columnas = int(input())

matriz = ingresar_matriz(filas, columnas)

#imprimir matriz:
#print("La matriz ingresada es:")
#for fila in matriz:
   # print(fila)

suma_diagonal_principal = sumar_diagonal_principal(matriz)
print(suma_diagonal_principal)
