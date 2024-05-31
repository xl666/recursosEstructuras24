
def reversa(cadena):
    if not cadena:
        return ''
    resul = ''
    for i in range(1, len(cadena)):
        res += cadena[-i]
        return resul + cadena[0]


def es_palindromo(cadena):
    return cadena == reversa(cadena)


cadena = input()
print(es_palindromo(cadena))
