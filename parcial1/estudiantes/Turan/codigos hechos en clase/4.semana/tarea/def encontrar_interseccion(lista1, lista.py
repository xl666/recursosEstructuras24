def compara(lista1, lista2):
    lista_ordenado = sorted(list(set(lista1).intersection(lista2)))
    return lista_ordenado

if __name__ == "__main__":
    N = int(input())
    M = int(input())
    lista_1 = [int(input()) for _ in range(N)]
    lista_2 = [int(input()) for _ in range(M)]

    resultado = compara(lista_1, lista_2)
    print(resultado)
