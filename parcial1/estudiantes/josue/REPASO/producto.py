n = int(input())
lista = []
resultado = 1

for _ in range(n):
    lista.append(int(input()))

for num in lista:
    resultado *= num


print(resultado)