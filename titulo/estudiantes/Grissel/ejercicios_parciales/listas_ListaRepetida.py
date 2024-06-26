def numeros_repetidos(n, lista):
    repetidos = [] # para regresar los números que se repiten

    # iterar sobre cada elemento donde indice i es el primer elemento
    for i in range(n): 
        
        # se reccore la lista desde indice i + 1, donde indice j es el segundo elemento
        for j in range(i + 1, n): # que se va a comparar con el elemento en el indice i
            
            #si elemento en la posicion[i] es igual a elemento de la posicion[j]
            if lista[i] == lista[j] and lista[i] not in repetidos: # y posicion[i] no esta en repetidos
                #return True
                repetidos.append(lista[i])
    #return False            
    return repetidos

if __name__ == '__main__':
    n = int(input())
    lista = [int(input()) for _ in range(n)]
    print(lista)
    print(numeros_repetidos(n, lista))