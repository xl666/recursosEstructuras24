
def contar_sin_unos(lista):
    total = len(lista)
    i = 0
    suma = 0
    while i < total: 
        elemento = lista[i]
        i += 1 #se pasa arriba del if
        if elemento == 1:
            continue
        suma += elemento   
    return suma

numeros = int(input('escribe cuantos numeros quieres ingresar'))
indexnumeros = []

if numeros == 0:
    print('no valido')
    exit()

for _ in range(numeros):
 indexnumeros.append(int(input()))

resultado = contar_sin_unos(indexnumeros) 
print(resultado)                                 

print(contar_sin_unos([2, 3, 4]) == 9)
print(contar_sin_unos([2, 3, 4, 1]) == 9)
print(contar_sin_unos([1, 1, 1, 1]) == 0)