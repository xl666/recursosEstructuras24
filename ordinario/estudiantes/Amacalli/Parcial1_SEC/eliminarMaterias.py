def eliminarMaterias(mate, prome):
    for i in range(len(prome)):
        if prome[i] >= 6:
            mate.remove(mate[i])

    print('Debes repetir estas materias: ')
    for materia in mate:
        print(materia)


if __name__ == '__main__':
    n = int(input('Ingresa el numero de materias que cursas: '))
    lista = []
    mate = []
    prome = []

    for _ in range(n):
        mate.append(input('Ingresa el nombre de la materia: '))

    for materia in mate:
        prome.append(int(input('Ingresa la calificación de %s: ' % materia)))
    
    eliminarMaterias(mate, prome)