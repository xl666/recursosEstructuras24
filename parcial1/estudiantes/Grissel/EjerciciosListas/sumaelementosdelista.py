def crear_lista(n):
    lista = []
    for _ in range(n):
        numero = int(input())
        lista.append(numero)
    return lista

def suma_lista(lista):
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma

if __name__ == '__main__':
    n = int(input()) # elementos de la lista
    print(suma_lista(crear_lista(n)))