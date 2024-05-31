# La función recibe una lista de enteros
# Calcula la sumatoria, pero ignora el valor 1
# osea que no cuenta los 1
def contar_sin_unos(lista):
    suma = 0
    for elemento in lista:
        if elemento == 1:
            continue
        suma = suma + elemento
    return suma

# Pruebas (las que pasan dan True)
print(contar_sin_unos([2, 3, 4]) == 9)
print(contar_sin_unos([2, 3, 4, 1]) == 9)
print(contar_sin_unos([1, 1, 1, 1]) == 0)
    
