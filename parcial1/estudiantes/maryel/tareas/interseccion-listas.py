def interseccion_listas():
    tamaño1 = int(input(''))
    tamaño2 = int(input(''))

    l1 = list(map(int, input('').split()))
    l2 = list(map(int, input('').split()))

    interseccion = list(set(l1) & set(l2))

    interseccion.sort()

    print(interseccion)


interseccion_listas()
