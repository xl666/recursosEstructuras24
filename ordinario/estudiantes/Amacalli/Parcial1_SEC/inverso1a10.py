def inverso(lista):
    for i in range(1, len(lista)):
        print(lista[-i], '\t')
    print(lista[0])

if __name__ == '__main__':
    lista = []
    for _ in range(9):
        lista.append(int(input()))

    inverso(lista)