def crear_lista(n):
    lista = []
    for _ in range(n):
        numero = int(input("Ingrese un número para la lista: "))
        lista.append(numero)
    return lista

def numero_medio(lista):
    lista_ordenada = sorted(lista)
    longitud = len(lista_ordenada)
    if longitud % 2 == 0:
        medio_1 = lista_ordenada[longitud // 2 - 1]
        medio_2 = lista_ordenada[longitud // 2]
        return (medio_1 + medio_2) / 2
    else:
        return lista_ordenada[longitud // 2]

if __name__ == '__main__':
    n = int(input("Ingrese el número de elementos de la lista: ")) 
    lista = crear_lista(n)
    print("El número medio en la lista es:", numero_medio(lista))
