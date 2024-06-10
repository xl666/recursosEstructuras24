def invertir(cadena):
    invertida = ''
    #cadena[::-1]
    for i in range(1,len(cadena)):
        invertida += cadena[-i]
    invertida += cadena[0]
    return invertida


if __name__ == '__main__':
    cadena = input()
    print(invertir(cadena))