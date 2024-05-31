
def imprimir_inverso(n, maximo):
    if n <= maximo: # caso base implícito 
        imprimir_inverso(n + 1, maximo) # primero la llamada recursiva
        print(n)

imprimir_inverso(7,5)        
    