import sys
import os

if len(sys.argv) != 2:
    print('Debes pasar un parámetro')
    exit(1)

ruta = sys.argv[1]
if not os.path.isdir(ruta):
    print('Se esperaba un directorio')
    exit(1)

print('Número de archivos: ')
print(len(os.listdir(ruta)))
