def eliminar_repetidos(lista, copia):
    if not lista:
        return copia
    if lista[0] in copia:
        return eliminar_repetidos(lista[1:], copia)
    else:
        copia.append(lista[0])
        return eliminar_repetidos(lista[1:], copia)       


if __name__ == '__main__':
    n = int(input())
    lista = []
    copia = []

    for _ in range(n):
        lista.append(int(input()))

    copia1 = eliminar_repetidos(lista, copia)

    print(copia1)
