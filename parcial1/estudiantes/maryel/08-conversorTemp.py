temperatura = float(input( "Ingrese la temperatura a convertir: "))
tipotemp  = input ("Es Fahrenheit (F) o Celcius (C):  ")

if tipotemp == 'F'or tipotemp == 'f':
    celsius = (temperatura -32)*5/9
    print("La temperatura en grados Celsius es: ",celsius)
elif tipotemp =='C' or tipotemp == 'c':
    fahrenheit = temperatura *1.8 + 32
    print("La temperatura en Fahrenheit es: ",fahrenheit)
else:
    print("Error, por favor ingrese una opción válida")

     
                   
