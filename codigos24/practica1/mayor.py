
def leer_lista(elementos):
    lista_resultado = []
    for _ in range(elementos):
        lista_resultado.append(int(input()))
    return lista_resultado

def mayor_lista(lista):
    if not lista:  # si la lista está vacía 
        return None
    mayor = lista[0]
    for elemento in lista[1:]:
        if elemento > mayor:
            mayor = elemento
    return mayor

if __name__ == '__main__':    
    elementos = int(input())
    lista_numeros = leer_lista(elementos)
    print(mayor_lista(lista_numeros))
