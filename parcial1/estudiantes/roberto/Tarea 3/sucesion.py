n=int(input())

def fibo(n):
    if n==1 or n==2:
        return 1
    anterior= 1
    actual = 1
    for _ in range(n-2):
        siguiente= anterior + actual
        anterior = actual
        actual= siguiente
    return actual
print(fibo(n))

