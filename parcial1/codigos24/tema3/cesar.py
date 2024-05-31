
def cifrar(shift, cadena):
    offset = 97 # a minúscula
    res = ''
    for c in cadena:
        if c == ' ':
            res += ' '
            continue
        valor = ord(c)
        pos = ((valor + shift) - offset) % 26
        nuevo = chr(pos + offset)
        res += nuevo
    return res

if __name__ == '__main__':
    shift = int(input())
    cadena = input()
    print(cifrar(shift, cadena))

