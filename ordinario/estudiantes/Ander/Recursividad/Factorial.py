# Escribir una función recursiva para calcular el factorial de un número.

def factorial(n: int) -> int:
    if not n:
        return 1
    return n * factorial(n - 1)

if __name__=='__main__':
    n = int(input())
    print(factorial(n))