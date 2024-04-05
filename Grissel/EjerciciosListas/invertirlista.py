def crear_lista():
    lista = []
    for _ in range(n):
        numero = int(input("Ingrese un número para la lista: "))
        lista.append(numero)
    return lista

def invertir_lista(lista):
    return lista[::-1]

if __name__ == '__main__':
    n = int(input("Ingrese el número de elementos de la lista: ")) 
    lista = crear_lista()
    print("La lista invertida es:", invertir_lista(lista))
