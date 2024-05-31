def factorial(numero):
    if numero == 0:
        return 1
    return numero * factorial(numero - 1)

print(factorial(3))