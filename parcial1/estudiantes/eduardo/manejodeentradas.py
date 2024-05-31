n_elementos = int(input())
lista = []

if n_elementos == 0:
 print('sin datos')
 exit()

for _ in range(n_elementos):
 lista.append(input())

for elemento in lista:
 print(elemento)

