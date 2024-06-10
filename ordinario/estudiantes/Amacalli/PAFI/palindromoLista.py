lista = [1, 2, 3, 2, 1]

lista2 = list(reversed(lista))

c = 0
for i in range(len(lista)):
    if lista[i] == lista2[i]:
        c += 1

if c == len(lista):
    print('La lista es palíndroma')
else:
    print('La lista no es palíndroma')

indIzq = 0
indDer = len(lista) - 1

while indIzq < indDer:
    if lista[indIzq] != lista[indDer]:
        print(False)
    indIzq += 1
    indDer -= 1
print(True)