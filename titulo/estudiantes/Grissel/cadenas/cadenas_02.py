def contar_puntos(cadena):
    contador = 0
    caracter_siguiente = ''
    for caracter in cadena:
        if caracter == '.' and caracter_siguiente != '.':
            contador += 1
        caracter_siguiente = caracter
    return contador

if __name__ == '__main__':
    cadena = input()
    print(contar_puntos(cadena))
    