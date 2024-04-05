def quitar_elemento(elemento, lista):
    return [x for x in lista if x != elemento]

if __name__ == '__main__':
    v = int(input())
    n = int(input())
    lista = [int(input()) for _ in range(n)]
    print(quitar_elemento(v, lista))
