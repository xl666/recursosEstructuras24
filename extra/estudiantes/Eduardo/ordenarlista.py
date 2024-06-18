listaordenada=[]
nlista1=int(input())
nlista2=int(input())

for i in range(nlista1):
    listaordenada.append(int(input()))

for _ in range(nlista2):
    listaordenada.append(int(input()))

for i in range(len(listaordenada)):
    for j in range(0, len(listaordenada) - i - 1):
        if listaordenada[j] > listaordenada[j + 1]:
            listaordenada[j], listaordenada[j + 1] = listaordenada[j + 1], listaordenada[j]

print(listaordenada)
