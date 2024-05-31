
def Encontrar(lista):
    return max(lista)

if __name__ == '__main__':
    longitud = int(input())
    lista = []

    if longitud <= 0:
        print('Hay un error')
    else:
        for i in range(longitud):
            lista.append(int(input()))
        print(Encontrar(lista))