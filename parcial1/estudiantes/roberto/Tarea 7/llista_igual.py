N = int(input())
M = int(input())
valores1 = [int(input()) for _ in range(N)]
valores2 = [int(input()) for _ in range(M)]

numero_comunes = []

for numero in valores1:
    if numero in valores2 and numero not in numero_comunes:
        numero_comunes.append(numero)
l2 = sorted(numero_comunes)

print(l2)