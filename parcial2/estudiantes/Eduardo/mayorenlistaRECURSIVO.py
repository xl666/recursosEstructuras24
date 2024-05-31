def mayor_rec(lista: list, mayor: int) -> int:
    """
    regresa el numero mayor, requiere inicializacion
    """
    if not lista:  #caso de lista vacia
        return mayor
    frente = lista.pop()
    if frente > mayor:
        mayor = frente #tambien se puede solucionar asi: linea actual: return mayor_rec(lista, frente) y en la linea de abajo: return mayor_rec(lista, mayor)
    return mayor_rec(lista, mayor)

def mayor(lista: list) -> int:
    """
    regresa el mayor de la lista
    lista: list
    returns: int
    """
    lista = lista[:]
    if not lista:
        return -1
    mayor = lista.pop()
    return mayor_rec(lista, mayor)

def mayor_rec2(lista):
    if not lista:
        return -1
    frente = lista.pop()
    if not lista: #la lista tenia un solo elemento
        return frente
    mayor_resto = mayor_rec2(lista)
    if frente > mayor_resto(lista):
        return frente
    else:
        return mayor_resto


if __name__ == '__main__':
    n = int(input())
    l = [input() for _ in range(n)]
    print(mayor(l))



    #casos base:
    #lista vacia
      #numero mayor (parametro)
    #casos recursivos:
      #cuando no esta vacia
      #comprar frente con mayor