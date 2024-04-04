import sys
import random
import datetime

def burbuja(lista):
    k=0#para que deje de recorres los último elementos, por cada ciclo se van ordenando los últimos elementos
    for i in range(len(lista)-1):
        n=0
        for j in range(len(lista)-k):
            aux=lista[j]
            if n<(len(lista)-1):
                if lista[j]>lista[j+1]:
                    aux=lista[j+1]
                    lista[j+1]=lista[j]
                    lista[j]=aux
            n+=1
        k+=1
    return lista

def insercion(lista):
    for j in range(len(lista)):
        n=0
        if j>0:
            k=0
            while n<(j+1):
                if lista[j]<lista[j-n]:
                    k+=1
                n+=1
            menor=lista[j]
            del(lista[j])
            lista.insert(j-k,menor)
    return lista

def esta_ordenada(lista):
    if not lista:
        return True
    anterior = lista[0]
    for siguiente in lista:
        if not anterior <= siguiente:
            return False
        anterior = siguiente
    return True

def probar_algoritmos(lista):
    t1 = datetime.datetime.now()
    l = burbuja(lista)
    t2 = datetime.datetime.now()
    microsegundos_burbuja = (t2 - t1).microseconds
    ordenada_burbuja=esta_ordenada(l)
    t3 = datetime.datetime.now()
    l2=insercion(lista)
    t4 = datetime.datetime.now()
    microsegundos_insercion = (t4 - t3).microseconds
    ordenada_insercion = esta_ordenada(l2)
    t5 = datetime.datetime.now()
    l3=lista.sort()
    t6 = datetime.datetime.now()
    microsegundos_sort= (t6 - t5).microseconds
    t7 = datetime.datetime.now()
    l4=sorted(lista)
    t8 = datetime.datetime.now()
    microsegundos_sorted= (t8 - t7).microseconds
    reporte = """
    Burbuja:
    Tiempo: %s microsegundos
    Ordenada: %s
    ------------ 
    Insercion
    Tiempo: %s microsegundos
    Ordenada: %s
    ------------
    Sort
    Tiempo: %s microsegundos
    -------------
    Sorted
    TIempo: %s microsegundos
    """
    return reporte % (microsegundos_burbuja, ordenada_burbuja,microsegundos_insercion,ordenada_insercion, microsegundos_sort, microsegundos_sorted)
    

if __name__ == '__main__':
    tamano_lista = int(sys.argv[1])
    lista = [random.randint(0, 100000)
             for _ in range(tamano_lista)]
    print(probar_algoritmos(lista))
    
    # reportar tiempo de ejecución de cada algoritmo
    # comparar con sort y sorted