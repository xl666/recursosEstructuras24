def contar_puntos(cadena):
    contador = 0
    continuo = False
    for c in cadena:
        if c == '.' and not continuo:
            contador += 1
            continuo = True
        elif c != '.':
            continuo = False
    return contador

if __name__ == '__main__':
    cadena = input()
    print(contar_puntos(cadena))