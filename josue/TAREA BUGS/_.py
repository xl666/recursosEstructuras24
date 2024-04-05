def obtener_matriculas(n, cadenas):
    matriculas = []

    for cadena in cadenas:
        partes = cadena.split('(')
        matricula = partes[1].strip(')')

        matriculas.append(matricula)

    return matriculas


if __name__ == '__main__':
    n = int(input())
    cadenas_alumnos = [input() for _ in range(n)]

    matriculas_resultantes = obtener_matriculas(n, cadenas_alumnos)

    for matricula in matriculas_resultantes:
        print(matricula)

