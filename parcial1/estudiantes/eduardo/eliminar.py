
filtro = int(input())

numdeelementos = int(input())

lista = [int(input()) for _ in range(numdeelementos)]

lista = [x for x in lista if x != filtro]

print(lista)