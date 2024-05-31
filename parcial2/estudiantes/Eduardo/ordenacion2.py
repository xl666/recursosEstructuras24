import sys
import random
import datetime

def quick_sort(lista_entrada):
    if len(lista_entrada) <= 1:
        return lista_entrada
    pivote = lista_entrada[len(lista_entrada) // 2]
    izquierda = [x for x in lista_entrada if x < pivote]
    medio = [x for x in lista_entrada if x == pivote]
    derecha = [x for x in lista_entrada if x > pivote]
    return quick_sort(izquierda) + medio + quick_sort(derecha)

def merge_sort(lista_entrada):
    if len(lista_entrada) <= 1:
        return lista_entrada
    mitad = len(lista_entrada) // 2
    izquierda = lista_entrada[:mitad]
    derecha = lista_entrada[mitad:]
    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    while izquierda and derecha:
        if izquierda[0] <= derecha[0]:
            resultado.append(izquierda.pop(0))
        else:
            resultado.append(derecha.pop(0))
    while izquierda:
        resultado.append(izquierda.pop(0))
    while derecha:
        resultado.append(derecha.pop(0))
    return resultado

def esta_ordenada(lista):
    if not lista:
        return True
    anterior = lista[0]
    for siguiente in lista:
        if not anterior <= siguiente:
            return False
        anterior = siguiente
    return True

def probar_quick_sort(lista):
    t1 = datetime.datetime.now()
    l = quick_sort(lista)
    t2 = datetime.datetime.now()
    microsegundos = (t2 - t1).microseconds
    ordenada = esta_ordenada(l)
    reporte = """
    Quick Sort:                     
    Tiempo: %s microsegundos
    Ordenada: %s
    ------------    
    """
    return reporte % (microsegundos, ordenada)

def probar_merge_sort(lista):
    t1 = datetime.datetime.now()
    l = merge_sort(lista)
    t2 = datetime.datetime.now()
    microsegundos = (t2 - t1).microseconds
    ordenada = esta_ordenada(l)
    reporte = """
    Merge Sort:                     
    Tiempo: %s microsegundos
    Ordenada: %s
    ------------    
    """
    return reporte % (microsegundos, ordenada)

tamano_lista = int(sys.argv[1])
lista_entrada = [random.randint(0, 100000) for _ in range(tamano_lista)]

print(probar_quick_sort(lista_entrada))
print(probar_merge_sort(lista_entrada))
