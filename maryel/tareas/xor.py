n1 = int(input())
n2 = int(input())

resultado = (bool(n1) and not bool(n2)) or (not bool(n1) and bool(n2))

print(resultado)
