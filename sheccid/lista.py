def multi(n, lista):
    producto = 1
    for num in lista:
        producto *= num
    return producto

n = int(input())
lista = []
for i in range(n):
    lista.append(int(input()))

resultado = multi(n, lista)
print(resultado)
