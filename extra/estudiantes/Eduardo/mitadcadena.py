cadena = input()
longitud = len(cadena)

if longitud % 2 != 0:
    mitad1impar = longitud//2
    print(cadena[mitad1impar])
else:
    mitad1par = longitud//2
    mitadpar = mitad1par-1
    print(cadena[mitadpar]+cadena[mitad1par])