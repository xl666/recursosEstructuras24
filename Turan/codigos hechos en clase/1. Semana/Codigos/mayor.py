def n_mayor(lista):
    mayor = lista[0]
    for i in lista:
        if mayor < i:
            mayor = i
    return mayor

n_elementos = int(input())

if n_elementos > 0:
    for _ in range(n_elementos):
        lista.append(int(input()))

numero_mayor = n_mayor(nums)
print(numero_mayor)

