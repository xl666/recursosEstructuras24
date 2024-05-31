import sys
import os

if len(sys.argv) != 2:
    print('Debes pasar un parametro')
    exit(1) #exit(1)=error , exit()/exit(0)= sin error

ruta = sys.argv[1]
if not os.path.isdir(ruta):
    print('Se esperaba un directorio')
    exit(1)

print('Numero de archivos: ')
print(len(os.listdir(ruta)))

    