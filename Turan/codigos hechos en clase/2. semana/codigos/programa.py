import os
import sys

def contar_archivos_en_directorio(ruta):
    # Verificar si la ruta es un directorio válido
    if not os.path.isdir(ruta):
        print("La ruta proporcionada no es un directorio válido.")
        return

    # Obtener la lista de archivos en el directorio
    archivos = os.listdir(ruta)

    # Contar el número de archivos
    num_archivos = len(archivos)

    # Mostrar el resultado
    print(f"El número total de archivos en el directorio {ruta} es: {num_archivos}")

if __name__ == "__main__":
    # Verificar si se proporciona un argumento de línea de comandos
    if len(sys.argv) != 2:
        print("Por favor, proporcione una ruta de directorio como argumento.")
    else:
        # Obtener la ruta del directorio del argumento de línea de comandos
        directorio = sys.argv[1]
        # Contar archivos en el directorio
        contar_archivos_en_directorio(directorio)
