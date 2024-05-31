numElementos = int(input())

maximo = None
if numElementos > 0:
    maximo = int(input())

    for i in range(numElementos - 1):
        numero = int(input())
        if numero > maximo:
            maximo = numero

else:
    print("Error")

if maximo is not None:
    print(maximo)

