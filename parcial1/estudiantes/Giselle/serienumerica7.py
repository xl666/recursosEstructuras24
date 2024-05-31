def calcularE(n):
    if n <= 0:
        return "El número debe ser mayor que 0"
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b


n = int(input())
resul = calcularE(n)
print(resul)
