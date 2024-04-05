def contar_puntos(cadena):
    count = 0
    i = 0
    while i < len(cadena):
        if cadena[i] == '.':
            count += 1
            while i < len(cadena) and cadena[i] == '.':
                i += 1
        else:
            i += 1
    return count


cadena = input()
print(contar_puntos(cadena))
