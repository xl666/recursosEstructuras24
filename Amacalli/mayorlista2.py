elementos = int(input())
def leer_lista(elementos):
    lista_resultado = []
    lista_resultado.append(int(input()))
    return lista_resultado
def mayor_lista(lista):
    if not lista:
        return None
    mayor = lista[0]
    for elemento in lista:
        if elemento > mayor:
            mayor = elemento
            return mayor