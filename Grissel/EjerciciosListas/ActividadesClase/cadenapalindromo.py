def reversa(cadena):
    if not cadena:
        return ''
    res = ''
    for i in range(1, len(cadena)):
       res += cadena[-i]
    return res + cadena[0] 

def es_palindromo(cadena):
    return cadena == reversa(cadena)
    #pass #pass es q está pendiente

if __name__=='__main__':
    cadena = input()
    print(es_palindromo(cadena))

    
