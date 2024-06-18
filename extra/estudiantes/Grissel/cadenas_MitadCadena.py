# Mitad cadena - - - - - - - - - - - - - -
cadena = input()

longitud = len(cadena)
mitad = longitud // 2
mitad2 = mitad -1

if longitud % 2 == 0: # corrección de cambiar mitad por longitud
    impar = cadena[mitad2] + cadena[mitad]
    print(impar)
else:
    print(cadena[mitad])