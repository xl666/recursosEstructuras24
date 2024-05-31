def fibonacci(numero):
    
    if numero == 1 or numero == 2:
        return 1
    else:
        x, y = 1, 1
        for _ in range(numero - 2):
            x, y = y, x + y
        return y

numero = int(input())
print(fibonacci(numero))
