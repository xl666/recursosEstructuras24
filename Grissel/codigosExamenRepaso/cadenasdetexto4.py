# Ejemplo 1: Copia completa de la cadena 'buenos dias'
s = 'buenos dias'
print(s[0:11]) 

# Ejemplo 2: Mismo resultado que el anterior usando el tamaño de la cadena
print(s[:len(s)])

# Ejemplo 3: Otra forma de obtener la cadena completa
print(s[:]) 

# Ejemplo 4: Todos los caracteres excepto el primero ('uenos dias')
print(s[1:])  

# Ejemplo 5: Todos los caracteres excepto el último ('buenos dia')
print(s[:-1])  # Imprime 'buenos dia'

# Ejemplo 6: Las dos letras entre el espacio ('os di')
print(s[4:9])  # Imprime ''

# Ejemplo 1: Obtener una subcadena invertida
cadena = "Python"
print(cadena[::-1])  # Cadena invertida: "nohtyP"

# Ejemplo 2: Obtener una subcadena con inicio y fin específicos
cadena = "Mi nombre es Grissel"
print(cadena[3:12])  #Desde el índice 3 hasta el 12: "nombre es"
