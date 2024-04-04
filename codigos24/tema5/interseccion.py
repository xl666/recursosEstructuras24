
def interseccion(l1, l2):
    s1 = set(l1)
    s2 = set(l2)
    inter = s1.intersection(s2)
    res = list(inter)
    return sorted(res)

def interseccion2(l1, l2):
    res = []
    for elemento in l1:
        if elemento in l2 and not elemento in res:
            res.append(elemento)

    return sorted(res)


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    l2 = [int(input()) for _ in range(m)]
    l1 = [int(input()) for _ in range(n)]
    print(interseccion2(l1, l2))
