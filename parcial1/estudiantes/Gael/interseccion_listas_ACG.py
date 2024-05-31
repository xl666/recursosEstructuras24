import copy
def llenar_listas(n_elementos):
    lista=[]
    for _ in range (n_elementos):
        lista.append(int(input()))
    return lista
def elementos_comunes (l1,l2):
    l3=[]
    cont=0
    aux=0
    for i in range(len(l1)):
        for j in range (len(l2)):
            if l1[i]==l2[j]:
                l3.append(l1[i])
    lista_buena=sorted(copy.deepcopy(l3))
    while cont<len(lista_buena):
        if lista_buena[cont]==lista_buena[cont-1]:
            del(lista_buena[cont])
            aux+=1
        if aux==len(lista_buena):
            del(lista_buena[1:])
            return lista_buena
        cont+=1
    
    return lista_buena

if __name__=='__main__':
    N=int(input())
    M=int(input())
    N_elementos=llenar_listas(N)
    M_elementos=llenar_listas(M)
    resultado=elementos_comunes(N_elementos,M_elementos)
    print(resultado)
