def contar_puntos(cadena):
    con = 0
    i = 0
    while i < len(cadena):
        if cadena[i] == '.':
            con += 1
            while i < len(cadena) and cadena[i] == '.':
                i += 1
        else:
            i += 1
    return con

cadena = input()
resultado = contar_puntos(cadena)
print(resultado)
