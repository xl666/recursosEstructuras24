a = []
b = []
N = int(input("Ingrese el número de elementos para la lista a: "))
M = int(input("Ingrese el número de elementos para la lista b: "))

# Llenar la lista 'a'
for i in range(N):
    elemento_a = int(input(f"Ingrese el elemento {i + 1} para la lista a: "))
    a.append(elemento_a)

# Llenar la lista 'b'
for i in range(M):
    elemento_b = int(input(f"Ingrese el elemento {i + 1} para la lista b: "))
    b.append(elemento_b)

print("Lista a:", a)
print("Lista b:", b)

# Mezclar las listas 'a' y 'b' en 's'
s = []

# Combinar los elementos de las listas 'a' y 'b' en 's' alternativamente
while a or b:
    if a:
        s.append(a.pop(0))
    if b:
        s.append(b.pop(0))

print("Lista combinada s:", s)
