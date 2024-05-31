def calcular_elemento_serie(n):
    if n <= 0:
        print("El valor de n debe ser un número entero positivo.")

    if n == 1 or n == 2:
        return 1

    a, b = 1, 1
    for _ in range(2, n):
        a, b = b, a + b

    return b

n = int(input())
resultado = calcular_elemento_serie(n)
print(resultado)
