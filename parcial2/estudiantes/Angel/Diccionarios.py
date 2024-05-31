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

def leer_diccionario(elementos: int) -> dict:
    """
    Lee un diccionario desde entrada estándar.
    Las llaves son cadenas y los valores enteros

    elementos: int
    returns: dict 
    """
    res = {}
    for _ in range(elementos):
        llave = input()
        valor = int(input())
        res[llave] = valor

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


def generar_diccionario_inverso(diccionario: dict) -> dict:
    inverso = {}
    for palabra, frecuencia in diccionario.items():
        if frecuencia not in inverso:
            inverso[frecuencia] = []
        inverso[frecuencia].append(palabra)
    return inverso

# Ejemplo de uso
if __name__ == '__main__':
    #cadena = input()
    #frecuencias  =  generar_dicionario(cadena)
    #imprimir_resultado(frecuencias)
    cadena = "Hola mundo mundo esto es una prueba prueba"
    frecuencias = leer_diccionario(cadena)
    diccionario_inverso = generar_diccionario_inverso(frecuencias)
    print(diccionario_inverso)
