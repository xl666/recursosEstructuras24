def coding(cadena):
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cadena2 = ''
    for i in (cadena):
        if i == ' ' :
            cadena2 += ' '
        elif i in abc:
            x = int((abc.index(i) +5) % 26)
            cadena2 += abc[x]
    return cadena2


cadena = str(input())
cadena2 = coding(cadena)
print(cadena2)