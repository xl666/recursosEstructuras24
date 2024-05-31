def crear_lista(n):
    lista = []
    for _ in range(n):
        numero = int(input("Ingrese un número para la lista: "))
        lista.append(numero)
    return lista

def eliminar_duplicados(lista):
    return list(set(lista)) # SET: colección desordenada y sin elementos duplicados

if __name__ == '__main__':
    n = int(input("Ingrese el número de elementos de la lista: ")) 
    lista = crear_lista(n)
    lista_sin_duplicados = eliminar_duplicados(lista)
    print("La lista sin elementos duplicados es:", lista_sin_duplicados)
