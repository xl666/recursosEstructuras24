# - - - endswith
# - - - Verificar si una cadena termina con un sufijo específico
cadena = "Hola mundo"
if cadena.endswith("mundo"):
    print("La cadena termina con 'mundo'")
else:
    print("La cadena no termina con 'mundo'") # Salida: La cadena termina con 'mundo'
    
# - - - Filtrar una lista de nombres de archivos que terminan con una extensión específica
archivos = ["documento.txt", "imagen.jpg", "script.py", "datos.csv", "presentacion.pptx"]
archivos_txt = [archivo for archivo in archivos if archivo.endswith(".txt")]
print(archivos_txt)  # Salida: ['documento.txt']

# - - - Contar cuántas cadenas en una lista terminan con un sufijo específico
palabras = ["gato", "perro", "gallina", "caballo", "cabra"]
contador = sum(1 for palabra in palabras if palabra.endswith("o"))
print("Cantidad de palabras que terminan con 'o':", contador)  # Salida: 3