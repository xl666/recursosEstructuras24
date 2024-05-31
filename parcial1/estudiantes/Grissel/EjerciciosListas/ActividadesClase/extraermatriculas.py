def obtener_matriculas(Num_cadenas, cadenas):
    return [cadena.split('(')[1].split(')')[0] for cadena in cadenas]

if __name__ == '__main__':
    Num_cadenas = int(input())
    cadenas = [input() for _ in range(Num_cadenas)]
    matriculas = obtener_matriculas(Num_cadenas, cadenas)
    for matricula in matriculas:
        print(matricula)

