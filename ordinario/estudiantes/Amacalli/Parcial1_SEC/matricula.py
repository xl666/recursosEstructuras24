def extraer_matricula (cadena):
    return cadena.split('(')[1][:-1]

def leerCadenas (n_elementos):
    cadenas = []
    for cadena in range(n_elementos):
        cadenas.append(input())
    return cadenas

if __name__ == '__main__':
    n_elementos = int(input())
    cadena = leerCadenas(n_elementos)
    print("\n", extraer_matricula(cadena))