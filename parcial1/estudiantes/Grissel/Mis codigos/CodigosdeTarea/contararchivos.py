import sys
import os

def contar_archivos(directorio):
    if not os.path.isdir(directorio):
        print("No se encontró el directorio")
        exit()
    return len(os.listdir(directorio))  

if len(sys.argv) != 2:
    exit(1)

directorio = sys.argv[1]
numero_archivos = contar_archivos(directorio)
if numero_archivos is not None:
    print(f"Número de archivos: {numero_archivos}")
    




