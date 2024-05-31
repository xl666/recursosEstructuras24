






def pertenece(elemento: str, lista: list) -> bool:
    """
    Determina si elemento pertenece a lista.

    elemento: str, lista: list
    returns: bool 
    """
    if not lista:
        return False
    frente = lista[0]
    resto = lista[1:]
    if frente == elemento:
        return True
    return pertenece(elemento, resto)

if __name__ == '__main__':
    x = input()
    n = int(input())
    lista = [input() for _ in range(n)]
    print(pertenece(x, lista))
