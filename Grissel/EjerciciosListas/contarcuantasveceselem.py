# - - - Contar cuántas veces aparece un elemento en la lista
def crear_lista(n):
    lista = []
    for _ in range(n):
        numero = int(input("Ingrese un número para la lista: "))
        lista.append(numero)
    return lista

def contar_elemento(lista, elemento):
    return lista.count(elemento)

if __name__ == '__main__':
    n = int(input("Ingrese el número de elementos de la lista: ")) 
    lista = crear_lista(n)
    elemento = int(input("Ingrese el elemento que desea contar: "))
    print("El elemento", elemento, "aparece", contar_elemento(lista, elemento), "veces en la lista.")
