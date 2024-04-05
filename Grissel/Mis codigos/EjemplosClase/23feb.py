#BUG1
def contar_sin_unos(lista):
    total = len(lista)
    i = 0
    suma = 0
    while i < total:
        elemento = lista[i]
        if elemento != 1:
            suma += elemento
        i += 1
    return suma

# Pruebas (las que pasan dan True)
print(contar_sin_unos([2, 3, 4]) == 9)
print(contar_sin_unos([2, 3, 4, 1]) == 9)
print(contar_sin_unos([1, 1, 1, 1]) == 0)
