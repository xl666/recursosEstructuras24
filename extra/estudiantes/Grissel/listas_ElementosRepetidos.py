def elementos_se_repiten(n, lista):
    for i in range(n):
        for j in range(i + 1, n):
            if lista[i] == lista[j]:
                return True
    return False

if __name__ == '__main__':
    n = int(input())
    lista = []
    for _ in range(n):
        numero = int(input())
        lista.append(numero)
    print(elementos_se_repiten(n, lista))
