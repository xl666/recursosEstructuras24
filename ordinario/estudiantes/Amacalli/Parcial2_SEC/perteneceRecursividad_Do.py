def pertenece(elemento: str, lista: list) -> None:
    """
    Determina si el elemento pertence a la lista
    """
    if not lista:
        return False
    frente = lista[0]
    resto = lista[1:]
    if frente == elemento:
        return True
    return pertenece(elemento, resto)

if __name__ == '__main__':
    x = int(input())
    n = int(input())
    lista = [int(input()) for _ in range(n)]
    print(pertenece(x, lista))