cadena = input()
usuario = input()
segundo_split = cadena.split('$')

algoritmo = segundo_split[1]
salt = segundo_split[2]
password = segundo_split[3]

if usuario == 'algoritmo':
    print(algoritmo)
elif usuario == 'salt':
    print(salt)
elif usuario == 'password':
    print(password)
else:
    print('Opción no válida')