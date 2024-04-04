def producto(lista):
    prod = 1
    for i in lista:
        prod *= i
    return prod    




if __name__ == '__main__':
    n=int(input())
    lista = []
    for _ in range(n):
        lista.append(int(input()))
    resultado = producto(lista)
    print(resultado)