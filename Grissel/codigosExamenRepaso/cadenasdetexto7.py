# - - - Dividir una cadena en palabras usando espacios como delimitador.
cadena = "Hola mundo feliz"
palabras = cadena.split()
print(palabras)  # Imprime: ['Hola', 'mundo', 'feliz']

# - - - Dividir una cadena en palabras usando una coma como delimitador.
cadena = "manzana,naranja,plátano"
frutas = cadena.split(",")
print(frutas)  # Imprime: ['manzana', 'naranja', 'plátano']

# - - - Dividir una cadena en caracteres individuales.
cadena = "Python"
caracteres = list(cadena)
print(caracteres)  # Imprime: ['P', 'y', 't', 'h', 'o', 'n']

# - - - Dividir una cadena en líneas utilizando el carácter de nueva línea como delimitador.
cadena = "Primera línea\nSegunda línea\nTercera línea"
lineas = cadena.split("\n")
print(lineas)  
# Imprime: ['Primera línea', 'Segunda línea', 'Tercera línea']