import sys
import os

# Verificar si se proporcionó un argumento
if len(sys.argv) != 2:
    print("Uso: python programa.py <directorio>")
    sys.exit(1)

# Obtener el directorio proporcionado como argumento
C:\Users\LENOVO\OneDrive\Escritorio\estructura de datos = sys.argv[1]

# Verificar si la ruta es un directorio válido
if not os.path.isdir(C:\Users\LENOVO\OneDrive\Escritorio\estructura de datos):
    print("La ruta proporcionada no es un directorio válido.")
    sys.exit(1)

# Obtener la lista de archivos en el directorio
archivos = os.listdir(C:\Users\LENOVO\OneDrive\Escritorio\estructura de datos)

# Contar el número total de archivos
numero_archivos = len(archivos)

print("El número total de archivos en el directorio es:", numero_archivos)
