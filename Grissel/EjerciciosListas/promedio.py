def crear_lista(n):
    lista = []
    for _ in range(n):
        numero = int(input("Ingrese un número para la lista: "))
        lista.append(numero)
    return lista

def promedio_lista(lista):
    return sum(lista) / len(lista)

if __name__ == '__main__':
    n = int(input("Ingrese el número de elementos de la lista: ")) 
    lista = crear_lista(n)
    print("El promedio de los elementos de la lista es:", promedio_lista(lista))
