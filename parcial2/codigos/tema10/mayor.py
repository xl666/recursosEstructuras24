
# recursividad no a la cola
def mayor_rec(lista: list, mayor: int) -> int:
    """
    Regresa el número mayor, requiere inicialización.

    
    returns: None 
    """
    if not lista: # lista vacía
        return mayor
    frente = lista.pop()
    if frente > mayor:
        return mayor_rec(lista, frente)
    return mayor_rec(lista, mayor)

def mayor_lista(lista: list) -> int:
    """
    Regresa el mayor de la lista.

    lista: list
    returns: int 
    """
    lista = lista[:]
    if not lista:
        return -1
    mayor = lista.pop()
    return mayor_rec(lista, mayor)

# recursividad a la cola
def mayor_rec2(lista):
    if not lista:
        return -1
    frente = lista[0]
    resto = lista[1:]
    if not resto: # la lista tenía un solo elemento
        return frente
    mayor_resto = mayor_rec2(resto)
    if frente > mayor_resto:
        return frente
    else:
        return mayor_resto
        


if __name__ == '__main__':
    n = int(input())
    l = [input() for _ in range(n)]
    print(mayor_lista(l))
    
