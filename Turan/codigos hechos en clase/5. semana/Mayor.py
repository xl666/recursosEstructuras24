def lista(n):
    lista=[]
    for i in range(n):
        i = int(input())
        lista.append(i)
    return lista
def mayor(lista):
    mayor= lista[0]
    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
    return mayor

if __name__=='__main__':
    n= int(input())

    m1 = mayor(lista(n))
    print(m1)
    