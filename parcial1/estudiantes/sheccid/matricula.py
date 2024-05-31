def obtener_matriculas(numero_cadenas, cadenas):
    matriculas = []

    for i in range(numero_cadenas):
        _, matricula = cadenas[i].split('(')
        matricula = matricula.rstrip(')').strip()
        matriculas.append(matricula)

    return matriculas

def main():
    numero_cadenas = int(input())
    cadenas = [input() for _ in range(numero_cadenas)]

    matriculas = obtener_matriculas(numero_cadenas, cadenas)

    for matricula in matriculas:
        print(matricula)

if __name__ == "__main__":
    main()
