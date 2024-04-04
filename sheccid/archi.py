import sys
import os

if len (sys.argv) !=2:
    print("Se espera un parametro")
    exit(1) #0=sin error 1=con error
try:
    ruta = str(sys.argv[1])
    if os.path.isdir(ruta):
        x=0
        for i in os.listdir(ruta):
            y=x
            x=x+1
        print(y)
except:
    print("Error, se esperaba una cadena")
    exit(1)
finally:
    print("Fin del programa")