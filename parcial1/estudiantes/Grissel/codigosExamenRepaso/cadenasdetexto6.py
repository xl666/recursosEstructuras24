# - - - Eliminar espacios en blanco al principio y al final de una cadena.
cadena = "   Hola mundo   "
limpia = cadena.strip()
print(limpia)  # Imprime: "Hola mundo"

# - - - Eliminar caracteres específicos al principio y al final de una cadena.
cadena = "---Hola mundo---"
limpia = cadena.strip("-")
print(limpia)  # Imprime: "Hola mundo"

# - - - Eliminar solo los espacios en blanco al principio de una cadena.
cadena = "   Hola mundo   "
limpia = cadena.lstrip()
print(limpia)  # Imprime: "Hola mundo   "

# - - - Eliminar solo los espacios en blanco al final de una cadena.
cadena = "   Hola mundo   "
limpia = cadena.rstrip()
print(limpia)  # Imprime: "   Hola mundo"