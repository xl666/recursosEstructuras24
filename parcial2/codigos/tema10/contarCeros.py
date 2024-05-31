
def contar_ceros2_rec(cadena, contador):
    if not cadena:
        return contador
    frente = cadena[0]
    resto = cadena[1:]

    if frente == '0':
        return contar_ceros2_rec(resto, contador + 1)
    else:
        return contar_ceros2_rec(resto, contador)

def contar_ceros2(cadena):
    return contar_ceros2_rec(cadena, 0)

def contar_ceros(cadena):
    if not cadena:
        return 0
    frente = cadena[0]
    resto = cadena[1:]
    if frente == '0':
        return 1 + contar_ceros(resto)
    else:
        return contar_ceros(resto)


if __name__ == '__main__':
    cadena = input()
    print(contar_ceros(cadena))
