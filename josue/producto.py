# Entrada de datos
n = int(input(""))
lista = []
for i in range(n):
    lista.append(int(input()))

producto = 1

for num in lista:
    producto *= num
    print(num)
    print(producto)

#print(producto)
