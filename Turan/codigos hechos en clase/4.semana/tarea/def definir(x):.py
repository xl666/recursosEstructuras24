def definir(x):
    lista = []
    for i in range(x):
        lista.append(i)
    lista = set(lista)
    return lista

def interseccion(A,B):
    lista_final =[]
    for i in A:
        if i in B:
            lista_final.append(i)
    lista_final.sort        
    return lista_final





if  __name__ == "__main__":
    N = int(input())
    M = int(input())
    lista_1 = definir(N)
    lista_2 = definir(M)
    lista_final = interseccion(lista_1,lista_2)
    print("La lista final es :",lista_final)