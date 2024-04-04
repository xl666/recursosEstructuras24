n = int(input())
lista = []
for i in range(n):
    lista.append(int(input()))
def maximo():
    valormax = lista[0]  
    for i in range(1, n):
        if lista[i] > valormax:
            valormax = lista[i]
    return valormax
print(maximo())