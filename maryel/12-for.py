Paises = ["Mexico",  "Estados Unidos", "Canada", "Chile"]

for Pais in Paises:
    print(Pais)

buscar = 3
for numero in range(5):
    print(numero)
    if numero == buscar:
        print('encontrado')
        break


buscar2 = 10
for numero in range(5):
    print(numero)
    if numero == buscar2:
        print('encontrado')
        break
else:
    print('no encontrado')
