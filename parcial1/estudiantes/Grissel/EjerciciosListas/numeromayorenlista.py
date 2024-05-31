# - - - Encontrar el número más grande en lista
def crear_lista(n):
    lista = []
    for _ in range(n):
        numero = int(input("Ingrese un número para la lista: "))
        lista.append(numero)
    return lista

def maximo_lista(lista):
    return max(lista)

if __name__ == '__main__':
    n = int(input("Ingrese el número de elementos de la lista: ")) 
    lista = crear_lista(n)
    print("El número más grande en la lista es:", maximo_lista(lista))
