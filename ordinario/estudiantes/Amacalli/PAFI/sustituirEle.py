lista = []

print('Ingresa los elementos de la lista: ')
for _ in range(5):
    lista.append(int(input()))

print('Ingresa el valor que quieres sustituir: ')
x = int(input())

print('Ingresa el valor por el cual lo quieres sustituir: ')
y = int(input())

def sustituir(lista, x, y):
    for i in range(len(lista)):
        if lista[i] == x:
            lista[i] = y
    return lista


print(sustituir(lista, x, y))
