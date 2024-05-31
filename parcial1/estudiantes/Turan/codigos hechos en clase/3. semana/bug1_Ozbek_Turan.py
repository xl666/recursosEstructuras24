# La función recibe una lista de enteros
# Calcula la sumatoria, pero ignora el valor 1
# osea que no cuenta los 1
def contar_sin_unos(lista):
    total = len(lista)
    i = 0
    suma = 0
    
    while i < total:
        elemento = lista[i]
        if elemento==1: #ignorando el valor de 1 convertiendo en 0, creo que tambien podria hacer filtrando la lista dentro de otra.
            elemento=elemento-1
            #continue ------> esto hacia que el siglo regresara a principio , hay que quitarlo.
        suma += elemento
        i += 1
    return suma

# Pruebas (las que pasan dan True)
print(contar_sin_unos([2, 3, 4]) == 9) #True
print(contar_sin_unos([2, 3, 4, 1]) == 9) #True
print(contar_sin_unos([1, 1, 1, 1]) == 0) #True
    