import sys
import os

def usuarios_logueables(ruta: str) -> list:
    """
    Regresa los usuarios que se pueden loguear
    en el sistema de acuerdo al archivo de
    entrada.

    ruta: str, archivo tipo passwd
    returns: list 
    """
    res = []
    for usuario in open(ruta):
        usuario = usuario.strip()
        if not usuario.endswith('nologin') and not usuario.endswith('false'):
            res.append(usuario.split(':')[0])

    return res
    


AYUDA = """
py sePuedeLoguar.py archivo

Determina los usuarios que se pueden loguear en el sistema de acuerdo a un archivo tipo passwd

Parámetros:
   - archivo: es un archivo de texto tipo passwd
"""

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Se esperaba un parámetro')
        print(AYUDA)
        exit(1)

    param = sys.argv[1]
    if param == '-h':
        print(AYUDA)
        exit(0)

    if not os.path.isfile(param):
        print('El archivo de entrada debe existir')
        print(AYUDA)
        exit(1)

    usuarios = usuarios_logueables(param)
    print(usuarios)
