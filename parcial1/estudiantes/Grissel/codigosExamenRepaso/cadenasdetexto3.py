# - - - Recorrido básico de la cadena e impresión de cada carácter en una línea separada.
cadena = "Python"
for caracter in cadena:
    print(caracter)

# - - - Recorrido inverso de la cadena e impresión de cada carácter en una línea separada.
cadena = "Hola mundo"
for i in range(len(cadena)-1, -1, -1):
    print(cadena[i])

# - - - Recorrido de la cadena con salto de dos caracteres e impresión de cada carácter en una línea separada.
cadena = "ABCDEFGHIJ"
for i in range(0, len(cadena), 2):
    print(cadena[i])     