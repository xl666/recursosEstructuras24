def crear_lista(n):
    lista = []
    for _ in range(n):
        numero = int(input("Ingrese un número para la lista: "))
        lista.append(numero)
    return lista

def agregar_al_principio(lista, valor):
    lista.insert(0, valor)
    return lista

if __name__ == '__main__':
    n = int(input("Ingrese el número de elementos de la lista: ")) 
    lista = crear_lista(n)
    valor = int(input("Ingrese el valor que desea agregar al principio de la lista: "))
    print("La lista con el valor agregado al principio es:", agregar_al_principio(lista, valor))
