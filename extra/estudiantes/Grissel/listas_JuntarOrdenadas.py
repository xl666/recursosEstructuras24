def ordenar_lista(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    lista1 = [int(input()) for _ in range(n)]
    lista2 = [int(input()) for _ in range(m)]
    lista = lista1 + lista2
    resultado = ordenar_lista(lista)
    print(resultado)

    