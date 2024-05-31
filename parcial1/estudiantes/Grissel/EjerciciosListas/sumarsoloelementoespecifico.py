def crear_lista(n):
    lista = []
    for _ in range(n):
        numero = int(input())
        lista.append(numero)
    return lista

def suma_lista(lista, num_a_sumar):
    suma = 0
    for elemento in lista:
        if elemento == num_a_sumar:
            suma += elemento
    return suma

if __name__ == '__main__':
    n = int(input()) # elementos de la lista
    lista = crear_lista(n)
    num_a_sumar = int(input()) # el numero que se desea sumar (en especifico)
    print(suma_lista(lista, num_a_sumar))
    