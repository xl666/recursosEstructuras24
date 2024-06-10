# Implementar una función recursiva para calcular la serie de Fibonacci.

def fib(n: int) -> int:
    if not n:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

if __name__=='__main__':
    n = int(input())
    print(fib(n))