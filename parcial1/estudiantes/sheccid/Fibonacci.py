def fibonacci(n):
    if n <= 0:
        return "Error"
    elif n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

n = int(input())
resultado = fibonacci(n)
print(resultado)