
def reversa(cadena):
    if not cadena:
        return ''
    res = ''
    for i in range(1, len(cadena)):
        res += cadena[-i]
    return res + cadena[0]

def es_palindromo(cadena):
    return cadena == reversa(cadena)

def es_palindromo2(cadena):
    return cadena == cadena[::-1]

if __name__ == '__main__':
    cadena = input()
    print(es_palindromo(cadena))
