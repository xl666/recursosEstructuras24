import sys
import os

if len(sys.argv) !=2: #Checamos la longitud de esto, y pongo 2 por el parametro 0
    print("Debes pasar un párametro")
    exit(1)

ruta = sys.argv[1] #Se que la ruta está en el parametro 1
if not os.path.isdir(ruta):
    print("Se esperaba un directorio") 

print ("Numero de archivos: ")
print(len(os.listdir(ruta)))

