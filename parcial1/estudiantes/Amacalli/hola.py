def hola():
	name = input('Ingrese su nombre: ')
	age =  input ('Ingrese tu edad: ')
	print('Hola ', name, ', tienes ', age)
	#comentario

hola()

if 3 < 2 or True:
    print('entra a if')
elif 6 == 6.0:
        print('entra al primer elif')
elif 5 > 3:
    print('entra al segundo elif')
else:
    print('entra al else')

l = [1, 2, 3, 5, 10]
if 5 in l:
	print('está el 5')
else:
		print('no esta el elemento')
	
x = 0
while True: # ciclo infinito
    print(x)
    if x > 2:
        break
    x += 1

for palabra in ['hola', 'mundo', 'mundial']:
    print(palabra)

for caracter in 'hola':
 	print(caracter)