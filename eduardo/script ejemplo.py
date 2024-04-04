import sys
import os

if len(sys.argv) != 2:
    print ('debes pasar un parametro')
    exit(1)

ruta = sys.argv[1]
if not os.path.isdir(ruta):
    print('se esperaba un directorio')
    exit(1)

print('numero de archivos: ')
print(len(os.listdir(ruta)))