
"""
1.- Hacer una copia del primer diccionario
2.- Recorrer el segundo diccionario
   - Si la llave está en la copia:
     - Cambiar valor asociado a la llave con la suma
   - No está la llave
     - Agregar llave a la copia con el mismo valor
"""


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


def unir_diccionarios(diccionario1: dict, diccionario2: dict) -> dict:
    """
    Une los diccionarios de entrada (llave str, valor int),
    si hay llaves que coinciden realiza una suma.

    diccionario1,
    diccionario2
    returns: dict 
    """
    res = diccionario1.copy() # evitar efecto colateral
    for llave in diccionario2:
        if llave in res.keys():
            res[llave] += diccionario2[llave]
        else:
            res[llave] = diccionario2[llave]

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
    n = int(input())
    m = int(input())
    diccionario1 = leer_diccionario(n)
    diccionario2 = leer_diccionario(m)
    resultado = unir_diccionarios(diccionario1, diccionario2)
    imprimir_resultado(resultado)
