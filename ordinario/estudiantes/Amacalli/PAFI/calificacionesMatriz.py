def calificaciones (matriz):
    f = len(matriz)
    c = len(matriz[0])
    res = 0
    promedio = []
    for i in range(c):
        for j in range(f):
            res += matriz[j][i]
        res = res / f
        promedio.append(round(res, 1))
    return promedio


if __name__ == '__main__':
    matriz = [[6, 7, 8], [10, 7, 6], [8, 5, 7], [9, 10, 5]]
    print(calificaciones(matriz))