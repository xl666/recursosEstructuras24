def pertenece(elemento: str, lista: list) -> bool:
    """

    Determina si elemento pertenece a lista vacía
    elemento: str, lista: list
    return: bool

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

    # casos base: siempre podemos devolver un valor
    # - lista vacía, el frente de la lista es el elemento que buscamos

    # casos recursivos: 
    # - el frente de la lista 