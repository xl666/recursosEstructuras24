def contarPalabras(cadena):
    cont = 0
    cad = cadena.split(' ')
    
    for i in range(len(cad)):
        if cad[i] != '':
            cont += 1
    return cont


if __name__ == '__main__':
    cadena = input()
    print(contarPalabras(cadena))