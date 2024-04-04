N_elementos = int(input())
lista = []

if N_elementos == 0:
    print("sin datos")
else:
    for _ in range(N_elementos):
        lista.append(input())

    for elemento in lista:
        print(elemento)
