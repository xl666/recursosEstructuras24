import sys
import os

if len(sys.argv) != 2:
    print("Error. Se esperaba un parámetro")
    exit(1)

try:
    ruta = str(sys.argv[1])
    if os.path.isdir(ruta):
        print(len(os.listdir(ruta)))
    else:
        print('No es una ruta')
except:
    print("Error. Se esperaba que ingresaras una cadena")
    exit(1)
finally:
    print("Fin del programa")