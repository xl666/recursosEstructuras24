ejemplos1 = '   Hola mundo   '
print(ejemplos1.strip())

ejemplos2 = 'hola mundo'
print(ejemplos2.upper())

ejemplos3 = 'Hola mundo Hola tierra'
print(ejemplos3.split())

ejemplos4 = 'Hola mundo'
print(ejemplos4.startswith('Hola'))

ejemplos5 = 'Hola mundo'
print(ejemplos5.endswith('mundo'))

ejemplos6 = '12E45'
print(ejemplos6.isnumeric())

nombre = 'Yahir'
edad = 20
ejemplos7 = 'Hola me llamo {} y tengo {} años'.format(nombre, edad)
print(ejemplos7)
