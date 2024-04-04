import sys
import random
import time as tiempo

def time(fonk):
    def wrappers(*args,**kwargs):
        starts = tiempo.time()
        fonk(*args, **kwargs)
        ends = tiempo.time()
        return ({ends -starts})
    return wrappers

@time
def burbuja(lista):
    copia = lista.copy()
    for i in range(len(copia)):
        for j in range(0, len(copia) -i -1):
            if copia[j] > copia[j+1]:
                copia[j], copia[j+1] = copia[j+1], copia[j]            
    return copia    

@time
def insercion(lista): #[5,2,4,1,3]
    for i in range(1, len(lista)):
        actual = lista[i]
        pos = i-1
        while ( pos >= 0 and lista[pos] > actual):
            lista[pos + 1] = lista[pos]
            pos -= 1
        lista[pos + 1] = actual
    return lista

@time
def esta_ordenada( x , y):
    if not x and not y:
        return True
    if x == y:
        return True
    last = x[0]
    for next in x:
        if last > next:
            return False
        last = next
        return True
    last = y[0]
    for next in y:
        if last > next:
            return False
        last = next
        return True
    return False

@time
def sort(lista):
    l = lista.copy()
    l.sort()
    l1 = sorted(lista)
    return l,l1

    


if __name__ == '__main__':
    tamano_lista = int(sys.argv[1])
    lista = [random.randint(0, 100000) for _ in range(tamano_lista)] 
    inser = insercion(lista)   
    burbu = burbuja(lista)  
    print("Tiempo de ejecucion de la burbuja es '%s' \n"
      "Tiempo de ejecucion de la insercion es '%s' \n"
      "Tiempo de verificacion de las listas es '%s' \n"
      "Teimpo de ejecucion de las listas Sort y Sorted es '%s' \n"  % (
          burbuja(lista),
          insercion(lista),
          esta_ordenada(list(inser),list(burbu)), 
          sort(lista)))
      
    
    
    # Buenas noches maestro. Apliqué un sistema de wrappers. Tenia apenas unas semana de haber aprendido navegando en internet. 
    # Construyo ambos listas , despues compruebo cada lista consiga misma y contra cada uno de los funciones. 
    # Subo un captura de pantalla sobre tiempo de ejecucion  de cada funcion y methodo
    # El sort y sorted dentro misma funcion corre más rapido que otras funciones
    # Favor de avisarme si requiere alguna modificación.
    # Nos vemos en la clase. 

    # Turan Ozbek