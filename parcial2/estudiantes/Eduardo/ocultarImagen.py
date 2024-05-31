import sys

def extraer_archivo_oculto(ruta_pdf, ruta_archivo_extraido) -> None:
    """
    extrae el archivo escondido de un pdf
    ruta_pdf: ruta del archivo pdf
    ruta_archivo_extraido: ruta donde se guarda el archivo extraido del pdf
    returns: None
    """
    relleno = b'0' * 100  

    with open(ruta_pdf, 'rb') as archivo_pdf:
        contenido_pdf = archivo_pdf.read()
        indice_relleno = contenido_pdf.find(relleno)

        if indice_relleno != -1:
            indice_inicio_archivo = indice_relleno + len(relleno)
            contenido_archivo = contenido_pdf[indice_inicio_archivo:]

            with open(ruta_archivo_extraido, 'wb') as archivo_extraido:
                archivo_extraido.write(contenido_archivo)
        else:
            print("no se encontro nada")

if __name__ == '__main__':
    ruta_pdf = sys.argv[1]
    ruta_archivo_extraido = sys.argv[2]
    extraer_archivo_oculto(ruta_pdf, ruta_archivo_extraido)

# cd C:\Users\eduar\OneDrive\Escritorio
# python3 ocultarimagen.py C:\Users\eduar\OneDrive\Escritorio\modificada.pdf C:\Users\eduar\OneDrive\Escritorio\imagen.jpg  
