import sys
import os

def contar_archivos_en_directorio(ruta_directorio):
    if not os.path.isdir(ruta_directorio):
        print("Error: La ruta proporcionada no es un directorio válido.")
        return
    
    lista_archivos = os.listdir(ruta_directorio)
    cantidad_archivos = len(lista_archivos)
    print(f"Número total de archivos en el directorio {ruta_directorio}: {cantidad_archivos}")

if __name__ == "__main__":
    # Verificar que se proporcionó un argumento (ruta del directorio)
    if len(sys.argv) != 2:
        print("Uso: python programa.py <ruta_directorio>")
    else:
        ruta_directorio = sys.argv[1]
        contar_archivos_en_directorio(ruta_directorio)