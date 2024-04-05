# Entrada de datos
n = int(input())
elementos = list(map(int, input().split( )))

# Encontrar el valor mayor
if elementos:
    mayor = elementos[0]
    for elemento in elementos:
        if elemento > mayor:
            mayor = elemento
    print(mayor)
else:
    print("Error: lista vacía")