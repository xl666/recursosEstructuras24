import sys

def sacar_imagen(ruta_pdf, ruta_salida):
    """
    Recupera la imagen incrustada en ruta_pdf y 
    la guarda en ruta_salida
    """
    with open(ruta_salida, 'wb') as salida:
        with open(ruta_pdf, 'rb') as entrada:
            contenido = entrada.read()
            paddding = b'0' * 100
            partes = contenido.split(paddding)
            salida.write(partes[1])

if __name__ == '__main__':
    ruta_pdf = sys.argv[1]
    ruta_salida = sys.argv[2]
    sacar_imagen(ruta_pdf, ruta_salida)
    