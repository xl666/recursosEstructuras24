#Inserta un caracter donde hay un caracter especial


def insertar(frase, cadena):
    cadena2 = ''
    for i in range(len(cadena)):
        if cadena[i] == '#':
            cadena2 += frase
        else:
            cadena2 += cadena[i]

    cadena = cadena.split(" ")
    for i in range(len(cadena)):
        if cadena[i] == '#':
            cadena = frase
    cadena = cadena.join(' ')

    return cadena

if __name__ == '__main__':
    frase = input()
    cadena = input()
    print(insertar(frase, cadena))