def fibonacci(n):
    if n <= 0:
        return "Ingrese un número entero positivo"

    a, b = 1, 1
    for _ in range(n - 2):
        a, b = b, a + b

    return b

n = int(input(""))
resultado = fibonacci(n)
print(resultado)
