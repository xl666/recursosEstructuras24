def matrizResultado(m1, m2):
    f1 = len(m1)
    c2 = len(m2[0])
    out = []
    for i in range(f1):
        aux = [0] * c2
        out.append(aux)
    return out

def multipliacion(m1, m2):
    resultante = matrizResultado(m1, m2)
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            cont = 0
            for k in range(len(m1[0])):
                cont = cont + (m1[i][k] * m2[k][j])
            resultante[i][j] = cont
    return resultante


if __name__ == '__main__':
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m2 = [[1, 2, 3], [3, 2, 1], [1, 2, 3]]

    if len(m1) == len(m2[0]):
        print(multipliacion(m1, m2))
