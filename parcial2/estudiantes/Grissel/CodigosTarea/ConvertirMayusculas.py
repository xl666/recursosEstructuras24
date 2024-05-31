import sys
import os

def convertir_a_mayusculas(archivo_entrada: str, archivo_salida: str):
    """
    Convertir texto minusculas a texto en mayúsculas y guardar en otro archivo.

    archivo_entrada: str
    archivo_salida: str
    """
    with open(archivo_entrada, 'r') as minuscula:
        contenido = minuscula.read()
    nuevo = contenido.upper()
    with open(archivo_salida, 'w') as mayuscula:
        mayuscula.write(nuevo)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Se esperaba tu archivo y tu archivo_convertir')
        exit(1)
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]

    if not os.path.isfile(archivo_entrada):
        print('El archivo debe existir')
        exit(1)

    convertir_a_mayusculas(archivo_entrada, archivo_salida)
    print(f"Contenido convertido a mayúsculas y guardado en {archivo_salida}")

