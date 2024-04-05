elementos = int(input())
maximo = 0

if elementos == 0:
    print("Error")
else:
    for _ in range(elementos):
        elemento = int(input())
        if elemento > maximo:
            maximo = elemento

    print(maximo)
