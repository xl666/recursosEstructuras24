def interseccion_listas(lista1, lista2):
    set1 = set(int(num) for num in lista1)
    set2 = set(int(num) for num in lista2)
    interseccion = sorted(list(set1.intersection(set2)))
    return interseccion

if __name__ == "__main__":
    N = int(input())
    M = int(input())

    lista1 = input().split(', ')
    lista2 = input().split(', ')

    resultado = interseccion_listas(lista1, lista2)
    print(resultado)