import sys
import random
import datetime

def burbuja(lista):
    copia = lista.copy()
    # ordenar acá

    return copia

def insercion(lista):
    pass

def esta_ordenada(lista):
    if not lista:
        return True
    anterior = lista[0]
    for siguiente in lista:
        if not anterior <= siguiente:
            return False
        anterior = siguiente
    return True

def probar_burbuja(lista):
    t1 = datetime.datetime.now()
    l = burbuja(lista)
    t2 = datetime.datetime.now()
    microsegundos = (t2 - t1).microseconds
    ordenada = esta_ordenada(l)
    reporte = """
    Burbuja:
    Tiempo: %s microsegundos
    Ordenada: %s
    ------------    
    """
    return reporte % (microsegundos, ordenada)
    

if __name__ == '__main__':
    tamano_lista = int(sys.argv[1])
    lista = [random.randint(0, 100000)
             for _ in range(tamano_lista)]
    t1 = datetime.datetime.now()
    t2 = datetime.datetime.now()
    dif = (t2 - t1).second
    
    # reportar tiempo de ejecución de cada algoritmo
    # comparar con sort y sorted
