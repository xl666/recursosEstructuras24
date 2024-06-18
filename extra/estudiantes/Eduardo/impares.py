def suma_impares(n):
    if n < 0:
        return 0
    elif n % 2 == 1:
        return n + suma_impares(n - 2)
    else:
        return suma_impares(n - 1)

n = int(input())
print(suma_impares(n))
