def generar_dicionario(cadena:str) -> dict:
    """
    Cuenta frecuencia de palabras y
    guarda el resultado en un diccionario.

    caden:str, cadena con varias palabras
    returns: dict 
    """
    palabras = cadena.split(' ')
    res = {}
    for palabra in palabras:
        if palabra in res:
            res[palabra] += 1
        else:
            res[palabra] = 1

    return res


def imprimir_resultado(diccionario: dict) -> None:
    """
    Imprime el resultado como lo  espera
    el sistema.

    diccionario: dict
    returns: None 
    """
    llaves_ordenadas = sorted(diccionario.keys())
    for llave in llaves_ordenadas:
        print('%s: %s' % (llave, diccionario[llave]))

if __name__ == '__main__':
    cadena = input()
    frecuencias  =  generar_dicionario(cadena)
    imprimir_resultado(frecuencias)
