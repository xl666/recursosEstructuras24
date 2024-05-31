# forma 1
def quitar_elemento(elemnto, lista):
    return [x for x in lista if x != elemnto]


# forma 2
def quitar_elemnto2(elemnto, lista):
    res = []
    for x in lista:
        if x != elemnto:
            res.append(x)
    return res


if __name__ == '__main__':
    v = int(input())
    n = int(input())
    lista = [int(input())for _ in range(n)]
    print(quitar_elemento(v, lista))
