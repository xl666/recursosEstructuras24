def producto_lista(numeros):

    producto = 1

    for num in numeros:
        producto = producto * num

    return producto

n = int(input())

numeros = []

if n < 1:
    print('error')
    exit()
    
for i in range(n):
    numeros.append(int(input()))

resultado = producto_lista(numeros)

print(resultado)
