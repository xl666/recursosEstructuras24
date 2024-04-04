N_int =int(input())
lista=[]

if N_int== 0:
    print("sin datos")
    exit

for i in range(N_int):
    lista.append(input())
for elemento in lista:
    print(elemento)