pos = int(input()) #pos=posicion

def calcular_fibonacci(pos):
    if pos == 1 or pos == 2:
        return 1
    anterior = 1
    actual = 1
    for _ in range(pos - 2):
        siguiente = anterior + actual
        anterior = actual
        actual = siguiente
    return actual

print(calcular_fibonacci(pos))