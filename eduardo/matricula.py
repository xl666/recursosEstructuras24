def obtener_matriculas(num_cadenas, cadenas):
    matriculas = []
    for i in range(num_cadenas):
        indice_inicio = cadenas[i].find('(')
        indice_fin = cadenas[i].rfind(')')
        matriculas.append(cadenas[i][indice_inicio + 1 : indice_fin])
    return matriculas

num_cadenas = int(input())
cadenas = [input() for _ in range(num_cadenas)]

matriculas = obtener_matriculas(num_cadenas, cadenas)

for matricula in matriculas:
    print(matricula)