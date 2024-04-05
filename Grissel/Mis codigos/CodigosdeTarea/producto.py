def producto_lista(lista):
    producto = 1
    for numero in lista:
        producto *= numero
    return producto

n = int(input()) #Ingresar cuantos elementos quiero de mi lista
numeros = []
for _ in range(n):
    numero = int(input())
    numeros.append(numero)

resultado = producto_lista(numeros)

print(resultado)

