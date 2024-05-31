def xor(a, b):
    return (a or b) and not (a and b)

num1 = bool(int(input()))
num2 = bool(int(input()))

resultado=xor(num1, num2)
print(resultado)
