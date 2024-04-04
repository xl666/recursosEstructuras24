#ingresar numero de filas
filas = int(input())
#ingresar numero de columnas
columnas = int(input())

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

matriz = ingresar_matriz(filas, columnas)

sumas_columnas = [0] * columnas


for fila in matriz:
    for j in range(columnas):
        sumas_columnas[j] += fila[j]

resultado = ",".join(str(suma) for suma in sumas_columnas)

print(resultado)


