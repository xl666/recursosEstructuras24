# rsplit - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
cadena = input("Ingresa una cadena: ")
separador = input("Ingresa el separador: ")
partes = cadena.rsplit(separador, 1)
print(partes)  # Salida: Lista de subcadenas divididas desde la derecha

# strip - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
cadena = input("Ingresa una cadena: ")
limpia = cadena.rstrip()
print(limpia)  # Salida: Cadena sin espacios a la derecha

# startswith - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
cadena = input("Ingresa una cadena: ")
prefijo = input("Ingresa el prefijo a verificar: ")
empieza_con_prefijo = cadena.startswith(prefijo)
print(empieza_con_prefijo)  # Salida: True o False si la cadena empieza con el prefijo

#swapcase 
cadena = input("Ingresa una cadena: ")
intercambiada = cadena.swapcase()
print(intercambiada)  # Salida: Cadena con mayúsculas y minúsculas intercambiadas
