def contar_sin_unos(lista):
    total = len(lista)
    i = 0
    suma = 0
    while i < total:
        elemento = lista[i]
        if elemento != 1:
            # print("ignorar 1")
            suma += elemento
            # print(f"suma actual {suma}")
        i += 1
        # print(f"indice {i}")
    return suma


# Pruebas
print(contar_sin_unos([2, 3, 4]) == 9)
print(contar_sin_unos([2, 3, 4, 1]) == 9)
print(contar_sin_unos([1, 1, 1, 1]) == 0)
