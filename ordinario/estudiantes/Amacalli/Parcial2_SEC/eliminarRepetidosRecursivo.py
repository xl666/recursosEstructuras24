
def eliminar_repetidos2(lista:list) -> list:
    #Hecho por el maestro
    if not lista:
        return []
    frente = lista[0]
    resto = lista[1:]
    demas = eliminar_repetidos2(resto)
    if frente in demas:
        return demas
    else:
        return [frente] + demas

def eliminar_recursivo(lista: list, res:list) -> list:
    if not lista:
        return res
    frente = lista[0]
    resto = lista[1:]
    
    if not frente in res:
        res.append(frente)
    return eliminar_recursivo(resto, res)
    
def eliminar(lista:list) -> list:
    return eliminar_recursivo(lista, [])

if __name__ == '__main__':
    n = int(input())
    lista = [int(input()) for _ in range(n)]
    lista1 = lista.copy()
    print(eliminar(lista1))