import sys
import os
import shutil

def txt(dir1): #para checar que los archivos sean .txt
    """
    Esta funcion revisa que los archivos que están en el directorio son archivos .txt
    y los guarda en una lista
    """
    archivos_txt = []
    archivos = os.listdir(dir1)
    for archivo in archivos:
        if archivo.endswith('.txt'):
            archivos_txt.append(archivo)
    return archivos_txt
     
def copiar(dir1, dir2):
    """
    Esta funcion copia los archivo del primer directorio especificado
    al segundo directorio 
    """
    txts = txt(dir1)
    for archivo in txts:
        arch1 = os.path.join(dir1, archivo)
        arch2 = os.path.join(dir2, archivo)
        shutil.copy(arch1, arch2)

AYUDA = """
python copiar_txts.py directorio1 directorio2
Copia archivos en otra carpeta
    Parámetros:
        - directorio_entrada: opcional, directorio de donde se va copiar
        si no se especifica es el directorio actual (.)
        - directorio_ salida: directorio a donde se va a copiar
"""        

if __name__ == '__main__':
    #directorios = parametros(sys.argv[1:])
    if not len(sys.argv) <= 3:
        print('Tienes que pasar dos directorios')
        print(AYUDA)
        exit(1)

    dir2 = sys.argv[1]
    dir1 = sys.argv[2]

    if dir1 == '.':
        dir1 = os.getcwd()

    if not dir1:
        dir1 = os.getcwd()

    if not os.path.isdir(dir1) and os.path.isdir(dir2):
        print('Debes ingresar un directorio existente')
        print(AYUDA)
        exit(1)
    
    copiar(dir2, dir1)