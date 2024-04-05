v = int(input())
n = int(input())

lista = [int(x) for x in input().split()]

nueva_lista = [num for num in lista if num != v]

print(nueva_lista)
