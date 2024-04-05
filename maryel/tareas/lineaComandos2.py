import os

# Ingresa la ruta del directorio aquí
directorio = "C:\Users\LENOVO\OneDrive\Escritorio\estructura de datos"

# Verificar si la ruta es un directorio válido
if not os.path.isdir(directorio):
    print("La ruta proporcionada no es un directorio válido.")
else:
    # Obtener la lista de archivos en el directorio
    archivos = os.listdir(directorio)

    # Contar el número total de archivos
    numero_archivos = len(archivos)

    print("El número total de archivos en el directorio es:", numero_archivos)

