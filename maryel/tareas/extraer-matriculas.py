def extraer_matriculas(total, cadenas):
    for cadena in cadenas:
        partes = cadena.split('(')
        matricula = partes[1].strip(')')
        print(matricula)


total = int(input())
cadenas = [input() for x in range(total)]

extraer_matriculas(total, cadenas)
