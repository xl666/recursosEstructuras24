import sys
import os

directorio = sys.argv[1]

if not os.path.isdir(directorio):
    sys.exit(1)

contenido = os.listdir(directorio)

num_archivos = len(contenido)

print(num_archivos)