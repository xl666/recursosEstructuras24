def listas(N,M):
    lista_1 =[]
    lista_aux =[]
    for elemento in range(N):
        elemento= int(input())
        lista_1.append(elemento)
    for elemento in range(M):
        elemento = int(input())
        if elemento in lista_1:
                lista_aux.append(elemento)
    lista_aux.sort()
    lista_aux = list(set(lista_aux))
    return lista_aux
        
if  __name__ == "__main__":
    N= int(input())
    M= int(input())
    lista_aux = listas(N,M)
    print(lista_aux)


    #Turan Ozbek