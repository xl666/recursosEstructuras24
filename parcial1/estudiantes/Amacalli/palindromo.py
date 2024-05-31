def reversa (cadena):
    if not cadena:
        return ''
    
    resultado = ''
    for i in range(1, len(cadena)):
        resultado += cadena[-i]
    return resultado + cadena[0]

def es_palindromo (cadena):
    return cadena == reversa(cadena)

if __name__ == '__main__':
    cadena = input()
    print(es_palindromo(cadena))


