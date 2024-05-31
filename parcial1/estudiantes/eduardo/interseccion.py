def comunes(lista1, lista2):
    listasinrepetidos1 = set(map(int, lista1))
    listasinrepetidos2 = set(map(int, lista2))
    inter = sorted(listasinrepetidos1.intersection(listasinrepetidos2))
    return inter

lista1 = []
lista2 = []

numelementos1 = int(input())
numelementos2 = int(input())

for _ in range(numelementos1):
    lista1.append(input())

for _ in range(numelementos2):
    lista2.append(input())

resultado = comunes(lista1, lista2)
resultado_ordenado = sorted(resultado)
print(resultado_ordenado)