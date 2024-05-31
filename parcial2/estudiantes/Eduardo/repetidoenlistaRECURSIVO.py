

def todos_repetidos_rec(lista, acumulador, resultado):  #version recursiva
    if not lista:
        return resultado
    frente = lista[0]
    resto = lista[1:]
    if frente in resto:
        resultado_parcial = True
    if frente in acumulador:
        resultado_parcial = True
        acumulador.append(frente)
    return todos_repetidos_rec(resto,acumulador,resultado_parcial and resultado)

def todos_repetidos(lista):
    if not lista:
        return False
    return todos_repetidos_rec(lista, [], True)

def todos_repetidos2(lista):
    if not lista:
        return False
    frente = lista[0]
    resto = lista[1:]
    if frente in lista:
        return True and todos_repetidos(resto)
    else:
        return False 

if __name__ == '__main__':
    n = int(input())
    lista = [input() for _ in range(n)]