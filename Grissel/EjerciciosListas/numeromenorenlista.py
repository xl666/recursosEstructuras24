# - - - Encontrar el número más pequeño en la lista
def crear_lista(n):
    lista = []
    for _ in range(n):
        numero = int(input("Ingrese un número para la lista: "))
        lista.append(numero)
    return lista

def minimo_lista(lista):
    return min(lista)

if __name__ == '__main__':
    n = int(input("Ingrese el número de elementos de la lista: ")) 
    lista = crear_lista(n)
    print("El número más pequeño en la lista es:", minimo_lista(lista))
