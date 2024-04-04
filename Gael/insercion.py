def insercion (lista):
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
            print(lista)
    return lista

if __name__=='__main__':
    longitud=int(input())
    lista=[int(input()) for _ in range (longitud)]
    print(insercion(lista))