n1 = int(input())
n2 = int(input())

lista1 = []
lista2 = []
intercalado = []

for i in range(n1):
    lista1.append(int(input()))

for _ in range(n2):
    lista2.append(int(input()))

x = 0
while x < n1 or x < n2:
    if x < n1:
        intercalado.append(lista1[x])
    if x < n2:
        intercalado.append(lista2[x])
    x += 1

print(intercalado)