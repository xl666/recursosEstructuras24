def xor(a, b):
    return (a or b) and not (a and b)
valor1 = bool(int(input()))  
valor2 = bool(int(input()))  
resultado = xor(valor1, valor2)
print(resultado)

