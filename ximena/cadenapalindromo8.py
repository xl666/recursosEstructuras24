# Dada una cadena de entrada determina si es un palíndromo, un palíndromo es una cadena que se lee igual de izquierda a derecha y de derecha a izquierda
def reversa(cadena):
    if not cadena:
        return ""
    res = ""
    for i in range(1, len(cadena)):
        res += cadena[-i]
    return res + cadena[0]
        

def es_palindromo(cadena):
    return cadena == reversa(cadena)

if __name__ == "__main__":
    cadena = input()
    print (es_palindromo(cadena))