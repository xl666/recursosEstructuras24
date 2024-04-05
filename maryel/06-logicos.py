edad = 20
print(edad >= 18 and edad < 30)
print(edad >= 18 or edad < 30)
print(not True)
print(not False)
print(not (edad > 18))

gas = False
encendido = True
edad = 18
if not gas and (encendido or edad > 17):
    print('puedes avanzar')

edad2 = 16
if 15 <= edad <= 65:
    print('puedes ingresar')
