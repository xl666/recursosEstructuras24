
def extraer_matricula(cadena):
    return cadena.split('(')[1][:-1]


def procesar_cadenas(cadenas):
    res = []
    for cadena in cadenas:
        res.append(extraer_matricula(cadena))
    return res

if __name__ == '__main__':
    n_cadenas = int(input())
    cadenas = []
    for _ in range(n_cadenas):
        cadenas.append(input())
    matriculas = procesar_cadenas(cadenas)
    for matricula in matriculas:
        print(matricula)

