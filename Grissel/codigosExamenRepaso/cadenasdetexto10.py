# - - - Unir una lista de cadenas en una sola cadena usando un separador
lista = ["Hola", "mundo", "Python"]
cadena = " - ".join(lista)
print(cadena)  # Output: Hola - mundo - Python

# - - - Convertir una lista de números en una cadena de texto separada por comas
numeros = [1, 2, 3, 4, 5]
cadena_numeros = ", ".join(str(num) for num in numeros)
print(cadena_numeros)  # Salida: 1, 2, 3, 4, 5

# - - - Unir las claves y valores de dos listas en una cadena de texto formateada
claves = ["nombre", "edad", "ciudad"]
valores = ["Juan", 30, "Madrid"]
cadena_lista = ", ".join(f"{claves[i]}: {valores[i]}" for i in range(len(claves)))
print(cadena_lista)  # Output: nombre: Juan, edad: 30, ciudad: Madrid