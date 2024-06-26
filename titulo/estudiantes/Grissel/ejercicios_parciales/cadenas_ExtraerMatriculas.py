def extrae_matricula(n, matriculas):
    matriculas = []
    for cadena in cadenas:
        partes = cadena.split('(')
        # print(partes) = ['Pepe Pecas López ', 'S20013851)']
        partes2 = partes[1].split(')')[0]
        matriculas.append(partes2)
    return matriculas

if __name__ == '__main__':
    n = int(input())
    cadenas = []
    for _ in range(n):
        matricula = input()
        cadenas.append(matricula)
    #print(cadenas)
    matriculas = extrae_matricula(n, cadenas)
    for matricula in matriculas:
        print(matricula)