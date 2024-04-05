
#elementos = int(input())

def leer_lista(elementos):
    lista_resultado = []
    lista_resultado.append(int(input()))
    return lista_resultado

def mayor_lista(lista):
    if not lista: #la lista está vacia
        return None
    mayor = lista[0]
    for elemento in lista:
        if elemento > mayor:
            mayor = elemento
    return mayor 

#lista_numeros = leer_lista(elementos)
#print(mayor_lista(lista_numeros))