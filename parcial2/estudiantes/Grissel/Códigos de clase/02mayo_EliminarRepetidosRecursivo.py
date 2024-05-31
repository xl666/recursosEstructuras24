# casos base: 
#   1. lista vacía --> regresar acumulador
#   2. l

# casos recursivos
#   1. lista no está vacía
#       Revisar si en el frente está en el acumulador
#           si: ignorar (no agreguamos al acumulador)
#           No: lo agregamos al acumulador 

def eliminar_repetidos2(lista: list) -> list:
    """
    Elimina elementos repetidos
    """
    if not lista:
        return []
    frente = lista[0]
    resto = lista[1:]
    demas = eliminar_repetidos2(resto)
    if frente in demas:
        return demas
    else:
        return [frente] + demas


def eliminar_repetidos_rec(lista: list, acumulador: list) -> list:
    """

    Elimina los elementos de forma recursiva
    lista: list
    acumulador: list, se debe inicializar como []
    returns: list

    """
    frente = lista[0]
    resto = lista[1:]
    if frente in lista:
        return eliminar_repetidos_rec(resto, acumulador)
    else:
        acumulador.append(frente)
        return eliminar_repetidos_rec(resto, acumulador)
    
def eliminar_repetidos(lista: list) -> list:
    """
    Regresa una lista
    lista: list
    return: list
    """
    return eliminar_repetidos_rec(lista,[])


if __name__ == '__main__':
    n = int(input())
    lista = [input() for _ in range(n)]
    print(eliminar_repetidos(lista))
