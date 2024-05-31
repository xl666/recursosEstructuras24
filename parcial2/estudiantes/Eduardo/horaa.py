import sys
import datetime

#respuesta = requests.get("enlace")

def dar_fecha(fuente='sistema': str) -> str:
    '''

    regresa la fecha y hora de acuerdo a la fuente dada
    fuente: str, puede ser sistema o google
    returns: str, una cadena con la fecha y hora

    '''
    if fuente == 'sistema':
        actual = datetime.datetime.now()
        return '%s/%s/%s %s:%s' % (actual.day, actual.month, actual.year, actual.hour, actual.minute)
    else:
        pass
    
def parametros_correctos(parametros: list) -> str:
    '''
    determina si los parametros son correctos
    parametros: list
    returns: str, fuentes de datos
    '''

if not len(parametros) == 1:
        print('tienes que pasar la fuente, google o sistema')
        print(AYUDA)
        exit(1) #termina con error
fuente = parametros[0]
    
if fuente == '-h' or fuente == '-help':
        print(AYUDA)
        exit(0)

if fuente != 'google' and fuente != 'sistema':
        print('la fuente tiene que ser google o sistema')
        print(AYUDA)
        exit(1)

AYUDA = """
python hora.py fuente
  regresa la fecha de acuerdo a la fuente
  parametros:
  - fuente: google o sistema
"""



if __name__ == '__main__':
    fuente = parametros_correctos(sys.argv[1:])
    print('la fecha actual es:')
    print(dar_fecha(fuente))