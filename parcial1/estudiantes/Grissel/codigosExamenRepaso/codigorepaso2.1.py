# - - - Calificación de estudiantes
calificacion = float(input())
if calificacion >= 6:
    print('Aprobaste')
else:
    print('Reprobaste')

# - - - Numero par o impar
numero = int(input())
if numero % 2 == 0:
    print('Es numero par')
else:
    print('Es un numero impar')

# - - - Calculo descuento
precio = float(input())
categoria = input()
a = 0.10
b = 0.20
c = 0.30
if categoria == 'a':
    resultado = precio - (precio * a)
elif categoria == 'b':
    resultado = precio - (precio * b)
elif categoria == 'c':
    resultado = precio - (precio * c)
print(resultado)

# - - - Triangulo según sus lados
lado1 = float(input())
lado2 = float(input())
lado3 = float(input())
if lado1 == lado2 and lado2 == lado3:
    print('Es triangulo equilatero')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('El triangulo es isóceles')
else:
    print('El triangulo es escaleno')