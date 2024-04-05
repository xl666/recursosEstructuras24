import random
import datetime
import time

def burbuja(lista):
    copia = lista.copy()
    n = len(copia)
    for i in range(n):
        for j in range(0, n-i-1):
            if copia[j] > copia[j+1]:
                copia[j], copia[j+1] = copia[j+1], copia[j]
    return copia

def insercion(lista):
    copia = lista.copy()
    n = len(copia)
    for i in range(1, n):
        valor_actual = copia[i]
        j = i - 1
        while j >= 0 and valor_actual < copia[j]:
            copia[j + 1] = copia[j]
            j -= 1
        copia[j + 1] = valor_actual
    return copia

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
    l = insercion(lista)
    t2 = datetime.datetime.now()
    microsegundos = (t2 - t1).microseconds
    ordenada = esta_ordenada(l)
    reporte = """
    Inserción Directa:
    Tiempo: %s microsegundos
    Ordenada: %s
    ------------    
    """
    return reporte % (microsegundos, ordenada)

if __name__ == '__main__':
    tamano_lista = int(input("Ingrese el tamaño de la lista: "))
    lista = [random.randint(0, 100000)
             for _ in range(tamano_lista)]
    print(probar_burbuja(lista))
    print(probar_insercion(lista))
