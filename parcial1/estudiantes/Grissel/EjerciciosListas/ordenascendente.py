def crear_lista(n):
    lista = []
    for _ in range(n):
        numero = int(input("Ingrese un número para la lista: "))
        lista.append(numero)
    return lista

def esta_ordenada_ascendente(lista):
    return lista == sorted(lista)

if __name__ == '__main__':
    n = int(input("Ingrese el número de elementos de la lista: ")) 
    lista = crear_lista(n)
    if esta_ordenada_ascendente(lista):
        print("La lista está ordenada de manera ascendente.")
    else:
        print("La lista no está ordenada de manera ascendente.")