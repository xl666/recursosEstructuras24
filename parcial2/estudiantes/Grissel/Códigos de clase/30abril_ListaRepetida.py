# casos base: 
# - lista vacía: False

def todos_repetidos_rec(lista, acumulador, resultado):
    if not lista:
        return resultado
    frente = lista[0]
    resto = lista[1:]
    resultado_parcial = False
    if frente in resto:
        resultado_parcial = True
    if frente in acumulador:
        resultado_parcial = True
        acumulador.append(frente)
    return todos_repetidos_rec(resto, acumulador, resultado_parcial and resultado)

if __name__ == '__main__':
    n = int(input())
    lista = [input() for _ in range(n)]
