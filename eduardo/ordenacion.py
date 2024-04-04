import sys
import random
import datetime

def burbuja(lista):
    copia = lista.copy()
    n = len(copia)
    for i in range(n):
        for j in range(0, n-i-1):
            if copia[j] > copia[j+1]:
                copia[j], copia[j+1] = copia[j+1], copia[j]
    return copia

def inserciondirecta(lista):
    copia2 = lista.copy()
    for i in range(1, len(copia2)):
        key = copia2[i]
        j = i - 1
        while j >= 0 and key < copia2[j]:
            copia2[j + 1] = copia2[j]
            j -= 1
        copia2[j + 1] = key
    return copia2

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

def probar_insercion(lista):
    t1 = datetime.datetime.now()
    l = inserciondirecta(lista)
    t2 = datetime.datetime.now()
    microsegundos = (t2 - t1).microseconds
    ordenada = esta_ordenada(l)
    reporte = """
    Insercion Directa:                     
    Tiempo: %s microsegundos
    Ordenada: %s
    ------------    
    """
    return reporte % (microsegundos, ordenada)


tamano_lista = int(sys.argv[1])
lista = [random.randint(0, 100000)
         for _ in range(tamano_lista)]