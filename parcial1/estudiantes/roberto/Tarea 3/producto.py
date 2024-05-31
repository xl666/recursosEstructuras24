N_int =int(input())
lista=[]
for i in range(N_int):
    lista.append(int(input()))
producto = 1
for elemento in lista:
    producto *= elemento
print(producto)