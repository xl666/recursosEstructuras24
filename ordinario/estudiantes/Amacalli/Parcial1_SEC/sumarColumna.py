def sumar_columnas(matriz):
    filas = len(matriz)
    columnas = len(matriz[0]) if filas > 0 else 0

    if columnas == 0:
        return ""

    suma_columnas = [0] * columnas

    for fila in matriz:
        for j in range(columnas):
            suma_columnas[j] += fila[j]

    return ','.join(map(str, suma_columnas))

if __name__ == '__main__':
    f = int(input())
    c = int(input())

    matriz = []

    for mf in range(f):
        fila = []
        for mc in range(c):
            fila.append(int(input()))
        matriz.append(fila)

    print(sumar_columnas(matriz))