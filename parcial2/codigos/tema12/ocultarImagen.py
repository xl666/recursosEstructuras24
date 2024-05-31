import sys

def ocultar_imagen(ruta_pdf, ruta_jpg, ruta_salida) -> None:
    """
    Oculta el archivo jpg en el de pdf
    utiliza un padding de 100 bytes para
    separar ambos archivos.

    ruta_pdf, ruta_jpg, ruta_salida
    returns: None 
    """
    padding = b'0' * 100
    with open(ruta_salida, 'wb') as salida:
        for chunk in open(ruta_pdf, 'rb'):
            salida.write(chunk)
        salida.write(padding)
        for chunk in open(ruta_jpg, 'rb'):
            salida.write(chunk)        


def obtener_imagen(ruta_alterado: str, ruta_imagen:str) -> None:
    """
    Recupera la imagen incrustada en ruta_alterado y
    la guarda en ruta_imagen

    ruta_alterado: str, ruta_imagen:str
    returns: None 
    """
    with open(ruta_imagen, 'wb') as salida:
        with open(ruta_alterado, 'rb') as entrada:
            contenido = entrada.read()
            padding = b'0' * 100
            partes = contenido.split(padding)
            salida.write(partes[1])
            
    
            
if __name__ == '__main__':   
    ruta_pdf = sys.argv[1]
    ruta_jpg = sys.argv[2]
    ruta_salida = sys.argv[3]
    ocultar_imagen(ruta_pdf, ruta_jpg, ruta_salida)
