import shutil
import os
import fnmatch

def obtenerarchivos(directorio, extension):
    """
    obtiene una lista de archivos con una extensión específica en un directorio
    directorio (str): directorio del cual se desean obtener los archivos
    extension (str): extensión de los archivos deseados
    returns (list): lista de archivos con la extensión especificada
    """
    archivos = os.listdir(directorio)
    return fnmatch.filter(archivos, extension)

def copiar_archivos(origen, destino, archivos):
    """
    copia archivos desde una ubicación de origen a una de destino
    origen (str): directorio de origen de los archivos
    destino (str): directorio de destino de los archivos
    archivos (list): lista de nombres de archivos a copiar
    """
    for archivo in archivos:
        ruta_origen = os.path.join(origen, archivo)
        ruta_destino = os.path.join(destino, archivo)
        shutil.copy(ruta_origen, ruta_destino)

patron = "*.txt"
directorioentro = input()
directoriosalida = input()

archivostxt = obtenerarchivos(directorioentro, patron)

copiar_archivos(directorioentro, directoriosalida, archivostxt)