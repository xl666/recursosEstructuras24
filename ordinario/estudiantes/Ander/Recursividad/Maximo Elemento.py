# Desarrollar una función recursiva para encontrar
# el máximo elemento en una lista.

def llenar_lista_rec(l: list, n: int) -> list:
    if not n:
        return l
    l.append(int(input()))
    return llenar_lista_rec(l, n - 1)

def maximo_elemento_rec(l: list, max: int=None) -> int:
    if not l:
        return l
    if len(l) == 1:
        return max
    if not max:
        max = l[0]
    if l[1] > max:
        max = l[1]
    return maximo_elemento_rec(l[1:], max)

if __name__=='__main__':
    l = []
    n = int(input())
    l = llenar_lista_rec(l, n)
    print(maximo_elemento_rec(l))