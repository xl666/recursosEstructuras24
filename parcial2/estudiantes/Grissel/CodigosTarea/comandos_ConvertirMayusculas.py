archivo = '/home/griss/Escritorio/SegundoParcial/CodigosTarea/hola/miarchivo.txt'
nuevo_archivo = '/home/griss/Escritorio/SegundoParcial/CodigosTarea/hola/archivomayus.txt'
#with open (archivo, 'r') as minuscula:
#    contenido = minuscula.read()
for linea in open(archivo):
    linea_a_mayuscula = linea.upper()
    nuevo_archivo.write(linea_a_mayuscula)


#with open(nuevo_archivo, 'w') as mayuscula:
    #mayuscula.write(nuevo)
