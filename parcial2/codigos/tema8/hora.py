import sys
import datetime
import requests

    
def dar_fecha(fuente='sistema') -> str:
    """
    Regresa la fecha y hora de acuerdo a la fuente
    dada

    fuente: str, puede ser sistema o google
    returns: str, una cadena con la fecha y hora
    
    """
    if fuente == 'sistema':
        actual = datetime.datetime.now()
        return '%s/%s/%s %s:%s' % (actual.day, actual.month, actual.year, actual.hour, actual.minute)
    else:
        separador = '<div class="BNeawe iBp4i AP7Wnd">'
        url = 'https://www.google.com/search?q=hora'
        res = requests.get(url)
        if res.status_code == 200:
            contenido = res.text
            partes = contenido.split(separador)
            hora = partes[2][:5]
            return hora


def parametros_correctos(parametros: list) -> str:
    """
    Determina si los parámetros están correctos.

    parametros: list
    returns: str, fuente de datos
    """
    if not len(parametros) == 1:
        print('Tienes que pasar la fuente, googlo o sistema')
        print(AYUDA)
        exit(1) # terminación con error
    fuente = parametros[0]

    if fuente == '-h' or fuente == '--help':
        print(AYUDA)
        exit(0)
    
    if fuente != 'google' and fuente != 'sistema':
        print('La fuente tiene que ser google o sistema')
        print(AYUDA)
        exit(1)

    return fuente
    
AYUDA = """
python hora.py fuente
Regresa la fecha de acuerdo a la fuente
   Parámetros:
   - fuente: google o sistema
"""

if __name__ == '__main__':

    fuente = parametros_correctos(sys.argv[1:])
    print('La fecha actual es:')
    print(dar_fecha(fuente))
