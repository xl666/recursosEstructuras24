elementos = int(input())
maximo = 0
for elemento in range(elementos):
    elemento = int(input())
    if elemento > maximo:
        maximo = elemento

print(maximo)