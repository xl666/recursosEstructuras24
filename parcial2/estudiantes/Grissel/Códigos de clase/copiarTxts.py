import sys
import os
import shutil

def parametros_correctos(params: list) -> bool:
    """
    Determina si se pasaron bien los parámetros.

    params: list
    returns: bool True si todo está bien
    """
    if len(params) != 1 and len(params) != 2:
        return False
    if not os.path.isdir(params[0]):
        return False
    if len(params) == 2:
        if not os.path.isdir(params[1]):
            return False

    return True

def copiar_txts(ruta_salida: str, ruta_entrada='.') -> None:
    """
    Copia los archivos txt de ruta_entrada a ruta_salida.

    ruta_salida: str,
    ruta_entrada='.'
    returns: None 
    """
    archivos_copiar = ['%s/%s' % (ruta_entrada, arch) for arch in os.listdir(ruta_entrada) if arch.endswith('.txt') and os.path.isfile('%s/%s' % (ruta_entrada, arch))]
    for archivo in archivos_copiar:
        shutil.copy(archivo, ruta_salida)
    
    

AYUDA = """
python copiarTxts.py ruta_salida [ruta_entrada]

Copia los archivos con extensión txt de ruta_entrada a ruta_salida
Parámetros:
    - ruta_salida: ruta de directorio donde se guardarán los txt
    - ruta_entrada: opcional, ruta de directorio donde están los txt, si no se pasa es el directorio actual (.)
"""

if __name__ == '__main__':
    params = sys.argv[1:]
    if not parametros_correctos(params):
        print(AYUDA)
        exit(1)
    if len(params) == 2:
        ruta_salida, ruta_entrada = params
        copiar_txts(ruta_salida, ruta_entrada)
    else:
        ruta_salida = params[0]
        copiar_txts(ruta_salida)