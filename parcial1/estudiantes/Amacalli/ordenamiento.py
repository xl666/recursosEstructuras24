import sys
import random
import datetime

def burbuja(lista):
    copia = lista.copy()
    # ordenar acá
    for i in range(0, len(copia) - 1):
    #Bucle para numero de vueltas
        for j in range(1, len(copia) - 1):
        #Bucle para comparacion e intercambio
            if copia[j] == copia[j + 1]:
                aux = copia[j]
                copia[j] = copia[j + 1]
                copia[j + 1] = aux
    return copia

def insercion(lista):
    copia2 = lista.copy()
    for i in range(1, len(copia2)):
        valor = copia2[i] #Toma el siguiente valor a ser insertado
        indice = i #Indice donde se insertará el valor

        while indice > 0 and copia2[indice - 1] > valor:
            copia2[indice] = copia2[indice - 1]
            indice -= 1 

        #Se inserta el valor en su indice correspondiente
        copia2[indice] = valor
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
    l2 = insercion(lista)
    t2 = datetime.datetime.now()
    microsegundo = (t2 - t1).microseconds
    ordenada = esta_ordenada(l2)
    reporte = """
    Insercion directa:
    Tiempo %s microsegundos
    Ordenada: %s
    ------------
    """
    return reporte % (microsegundo, ordenada)

if __name__ == '__main__':
    tamano_lista = int(sys.argv[1])
    lista = [random.randint(0, 100000)
             for _ in range(tamano_lista)]
    #t1 = datetime.datetime.now()
    #t2 = datetime.datetime.now()
    #dif = (t2 - t1).second

    burbuja(lista)
    insercion(lista)
    print(probar_burbuja(lista))
    print(probar_insercion(lista))
    

    # reportar tiempo de ejecución de cada algoritmo
    # comparar con sort y sorted