# - - - startswith
# - - - Verificar si una cadena comienza con un prefijo específico
cadena = "Hola mundo"
if cadena.startswith("Hola"):
    print (True)
else:
    print(False) # salida: True
    
# - - - Filtrar una lista de cadenas que comienzan con un prefijo específico:
lista = ["manzana", "banana", "pera", "malón", "naranja"]
resultado = [fruta for fruta in lista if fruta.startswith("ma")]
print(resultado)  # Output: ['manzana', 'malón']

# - - - Contar cuántas cadenas en una lista comienzan con un prefijo específico
lista = ["gato", "perro", "gallina", "caballo", "cabra"]
contador = sum(1 for palabra in lista if palabra.startswith("g"))
print("Cantidad de palabras que comienzan con 'g':", contador)  # Output: 2