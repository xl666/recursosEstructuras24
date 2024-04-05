import sys

if len(sys.argv) < 3: # hay que contar posición 0
    print('Error: se esperaban dos parámetros')
    exit(1) # terminación con error

try: # la conversión puede fallar
    numero1 = int(sys.argv[1])
    numero2 = int(sys.argv[2])
    print(numero1 + numero2)
except:
    print('Error: se esperaba que pasaras números')
    exit(1)
finally:
    print('Fin del programa')

    


  