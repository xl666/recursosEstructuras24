n = int(input())
lista = []

if n == 0:
 print('no valido')
 exit

for _ in range(n):
 lista.append(int(input()))


maximo = lista[0]

for elemento in lista:
    if elemento > maximo:
        maximo = elemento

print(maximo)