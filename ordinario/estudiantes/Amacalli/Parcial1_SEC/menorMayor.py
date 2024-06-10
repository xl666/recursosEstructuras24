def menor(lista):
    l = sorted(lista)
    for i in range(len(l)):
        print(l[i])

if __name__ == '__main__':
    n = int(input())
    lista = []
    for _ in range(n):
        lista.append(int(input()))

    menor(lista)