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

def unir_diccionario(diccionario1, diccionario2):
    suma = {}
    for llave in diccionario1:
        suma[llave] = diccionario1[llave]
    for llave in diccionario2:
        if llave in suma.keys():
            suma[llave] = diccionario2[llave] + suma[llave]
        else:
            suma[llave] = diccionario2[llave]
    return suma

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
    imprimir_resultado(unir_diccionario(diccionario1, diccionario2))
