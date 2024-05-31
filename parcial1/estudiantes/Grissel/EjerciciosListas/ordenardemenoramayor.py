def crear_lista(n):
    lista = []
    for _ in range(n):
        numero = int(input("Ingrese un número para la lista: "))
        lista.append(numero)
    return lista
 
def ordenar_lista(lista):
    return sorted(lista)

if __name__ == '__main__':
    n = int(input("Ingrese el número de elementos de la lista: ")) 
    lista = crear_lista(n)
    print("La lista ordenada de menor a mayor es:", ordenar_lista(lista))