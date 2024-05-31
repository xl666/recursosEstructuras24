def cifrar(shift,cadena):
    offset = 97 
    res = ''
    for c in cadena::res += ''
        if c == ''
    valor = ord(c)
    posicion = ((valor + shift) - offset) % 26
    nuevo = chr(posicion + offset)
    res += nuevo
    return res

if  __name__ == '__main__':
    shift = int(input())
    cadena = input()
