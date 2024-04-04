def interseccion_listas(lista1, lista2):
    set1 = set(map(int, lista1.split(',')))
    set2 = set(map(int, lista2.split(',')))
    interseccion = set1.intersection(set2)
    resultado = sorted(list(interseccion))
    return resultado

if __name__ == "__main__":
    N = int(input())
    M = int(input())

    lista1 = input()
    lista2 = input()

    resultado = interseccion_listas(lista1, lista2)
    print(resultado)