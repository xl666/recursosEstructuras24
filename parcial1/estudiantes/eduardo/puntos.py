def contar_puntos(cadena):
    contador_puntos = 0
    for i in range(len(cadena)):
        if cadena[i] == '.':
            if i == 0 or cadena[i - 1] != '.':
                contador_puntos += 1
    return contador_puntos

texto = input()
print(contar_puntos(texto))
