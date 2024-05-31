num_elim = int(input())
N = int(input())
valores1 = [int(input()) for _ in range(N)]


for numero in valores1[:]:
    if numero == num_elim:
        del valores1[valores1.index(numero)]

print(valores1)