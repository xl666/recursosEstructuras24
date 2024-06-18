def intercalar(lista1, lista2):
    lista_intercalada = []
    
    longitud_lista1 = len(lista1)
    longitud_lista2 = len(lista2)
    longitud_listas = max(longitud_lista1, longitud_lista2)
    
    for i in range(longitud_listas):
        if i < longitud_lista1:
            lista_intercalada.append(lista1[i])
        if i < longitud_lista2:
            lista_intercalada.append(lista2[i])
    return lista_intercalada
            
if __name__ == '__main__':
    n = int(input())
    m = int(input())
    lista1 = [int(input()) for _ in range(n)]
    lista2 = [int(input()) for _ in range(m)]
    
    lista_intercalada = intercalar(lista1, lista2)
    print(lista_intercalada)
    