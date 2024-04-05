texto = "hola Mundo"
print(texto.upper())  # Imprime HOLAS MUNDO en mayusculas
print(texto.lower())  # Imprime holas mundo en minusculas
# Capitaliza la primera letra y deja las demas minusculas
print(texto.capitalize())
print(texto.title())  # Capitaliza todas las palabras del texto
print(texto.strip())  # Elimina  los espacios al inicio y final de una cadena
print(texto.strip().capitalize())  # Combinación de strip() y capitalize()
print(texto.lstrip())  # Elimina los espacios de la izquierda de la cadena
print(texto.rstrip())  # Elimina los espacios de la derecha de la cadena
# Devuelve la posicion donde se encuentra el dato buscado
print(texto.find("do"))
# Cambia la palabra Mundo por Tierra
nuevotexto = texto.replace("Mundo", "Tierra")
print(texto, nuevotexto)  # Imprime Hola Mundo y Hola Tierra
# Verifica si existe la palabra Mundo en el Texto Devuelve True o False
print("Mundo" in texto)
print("Mundo" not in texto)  # Lo contrario al de arriba, lo esta negando
print(len(texto))  # Devuelve la longitud del texto
print(texto[3])  # Devuelve el caracter de la posicion 4 del texto Imprime a
print(texto[0:4])  # Devuelve los primeros 4 caracteres Del Texto Imprime Hola
# Devuelve Todos Los Caracteres Desde La Posicion 4 hasta El Final Del Texto
print(texto[4:])
print(texto[:4])  # Devuelve Todos Los Caracteres Hasta La Posicion 4 Del Texto
print(texto[:])  # Devuelve Todos Los Caracteres Del Texto
