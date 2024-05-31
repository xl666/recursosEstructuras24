# casos base:
# - lista vacia
# - que haya numeros repetidos

def elimina_repetido_rec(elementos: list, lista: list) -> list:
    """

    Imprime los elementos de una lista sin repeticiones

    lista: list
    returns: list

    """
    if not lista:
        return elementos
    frente = lista[0]
    resto = lista[1:]
    if frente not in elementos:
        elementos.append(frente)
    return elimina_repetido_rec(elementos, resto)

if __name__ == '__main__':
    n = int(input())
    lista = [input() for _ in range(n)]
    elementos = elimina_repetido_rec([], lista)
    print(elementos)