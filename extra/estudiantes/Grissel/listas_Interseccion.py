def interseccion(lista1, lista2):
    resultado = []
    if len(lista1) > len(lista2):
        mayor = lista1
        menor = lista2
    else:
        mayor = lista2
        menor = lista1
    for elemento1 in mayor:
        for elemento2 in menor:
            if elemento1 == elemento2 and not elemento2 in resultado:
                resultado.append(elemento2)
    resultado.sort()
    return resultado

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    lista1 = [int(input()) for _ in range (n)]
    lista2 = [int(input()) for _ in range (m)]
    resultado = interseccion(lista1, lista2)
    print(resultado)