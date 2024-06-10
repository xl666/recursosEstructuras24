num = int(input('Ingresa un numero: '))
inicio = int(input('Ingresa el inicio del rango: '))
fin = int(input('Ingresa el fin del rango: '))

c = 0

while inicio <= fin:
    if inicio % num == 0:
        c += 1
    inicio += 1

print('Hay ', c, ' en el rango de ', inicio, ' a ', fin)
