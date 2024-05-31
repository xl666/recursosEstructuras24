def productototal(lista):
    producto = 1
    for numero in lista:
        producto *= numero
    return producto

n = int(input())
numeros = []
for i in range(n):
    numero = int(input())
    numeros.append(numero)

resultado = productototal(numeros)
print(resultado)
