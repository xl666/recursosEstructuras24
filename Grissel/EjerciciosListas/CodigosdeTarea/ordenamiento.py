import sys
import random
import datetime

def burbuja(lista):
    n = len(lista)
    for i in range(n-1):       # <-- este es el bucle padre
        for j in range(n-1-i): # <-- este es el bucle hijo
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def insercion(lista):
    for i in range(len(lista)):
        for j in range(i,0,-1):
            if lista[j-1] > lista[j]:
                lista[j-1], lista[j] = lista[j], lista[j-1]

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
    ordenada_previamente = esta_ordenada(lista)
    t1 = datetime.datetime.now()
    l = burbuja(lista)
    t2 = datetime.datetime.now()
    microsegundos = (t2 - t1).microseconds
    ordenada = esta_ordenada(l)
    if ordenada_previamente and ordenada:
        ordenada = True
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
    ordenada = esta_ordenada(lista)
    reporte = """
    Inserción directa:
    Tiempo: %s microsegundos
    Ordenada: %s
    ------------    
    """
    return reporte % (microsegundos, ordenada)

if __name__ == '__main__':
    tamano_lista = int(sys.argv[1])
    lista = [random.randint(0, 100000)
             for _ in range(tamano_lista)]
    
    print(probar_burbuja(lista))
    print(probar_insercion(lista))
    
    t1 = datetime.datetime.now()
    lista.sort()
    t2 = datetime.datetime.now()
    tiempo_sort = (t2 - t1).microseconds
    
    t1 = datetime.datetime.now()
    sorted_lista = sorted(lista)
    t2 = datetime.datetime.now()
    tiempo_sorted = (t2 - t1).microseconds
    
    print("\nTiempo de ejecución de sort:", tiempo_sort, "microsegundos")
    print("Tiempo de ejecución de sorted:", tiempo_sorted, "microsegundos")
