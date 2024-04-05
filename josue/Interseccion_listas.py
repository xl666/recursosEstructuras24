def llenar_lista(a, b):
    l = []
    l2 = []
    for i in range(a):
        elemento = int(input())
        l.append(elemento)
    for i in range(b):
        elemento = int(input())
        l2.append(elemento)
    return l, l2

def pares_lista(l, l2):
    l3 = []
    for i in range(len(l)):
        for j in range(len(l2)):
            if l[i] == l2[j] and l[i] not in l3:
                l3.append(l[i])
    return l3

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    lista1, lista2 = llenar_lista(a, b)
    lista_interseccion = pares_lista(lista1, lista2)

    lista_interseccion.sort()
    print(lista_interseccion)

