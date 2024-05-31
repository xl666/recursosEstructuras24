def elementoserie(n):
    a = 1
    b = 1
    
    for _ in range(2, n):
        a, b = b, a + b
    return b

n = int(input())
resultado = elementoserie(n)
print(resultado)